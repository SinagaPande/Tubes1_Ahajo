from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position

class HCLBot(BaseLogic):
    def __init__(self):
        pass

    def get_obj_pos(self, board: Board):
        self.diamonds = []
        self.bots = []
        self.teleport = []

        for obj in board.game_objects:
            if obj.type == "DiamondGameObject" or obj.type == "DiamondButtonGameObject":
                self.diamonds.append(obj)
            elif obj.type == "BotGameObject":
                self.bots.append(obj)
            elif obj.type == "TeleportGameObject":
                self.teleport.append(obj)
    
    def calculate_distance(self,x1,y1,x2,y2) -> float:
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def check_enemy(self,board_bot: GameObject, board: Board) -> tuple[Position, bool]:
        for bot in self.bots:
            if bot.id != board_bot.id and self.calculate_distance(board_bot.position.x, board_bot.position.y, bot.position.x, bot.position.y) < 2:
                return bot.position, True
        return bot.position, False
    
    def find_teleport_distance(self, x, y) -> tuple[GameObject, GameObject]:
        min_dist = float('inf')
        max_dist = float(-1.0)
        nearest_teleport = None
        farthest_teleport = None
        for tele in self.teleport:
            dist = self.calculate_distance(x, y, tele.position.x, tele.position.y)
            if dist < min_dist:
                min_dist = dist
                nearest_teleport = tele
            if dist > max_dist:
                max_dist = dist
                farthest_teleport = tele
        return nearest_teleport, farthest_teleport

    def next_move(self, board_bot: GameObject, board: Board):
        self.get_obj_pos(board)
        min_dist = float('inf')
        goals_pos = self.diamonds[0]
        nearest_teleport, farthest_teleport = self.find_teleport_distance(board_bot.position.x, board_bot.position.y)
        if board_bot.properties.diamonds == board_bot.properties.inventory_size:
            if self.check_enemy(board_bot, board)[1]:
                goals_pos = self.check_enemy(board_bot, board)[0]
            else:
                base_distance = self.calculate_distance(board_bot.position.x, board_bot.position.y, board_bot.properties.base.x, board_bot.properties.base.y)
                base_distance_teleport = self.calculate_distance(board_bot.position.x, board_bot.position.y, nearest_teleport.position.x, nearest_teleport.position.y) + self.calculate_distance(farthest_teleport.position.x, farthest_teleport.position.y, board_bot.properties.base.x, board_bot.properties.base.y)
                if base_distance_teleport < base_distance:
                    goals_pos = nearest_teleport.position
                else:
                    goals_pos = board_bot.properties.base
        else:
            inventory_space = board_bot.properties.inventory_size - board_bot.properties.diamonds
            for d in self.diamonds:
                if self.check_enemy(board_bot, board)[1]:
                    goals_pos = self.check_enemy(board_bot, board)[0]
                elif self.calculate_distance(board_bot.position.x, board_bot.position.y, d.position.x, d.position.y) < min_dist:
                    point = d.properties.points or 0
                    if point <= inventory_space:
                        goals_pos = d.position
                        min_dist = self.calculate_distance(board_bot.position.x, board_bot.position.y, d.position.x, d.position.y)

            #nearest_dm_with_teleport = None
            for d in self.diamonds:
                diamond_distance = self.calculate_distance(d.position.x, d.position.y, farthest_teleport.position.x, farthest_teleport.position.y) + self.calculate_distance(board_bot.position.x, board_bot.position.y, nearest_teleport.position.x, nearest_teleport.position.y)
                if  diamond_distance < min_dist:
                    point = d.properties.points or 0
                    if point <= inventory_space:
                        goals_pos = nearest_teleport.position
                        min_dist = diamond_distance
                        
            print(f"Non teleport distance: {min_dist}")
            print(f"Teleport distance: {diamond_distance}")

        if(board_bot.position.x > goals_pos.x):
            delta_x = -1
            delta_y = 0
        elif(board_bot.position.x < goals_pos.x):
            delta_x = 1
            delta_y = 0
        elif(board_bot.position.y > goals_pos.y):
            delta_x = 0
            delta_y = -1
        else:
            delta_x = 0
            delta_y = 1

        return delta_x, delta_y
