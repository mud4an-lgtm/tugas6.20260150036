def hitung_persentase_presensi(hadir,total_pertemuan=14):
    presentase =hadir / total_pertemuan *100
    #rata_rata =total / 2
    return presentase
def hitung_nilai_akhir(tugas,ucp1,ucp2):
    nilai = tugas(20/100)+ ucp1(40/100)+ ucp2(40/100)
    #rata_rata = total / 3
    return nilai

def cek_kelayakan_aslab(persentase_presensi,nilai_akhir):
    if persentase_presensi <75:
        return "DITOLAK(kehadiran dibawah 75%)" 
    elif persentase_presensi >= 75 and nilai_akhir >= 75:
        return "DITERIMA(memenuhi syarat)"
    elif persentase_presensi >= 75 and nilai_akhir <75:
        return "ditolak(nilai akhir kurang)"
    else:
        return "DITOLAK(nilai akhir kurang)"
    
    

      
