# Generated by Django 2.1.3 on 2018-11-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20181111_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('paid', 'paid'), ('delivered', 'delivered'), ('reverted', 'reverted'), ('failed', 'failed')], default='created', max_length=20),
        ),
    ]
