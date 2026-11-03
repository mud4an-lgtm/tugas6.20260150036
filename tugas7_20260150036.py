
# ------------------------------------------
# SISTEM EVALUASI KELAYAKAN ASLAB AI
# ------------------------------------------

import tugas7.modul_evaluasi as modul_evaluasi


# 1. Fungsi validasi input angka
def input_angka_valid(prompt, min_val, max_val):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < min_val or nilai > max_val:
                print("[WARNING] Angka harus antara",
                      min_val, "sampai", max_val)
            else:
                return nilai
        except ValueError:
            print("[ERROR] Input harus berupa angka!")
            print("Silakan masukkan kembali.")


# 2. Menu utama
while True:

    print("\n---------------------------------")
    print(" SISTEM EVALUASI KELAYAKAN ASLAB")
    print("-----------------------------------")
    

    try:
            # identitas
            print("\n--- DATA MAHASISWA ---")
            nama = input("Masukkan Nama: ")
            nim = input("Masukkan NIM: ")
            # kehadiran
            hadir = input_angka_valid(
                "Jumlah Kehadiran (0-14): ", 0, 14)
            # nilai
            print("\n--- INPUT NILAI ---")
            tugas = input_angka_valid(
                "Nilai Tugas (0-100): ", 0, 100)
            ucp1 = input_angka_valid(
                "Nilai UCP 1 (0-100): ", 0, 100)
            ucp2 = input_angka_valid(
                "Nilai UCP 2 (0-100): ", 0, 100)
            # Proses perhitungan
            persentase = modul_evaluasi.hitung_persentase_presensi(hadir)
            nilai_akhir = modul_evaluasi.hitung_nilai_akhir(
                tugas, ucp1, ucp2)
            status = modul_evaluasi.cek_kelayakan_aslab(
                persentase, nilai_akhir)
            print("\n===================================")
            print("       HASIL EVALUASI ASLAB")
            print("===================================")

            print("Nama              :", nama)
            print("NIM               :", nim)
            print("Kehadiran         :", hadir, "/ 14")
            print("Persentase Hadir  :", round(persentase, 2), "%")
            print("Nilai Akhir       :", round(nilai_akhir, 2))
            print("-----------------------------------")
            print("STATUS            :", status)
            print("===================================")

        

    except ValueError:
        print("[ERROR]")
