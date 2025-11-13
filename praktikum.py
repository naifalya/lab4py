# Program untuk menambahkan data mahasiswa ke dalam list

# List kosong untuk menyimpan data
data_mahasiswa = []

while True:
    # Meminta input data mahasiswa
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    # Hitung nilai akhir: 30% tugas + 35% UTS + 35% UAS
    nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)

    # Simpan data sebagai dictionary ke dalam list
    mahasiswa = {
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": round(nilai_akhir, 2)
    }
    data_mahasiswa.append(mahasiswa)

    # Pertanyaan untuk menambah data lagi
    tambah_lagi = input("Tambah data lagi? (y/t): ").lower()
    if tambah_lagi == 't':
        break

# Tampilkan daftar data setelah loop selesai
print("\nDaftar Data Mahasiswa:")
print("-" * 80)
print(f"{'No.':<5} {'Nama':<20} {'NIM':<15} {'Tugas':<8} {'UTS':<8} {'UAS':<8} {'Nilai Akhir':<12}")
print("-" * 80)
for i, mhs in enumerate(data_mahasiswa, start=1):
    print(
        f"{i:<5} {mhs['nama']:<20} {mhs['nim']:<15} {mhs['tugas']:<8} {mhs['uts']:<8} {mhs['uas']:<8} {mhs['nilai_akhir']:<12}")
print("-" * 80)
