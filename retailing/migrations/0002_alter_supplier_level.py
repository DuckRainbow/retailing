# Generated by Django 4.2.2 on 2025-01-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='level',
            field=models.CharField(choices=[(2, 'индивидуальный предприниматель'), (0, 'завод'), (1, 'розничная сеть')]),
        ),
    ]
