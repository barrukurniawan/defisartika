# Generated by Django 2.1.3 on 2019-03-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('api_token', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('create_user', models.IntegerField(blank=True, null=True)),
                ('update_user', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('code_pos', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('no_identification', models.CharField(blank=True, max_length=100, null=True)),
                ('dashboard_id', models.CharField(blank=True, max_length=50, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.CharField(default='false', max_length=5, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='TabelKelembaban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('api_key', models.CharField(max_length=8)),
                ('nilai_kelembaban', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'tabel_kelembaban',
                'db_table': 'tabel_kelembaban',
            },
        ),
        migrations.CreateModel(
            name='TabelSuhu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('api_key', models.CharField(max_length=8)),
                ('nilai_suhu', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'tabel_suhu',
                'db_table': 'tabel_suhu',
            },
        ),
        migrations.CreateModel(
            name='TabelTekananUdara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('api_key', models.CharField(max_length=8)),
                ('nilai_tekananudara', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'tabel_tekananudara',
                'db_table': 'tabel_tekananudara',
            },
        ),
    ]
