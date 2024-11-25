import pandas as pd 
from django.core.management.base import BaseCommand
from dataset.models import KegiatanMahasiswa , KRS , Mahasiswa
import os 
from django.conf import settings

class Command(BaseCommand):
    help='Import Dataset from csv file'
    def handle(self , *args , **kwargs):

        data_dir = os.path.join(settings.BASE_DIR , 'data')

        krs_file_path = os.path.join(data_dir , 'krs.csv')

        kegiatan_file_path = os.path.join(data_dir , 'kegiatan_mahasiswa.csv')

        mahasiswa_file_path = os.path.join(data_dir , 'mahasiswa.csv')

        try: 
            dfKRS = pd.read_csv(krs_file_path)
            dfKegiatan = pd.read_csv(kegiatan_file_path)
            dfMahasiswa = pd.read_csv(mahasiswa_file_path)

            dfKRS['npm_mahasiswa'] = dfKRS['npm_mahasiswa'].fillna(value='Unknown')
            dfKRS['jenis_semester'] = dfKRS['jenis_semester'].fillna(value='Unknown')
            dfKRS['tahun_semester'] = dfKRS['tahun_semester'].fillna(value='Unknown')
            dfKRS['kode_kelas'] = dfKRS['kode_kelas'].fillna(value='Unknown')
            dfKRS['nama_matkul'] = dfKRS['nama_matkul'].fillna(value='Unknown')
            dfKRS['sks_matakuliah'] = dfKRS['sks_matakuliah'].fillna(value='0')
            dfKRS['total_hadir'] = dfKRS['total_hadir'].fillna(value='0')
            dfKRS['total_pertemuan'] = dfKRS['total_pertemuan'].fillna(value='0')
            dfKRS['total_terlaksana'] = dfKRS['total_terlaksana'].fillna(value='0')
            dfKRS['total_tidak_hadir'] = dfKRS['total_tidak_hadir'].fillna(value='0')
            dfKRS['kode_nilai'] = dfKRS['kode_nilai'].fillna(value='Unknown')
            dfKRS['kategori_matakuliah'] = dfKRS['kategori_matakuliah'].fillna(value='Unknown')
            dfKRS['persentase_kehadiran'] = dfKRS['persentase_kehadiran'].fillna(value='0')

            dfMahasiswa['npm_mahasiswa'] = dfMahasiswa['npm_mahasiswa'].fillna(value="Unknown")
            dfMahasiswa['nama_mahasiswa'] = dfMahasiswa['nama_mahasiswa'].fillna(value="Unknown")
            dfMahasiswa['prodi_mahasiswa'] = dfMahasiswa['prodi_mahasiswa'].fillna(value="Unknown")
            dfMahasiswa['angkatan_mahasiswa'] = dfMahasiswa['angkatan_mahasiswa'].fillna(value="Unknown")
            dfMahasiswa['ipk_mahasiswa'] = dfMahasiswa['ipk_mahasiswa'].fillna(value="0")
            dfMahasiswa['status_mahasiswa'] = dfMahasiswa['status_mahasiswa'].fillna(value="Unknown")
            dfMahasiswa['pembimbing_tugas_akhir'] = dfMahasiswa['pembimbing_tugas_akhir'].fillna(value="Unknown")

            dfKegiatan['npm_mahasiswa'] = dfKegiatan['npm_mahasiswa'].fillna(value='Unknown')
            dfKegiatan['bank_id'] = dfKegiatan['bank_id'].fillna(value='Unknown')
            dfKegiatan['nama_kegiatan'] = dfKegiatan['nama_kegiatan'].fillna(value='Unknown')
            dfKegiatan['tingkat_kegiatan'] = dfKegiatan['tingkat_kegiatan'].fillna(value='Unknown')
            dfKegiatan['tanggal_kegiatan'] = dfKegiatan['tanggal_kegiatan'].fillna(value='Unknown')
            dfKegiatan['kategori'] = dfKegiatan['kategori'].fillna(value='Unknown')
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('CSV File not Found'))
            return 

        for _,row in dfKRS.iterrows():
            KRS.objects.create(
                npm_mahasiswa= row['npm_mahasiswa'],
                jenis_semester= row['jenis_semester'],
                tahun_semester= row['tahun_semester'],
                kode_kelas= row['kode_kelas'],
                kode_matkul= row['kode_matkul'],
                nama_matkul= row['nama_matkul'],
                sks_matakuliah= row['sks_matakuliah'],
                total_hadir= row['total_hadir'],
                total_pertemuan= row['total_pertemuan'],
                total_terlaksana= row['total_terlaksana'],
                total_tidak_hadir= row['total_tidak_hadir'],
                kode_nilai= row['kode_nilai'],
                kategori_matakuliah= row['kategori_matakuliah'],
                persentase_kehadiran= row['persentase_kehadiran']
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported KRS'))

        for _,row in dfMahasiswa.iterrows():
            Mahasiswa.objects.create(
                npm_mahasiswa= row['npm_mahasiswa'],
                nama_mahasiswa= row['nama_mahasiswa'],
                prodi_mahasiswa= row['prodi_mahasiswa'],
                angkatan_mahasiswa= row['angkatan_mahasiswa'],
                ipk_mahasiswa= row['ipk_mahasiswa'],
                status_mahasiswa= row['status_mahasiswa'],
                pembimbing_tugas_akhir= row['pembimbing_tugas_akhir'],
                
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported Mahasiswa'))

        for _,row in dfKegiatan.iterrows():
            KegiatanMahasiswa.objects.create(
                npm_mahasiswa= row['npm_mahasiswa'],
                bank_id= row['bank_id'],
                nama_kegiatan= row['nama_kegiatan'],
                tingkat_kegiatan= row['tingkat_kegiatan'],
                tanggal_kegiatan= row['tanggal_kegiatan'],
                kategori= row['kategori'],
                
                
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported Kegiatan Mahasiswa'))
