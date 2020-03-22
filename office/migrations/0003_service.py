# Generated by Django 2.2.5 on 2020-03-18 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_auto_20200318_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_service', to='office.Office')),
            ],
        ),
    ]