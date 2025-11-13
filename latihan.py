# Latihan Manipulasi List

# 1. Buat sebuah list sebanyak 5 elemen dengan nilai bebas
A = [6, 15, 20, 35, 50]
print("List A awal:", A)

# 2. Akses list
print("Elemen ke-3 (indeks 2):", A[2])  # Tampilkan elemen ke-3
print("Elemen ke-2 sampai ke-4 (indeks 1-3):", A[1:4])  # Ambil nilai elemen ke-2 sampai ke-4
print("Elemen terakhir:", A[-1])  # Ambil elemen terakhir

# 3. Ubah elemen list
A[3] = 77  # Ubah elemen ke-4 dengan nilai lainnya
print("Setelah ubah elemen ke-4:", A)

# Ubah elemen ke-4 sampai dengan elemen terakhir (indeks 3 sampai akhir)
A[3:] = [88, 99]
print("Setelah ubah elemen ke-4 sampai terakhir:", A)

# 4. Tambah elemen list
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke-2 (B)
B = A[:2]  # Ambil 2 elemen pertama dari A
print("List B (2 elemen pertama dari A):", B)

# Tambah list B dengan nilai string
B.append("world")
print("List B setelah tambah string:", B)

# Tambah list B dengan 3 nilai
B.extend([11, 112, 113])
print("List B setelah tambah 3 nilai:", B)

# Gabungkan list B dengan list A
A.extend(B)
print("List A setelah digabungkan dengan B:", A)
