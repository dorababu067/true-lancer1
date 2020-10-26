# Generated by Django 3.1.2 on 2020-10-26 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('groupid', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('ipaddress', models.GenericIPAddressField()),
                ('registerdate', models.DateField(auto_now_add=True)),
                ('last_login_date', models.DateField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoginDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='some type', max_length=255)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True)),
                ('useragent', models.CharField(max_length=1000)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
