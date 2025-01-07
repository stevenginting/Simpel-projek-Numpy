import numpy as np

pengangguran_bulanan = [4.6, 4.9, 5.1, 5.3, 4.7, 5.4, 5.2, 4.8, 5.1, 4.7, 4.9, 5.2]

#TUGAS 1
rata_rata = np.mean(pengangguran_bulanan)
# print(rata_rata)
tengah = np.median(pengangguran_bulanan)
print(tengah)

#----------------------------------#
#TUGAS 2
laju_perubahan = np.diff(pengangguran_bulanan)
#print(laju_perubahan)
rata_rata_perubahan = np.mean(laju_perubahan)
#print(rata_rata_perubahan)

if rata_rata_perubahan < 0:
    print("penurunan")
else:
    print("kenaikan!!")