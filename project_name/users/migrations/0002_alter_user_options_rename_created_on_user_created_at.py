# Generated by Django 4.1.2 on 2022-11-01 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-created_at'], 'verbose_name': '사용자', 'verbose_name_plural': '사용자 그룹'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='created_on',
            new_name='created_at',
        ),
    ]
