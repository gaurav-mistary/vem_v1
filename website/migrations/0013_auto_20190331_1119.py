# Generated by Django 2.1.7 on 2019-03-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20190331_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='m_shot_weight',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
    ]