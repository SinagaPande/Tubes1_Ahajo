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
./run-bots.bat

Identitas Pembuat (Author)
M. Fadhil Hawari 123140147 
Abel Fortino 123140111 
Jonathan Nicholaus Damero Sinaga 123140153 

