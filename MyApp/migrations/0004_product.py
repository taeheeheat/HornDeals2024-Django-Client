# Generated by Django 4.2.16 on 2025-01-25 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('location', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, choices=[('clothing', 'Clothing'), ('accessories', 'Accessories'), ('tickets', 'Tickets'), ('studyMaterials', 'Study Materials'), ('miscellaneous', 'Miscellaneous')], max_length=50)),
            ],
        ),
    ]
