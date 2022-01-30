# Generated by Django 3.2.2 on 2022-01-30 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(default='Enter product name', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default='0.0', max_digits=5)),
                ('description', models.TextField(default='Enter product description')),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
