# Generated by Django 3.1.7 on 2021-02-26 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pendaftaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pendaftaran', models.DateField()),
                ('no_pelayanan', models.CharField(blank=True, default=0, max_length=11, null=True, unique=True)),
                ('nama', models.CharField(max_length=100)),
                ('mutasi', models.CharField(max_length=255)),
                ('jumlah', models.IntegerField()),
                ('keterangan', models.CharField(choices=[('PROSES', 'PROSES'), ('SELESAI', 'SELESAI')], max_length=20)),
                ('tanggal_selesai', models.DateField()),
                ('desa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.desa')),
                ('kecamatan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.kecamatan')),
            ],
        ),
        migrations.CreateModel(
            name='SPPTLama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_sppt_lama', models.CharField(blank=True, max_length=18, null=True)),
                ('nama_wp_lama', models.CharField(max_length=100)),
                ('tarif_lama', models.DecimalField(blank=True, decimal_places=4, max_digits=19)),
                ('no_pelayanan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.pendaftaran')),
            ],
        ),
        migrations.CreateModel(
            name='SPPTBaru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_sppt_baru', models.CharField(blank=True, max_length=18, null=True)),
                ('nama_wp_baru', models.CharField(max_length=100)),
                ('tarif_baru', models.DecimalField(blank=True, decimal_places=4, max_digits=19)),
                ('keterangan', models.CharField(blank=True, choices=[('TETAP', 'TETAP'), ('BARU', 'BARU'), ('NAIK', 'NAIK'), ('TURUN', 'TURUN')], max_length=20)),
                ('transaksi', models.CharField(blank=True, max_length=20)),
                ('luas_tanah', models.IntegerField(blank=True, null=True)),
                ('luas_bangunan', models.IntegerField(blank=True, null=True)),
                ('sppt_lama', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.spptlama')),
            ],
        ),
        migrations.AddField(
            model_name='desa',
            name='kecamatan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.kecamatan'),
        ),
    ]
