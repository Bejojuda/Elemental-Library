# Generated by Django 3.1.1 on 2020-09-03 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField(auto_created=True)),
                ('return_date', models.DateField()),
                ('person_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('book_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookunit')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]