# PROGRAM HITUNG GAJI KARYAWAN
print("=== PROGRAM HITUNG GAJI KARYAWAN PT. DINSIN DAMAI ===")

# Input data karyawan
nama = input("Nama Karyawan        : ")
golongan = input("Golongan Jabatan [1/2/3] : ")
pendidikan = input("Pendidikan [SMA/D1/D3/S1] : ").upper()
jam_kerja = int(input("Jumlah Jam Kerja         : "))

# Gaji pokok
gaji_pokok = 300000

# Hitung tunjangan jabatan
if golongan == "1":
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == "2":
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == "3":
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid!")

# Hitung tunjangan pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0
    print("Pendidikan tidak valid!")

# Hitung honor lembur
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0

# Total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

# Tampilkan hasil
print("\n=== HASIL PERHITUNGAN GAJI ===")
print(f"Karyawan yang bernama   : {nama}")
print(f"Tunjangan Jabatan       : Rp {tunjangan_jabatan:,.0f}")
print(f"Tunjangan Pendidikan    : Rp {tunjangan_pendidikan:,.0f}")
print(f"Honor Lembur            : Rp {lembur:,.0f}")
print("------------------------------------------ +")
print(f"Total Gaji              : Rp {total_gaji:,.0f}")