# Generated by Django 2.2.28 on 2022-04-26 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editpwd',
            fields=[
                ('eid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('captcha', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'editpwd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('uemail', models.CharField(blank=True, max_length=20, null=True)),
                ('usex', models.CharField(blank=True, max_length=20, null=True)),
                ('uname', models.CharField(blank=True, max_length=20, null=True)),
                ('upsw', models.CharField(blank=True, max_length=100, null=True)),
                ('uphone', models.CharField(blank=True, max_length=20, null=True)),
                ('uadmin', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.User')),
                ('province', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('district', models.CharField(blank=True, max_length=30, null=True)),
                ('detail', models.CharField(blank=True, max_length=128, null=True)),
                ('get_name', models.CharField(blank=True, max_length=128, null=True)),
                ('get_phone', models.CharField(blank=True, max_length=128, null=True)),
                ('get_code', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
    ]