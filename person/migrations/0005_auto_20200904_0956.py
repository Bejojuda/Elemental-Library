# Generated by Django 3.1.1 on 2020-09-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20200904_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=45),
        ),
    ]