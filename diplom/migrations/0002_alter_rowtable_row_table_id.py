# Generated by Django 4.0.4 on 2022-06-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rowtable',
            name='row_table_id',
            field=models.AutoField(db_column='id_строки', primary_key=True, serialize=False, verbose_name='id_строки'),
        ),
    ]
