# Generated by Django 5.1.2 on 2024-10-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_comments_options_messsages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=None, upload_to='images/')),
                ('created_at', models.TimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_at'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='messsages',
            options={'verbose_name': 'Messsage', 'verbose_name_plural': 'Messsages'},
        ),
    ]
