# Tubes1_Ahajo
Penjelasan Algoritma Greedy yang Diimplementasikan
Strategi utama yang diterapkan dalam bot ini mengadopsi pendekatan greedy berbasis jarak terdekat dengan pertimbangan keamanan dari bot lawan dan teleportasi. Bot secara konsisten memilih diamond terdekat yang sesuai dengan kapasitas inventory saat ini, dengan mekanisme fallback ke penghindaran musuh ketika terdeteksi bahaya. Implementasi ini menggabungkan tiga lapisan strategi: 
1.	prioritas keamanan melalui pengecekan musuh dalam radius 2 unit  
2.	optimasi rute menggunakan portal teleport ketika menguntungkan 
3.	default ke algoritma greedy konvensional pencarian diamond terdekat 
Dari segi efektivitas, strategi ini mengutamakan dalam beberapa aspek seperti: 
1.	Manajemen risiko dengan melakukan penghindaran musuh yang dimulai ketika inventory penuh 
2.	Optimalisasi gerakan melalui analisis biaya-manfaat penggunaan teleport yang dihitung berdasarkan jarak antara Bot dengan teleportasi dan jarak teleportasi dengan GameObject lain seperti Diamond maupun Base 
3.	Keputusan yang berbeda saat inventory kosong dan saat penuh 

Langkah Menjalankan atau Build Program
LANGKAH-LANGKAH MENJALANKAN PROGRAM (BUILD/RUN)

1. Install Python
   Pastikan Python versi 3 sudah terinstal.
   Download di sini: [https://www.python.org/downloads](https://www.python.org/downloads)

2. Download dan Extract Source Code
   Download file .zip dari Bot Starter Pack.
   Extract ke folder, misalnya: tubes1-IF2110-bot-starter-pack-1.0.1

3. Masuk ke folder project
   Buka terminal (Command Prompt / Powershell / Terminal Linux), lalu jalankan:
   cd C:\Users\nama\_user\Downloads\tubes1-IF2110-bot-starter-pack-1.0.1
   (Sesuaikan path-nya dengan folder kamu)

4. Install dependency (library)
   Jalankan perintah:
   pip install -r requirements.txt
   Ini akan menginstal semua kebutuhan program yang ada di file requirements.txt

5. Letakkan file bot kamu
   Misalnya kamu punya file bernama Bot1.py, letakkan di dalam folder:
   game/logic/Bot1.py

6. Daftarkan bot kamu di main.py
   Buka file main.py, lalu lakukan dua hal berikut:
   a. Tambahkan baris import:
   from game.logic.Bot1 import Bot1
   b. Tambahkan ke dalam dictionary CONTROLLERS seperti ini:
   CONTROLLERS = {
   "Random": Random,
   "Bot1": Bot1
   }

7. Jalankan bot kamu
   Jalankan perintah:
   python main.py --logic Bot1 --email=[mfadhil.123140147@student.itera.ac.id](mailto:mfadhil.123140147@student.itera.ac.id) --name=Hawari --password=123 --team etimo
   Keterangan:
   \--logic diisi sesuai nama class kamu
   \--email dan --name harus berbeda untuk tiap bot
   \--password bebas, jangan pakai spasi
   \--team wajib diisi "etimo"

8. (Opsional) Menjalankan banyak bot
   Untuk Windows: jalankan file run-bots.bat
   Untuk Linux atau macOS: jalankan file run-bots.sh
   Edit dulu isi file .bat atau .sh agar sesuai dengan logic, email, name, dan password masing-masing bot

Identitas Pembuat (Author)
M. Fadhil Hawari 123140147 
Abel Fortino 123140111 
Jonathan Nicholaus Damero Sinaga 123140153 

