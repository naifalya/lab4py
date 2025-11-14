# List dan Tuple

## Modul Praktikum 4

### LATIHAN
Latihan ini bertujuan untuk menguji kemampuan dasar terhadap list, yaitu:
1. **Indexing** = mengambil nilai berdasar posisi
2. **Slicing** = mengambil potongan list
3. **Assignment** = mengubah nilai dalam list
4. **Append & extend** = menambahkan item ke dalam list
5. **Concatenation** = menggabungkan list

Berikut adalah dokumentasi proses pengerjaan latihan:
<img width="673" height="417" alt="1Latihan" src="https://github.com/user-attachments/assets/dc17dbfe-dfb0-41d0-86ae-c32f8af1025b" />
<img width="725" height="215" alt="2Latihan" src="https://github.com/user-attachments/assets/1b69dcfc-f936-4767-b91b-49b75b02a077" />

Dan, berikut adalah output dari latihan tersebut:
![Dokumentasi](Dokumentasi/HasilL.png)

### PRAKTIKUM
Dibuat program yang dapat menambahkan data mahasiswa sebanyak-banyaknya ke dalam list, lalu menampilkan daftar data ketika pengguna berhenti memasukkan input.
1. **Membuat list kosong** = List digunakan untuk menyimpan data mahasiswa lebih dari satu. Setiap mahasiswa akan disimpan sebagai dictionary dan dimasukkan ke dalam list ini menggunakan append().
2. **Mulai perulangan input** = While True digunakan agar program terus berulah sampai ada perintah `break`.
3. **Menginput data mahasiswa** = Data per mahasiswa disimpan kedalam Dictionary agar data terstruktur, mudah diproses dalam loop. Semua nilai tugas, UTS, dan UAS dikonversi ke `float` karena bertipe angka.
4. **Menghitung nilai akhir** = Menggunakan rumus bobot 30% dari tugas, 35% dari UTS dan 35% dari UAS. Nilai kemudian dibulatkan.
5. **Menyimpan dictionary ke list** = Setiap mahasiswa baru akan ditambahkan ke list.
6. **Mengkonfirmasi data** = Jika user mengetik “t”: loop berhenti dan lanjut menampilkan data. Namun, jika mengetik “y”: kembali ke awal loop (input lagi)
7. **Menampilkan tabel** = Hasil akhirnya adalah tabel dengan penggunaan fungsi <20, <15, <8, dst. agar kolom tabel rapi.

Berikut adalah dokumentasi proses pengerjaan praktikum:
<img width="755" height="446" alt="1Praktikum" src="https://github.com/user-attachments/assets/7e73ac52-2b33-45a0-be3e-888283871a0c" />
<img width="887" height="293" alt="2Praktikum" src="https://github.com/user-attachments/assets/c19431f8-7d09-4fa5-872a-ee2c86f590f7" />

Berikut adalah alur kerja program pendataan nilai mahasiswa:
<img width="233" height="581" alt="flowchartP" src="https://github.com/user-attachments/assets/043e1c52-3b91-4794-bba7-5eb2f4d17661" />

Dan, berikut adalah output dari latihan tersebut:
<img width="634" height="419" alt="HasilP" src="https://github.com/user-attachments/assets/f365864d-adc9-4914-9e42-1876747ec36c" />




