Natasya labaso F55123016
(Pscode Marge Sort)

Pscode untuk marge sort
MERGE_SORT(array):
    jika panjang(array) <= 1:
        kembalikan array  // Basis rekursi: jika array hanya berisi 1 elemen, kembalikan array
    tengah = panjang(array) // 2  // Tentukan titik tengah array
    kiri = MERGE_SORT(array[0:tengah])  // Rekursi untuk bagian kiri array
    kanan = MERGE_SORT(array[tengah:])  // Rekursi untuk bagian kanan array
    kembalikan MERGE(kiri, kanan)  // Gabungkan dua bagian yang terurut

MERGE(kiri, kanan):
    hasil = []  // Array untuk menyimpan hasil penggabungan
    i, j = 0, 0  // Indeks awal untuk kedua array (kiri dan kanan)
    
    selama i < panjang(kiri) dan j < panjang(kanan):  // Selama elemen-elemen di kedua array masih ada
        jika kiri[i] <= kanan[j]:
            tambahkan kiri[i] ke hasil
            i = i + 1
        selain itu:
            tambahkan kanan[j] ke hasil
            j = j + 1

    tambahkan sisa elemen kiri[i:] ke hasil  // Tambahkan sisa elemen dari kiri
    tambahkan sisa elemen kanan[j:] ke hasil  // Tambahkan sisa elemen dari kanan
    kembalikan hasil


1.Analisis Big O (Waktu Terburuk)
Pada fungsi MERGE, kita melakukan beberapa langkah penting:
-Perbandingan Elemen: Proses utama adalah membandingkan elemen dari array kiri dan kanan 
 menggunakan dua indeks. Proses ini berlanjut hingga salah satu array habis.
-Menambahkan Sisa Elemen: Setelah perbandingan, sisa elemen dari array yang belum habis 
 ditambahkan ke hasil. Operasi ini tetap memerlukan waktu O(n), dengan n adalah jumlah total 
 elemen.
-Total Perbandingan dan Penggabungan: Setiap perbandingan dan penambahan elemen berlangsung 
 sebanyak n kali, yaitu jumlah total elemen yang digabungkan dari kedua array.

2.Analisis Big Theta (Waktu Rata-Rata dan Terburuk)
 Fungsi MERGE memiliki waktu yang konsisten, yaitu O(n) pada semua kasus (terbaik, rata-rata, 
 dan terburuk), karena kita selalu melakukan perbandingan dan penambahan elemen untuk n elemen  kiri + kanan). Jadi, Big Theta untuk fungsi MERGE adalah Θ(n).


Pscode untuk Buble sort
BUBBLE_SORT(array):
    n = panjang(array)
    untuk i dari 0 hingga n-1:
        untuk j dari 0 hingga n-i-2:
            jika array[j] > array[j + 1]:
                tukar(array[j], array[j + 1])
    kembalikan array


1.Analisis Big O (Waktu Terburuk)
-Pada setiap iterasi luar (i), perulangan dalam (j) membandingkan elemen bersebelahan dan 
 melakukan pertukaran jika perlu.
-Iterasi pertama melakukan perbandingan n-1 kali, iterasi kedua n-2 kali, dan seterusnya.

2.Analisi Big Theta (Waktu Rata-Rata dan Terbaik)
-Waktu Rata-Rata: Bubble Sort tetap memerlukan perbandingan untuk hampir semua elemen, 
 meskipun beberapa sudah terurut. Oleh karena itu, Θ(n²).
-Waktu Terbaik: Meskipun array sudah terurut, Bubble Sort tetap memeriksa setiap elemen untuk 
 memastikan tidak ada pertukaran, sehingga Θ(n²).


 

