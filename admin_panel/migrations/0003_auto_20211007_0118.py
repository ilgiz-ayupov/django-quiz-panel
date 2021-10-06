# Generated by Django 3.2.8 on 2021-10-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_questions_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='status',
            field=models.CharField(choices=[('Авторизовался', 'Авторизовался'), ('Проходит викторину', 'Проходит викторину'), ('Закончил викторину', 'Закончил викторину')], default='Авторизовался', max_length=255),
        ),
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question_photos/', verbose_name='Картинка'),
        ),
    ]