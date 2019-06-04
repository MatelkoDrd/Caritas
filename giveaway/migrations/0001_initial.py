# Generated by Django 2.2.1 on 2019-06-04 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0002_auto_20190527_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('type', models.IntegerField(choices=[(1, 'Adult'), (2, 'Kid')])),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Adult'), (2, 'Kid')])),
                ('size', models.IntegerField(choices=[(1, 'S'), (2, 'M'), (3, 'L')])),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Adult'), (2, 'Kid')])),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Giveaway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bags', models.IntegerField()),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.Book')),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.Clothes')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.Location')),
                ('organizations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization')),
                ('others', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.Other')),
                ('toy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.Toy')),
            ],
        ),
    ]
