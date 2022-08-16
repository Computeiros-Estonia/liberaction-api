# Generated by Django 4.0 on 2022-08-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_birth_date_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(null=True, verbose_name='date de nascimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, null=True, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('o', 'Outro')], max_length=1, null=True, verbose_name='Unidade de Medida'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, null=True, verbose_name='sobrenome'),
        ),
    ]