# Generated by Django 5.1.3 on 2024-11-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KegiatanMahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npm_mahasiswa', models.CharField(max_length=20)),
                ('bank_id', models.CharField(max_length=200)),
                ('nama_kegiatan', models.TextField()),
                ('tingkat_kegiatan', models.CharField(max_length=255)),
                ('tanggal_kegiatan', models.CharField(max_length=255)),
                ('kategori', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='KRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npm_mahasiswa', models.CharField(max_length=20)),
                ('jenis_semester', models.CharField(max_length=255)),
                ('tahun_semester', models.CharField(max_length=10)),
                ('kode_kelas', models.CharField(max_length=20)),
                ('kode_matkul', models.CharField(max_length=200)),
                ('nama_matkul', models.CharField(max_length=200)),
                ('sks_matakuliah', models.IntegerField()),
                ('total_hadir', models.IntegerField()),
                ('total_pertemuan', models.IntegerField()),
                ('total_terlaksana', models.IntegerField()),
                ('total_tidak_hadir', models.IntegerField()),
                ('kode_nilai', models.CharField(max_length=10)),
                ('kategori_matakuliah', models.CharField(max_length=255)),
                ('persentase_kehadiran', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npm_mahasiswa', models.CharField(max_length=20)),
                ('nama_mahasiswa', models.CharField(max_length=255)),
                ('prodi_mahasiswa', models.CharField(max_length=255)),
                ('angkatan_mahasiswa', models.CharField(max_length=10)),
                ('ipk_mahasiswa', models.FloatField()),
                ('status_mahasiswa', models.CharField(max_length=200)),
                ('pembimbing_tugas_akhir', models.CharField(max_length=255)),
            ],
        ),
    ]
