from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    npm_mahasiswa = models.CharField(max_length=20)
    nama_mahasiswa = models.CharField(max_length=255)
    prodi_mahasiswa = models.CharField(max_length=255)
    angkatan_mahasiswa = models.CharField(max_length=10)
    ipk_mahasiswa = models.FloatField()
    status_mahasiswa = models.CharField(max_length=200)
    pembimbing_tugas_akhir = models.CharField(max_length=255)


class KRS(models.Model):
    npm_mahasiswa = models.CharField(max_length=20)
    jenis_semester = models.CharField(max_length=255)
    tahun_semester = models.CharField(max_length=10)
    kode_kelas = models.CharField(max_length=20)
    kode_matkul = models.CharField(max_length=200)
    nama_matkul = models.CharField(max_length=200)
    sks_matakuliah = models.IntegerField()
    total_hadir = models.IntegerField()
    total_pertemuan = models.IntegerField()
    total_terlaksana = models.IntegerField()
    total_tidak_hadir = models.IntegerField()
    kode_nilai = models.CharField(max_length=10)
    kategori_matakuliah = models.CharField(max_length=255)
    persentase_kehadiran = models.FloatField()


class KegiatanMahasiswa(models.Model):
    npm_mahasiswa = models.CharField(max_length=20)
    bank_id = models.CharField(max_length=200)
    nama_kegiatan = models.TextField()
    tingkat_kegiatan = models.CharField(max_length=255)
    tanggal_kegiatan = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
