# Generated by Django 2.2.12 on 2020-06-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200606_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Oczekujące'), ('Out for delivery', 'Wysłane'), ('Delivered', 'Dostarczone')], max_length=200, null=True),
        ),
    ]