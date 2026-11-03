
# ==========================================
# MODUL EVALUASI KELAYAKAN ASLAB
# ==========================================

# 1. Menghitung persentase kehadiran
def hitung_persentase_presensi(hadir, total_pertemuan=14):
    persentase = (hadir / total_pertemuan) * 100
    return persentase
# 2. Menghitung nilai akhir
def hitung_nilai_akhir(tugas, ucp1, ucp2):
    nilai = (tugas * 0.20) + (ucp1 * 0.40) + (ucp2 * 0.40)
    return nilai
# 3. Mengecek kelayakan asisten laboratorium
def cek_kelayakan_aslab(persentase_presensi, nilai_akhir):
    if persentase_presensi < 75.0:
        return "DITOLAK (Kehadiran di bawah 75%)"
    elif nilai_akhir >= 75.0 and nilai_akhir >= 75.0:
        return "DITERIMA (Memenuhi Syarat)"
    else:
        return "DITOLAK (Nilai Akhir Kurang)"
