import numpy as np

pengangguran_bulanan = [4.6, 4.9, 5.1, 5.3, 4.7, 5.4, 5.2, 4.8, 5.1, 4.7, 4.9, 5.2]

# Statistik Deskriptif
rata_rata = np.mean(pengangguran_bulanan)
median = np.median(pengangguran_bulanan)
nilai_terbesar = np.max(pengangguran_bulanan)
nilai_terkecil = np.min(pengangguran_bulanan)
bulan_tertinggi = np.argmax(pengangguran_bulanan) + 1  # Menambahkan 1 karena indeks mulai dari 0
bulan_terendah = np.argmin(pengangguran_bulanan) + 1  # Menambahkan 1 karena indeks mulai dari 0

print(f"Rata-rata Tingkat Pengangguran: {rata_rata:.2f}%")
print(f"Median Tingkat Pengangguran: {median:.2f}%")
print(f"Tingkat Pengangguran Tertinggi: {nilai_terbesar:.2f}% pada bulan {bulan_tertinggi}")
print(f"Tingkat Pengangguran Terendah: {nilai_terkecil:.2f}% pada bulan {bulan_terendah}")

# Analisis Tren Bulanan
laju_perubahan = np.diff(pengangguran_bulanan)
rata_rata_perubahan = np.mean(laju_perubahan)

if rata_rata_perubahan < 0:
    print("Terdapat tren penurunan tingkat pengangguran.")
else:
    print("Terdapat tren kenaikan tingkat pengangguran.")
