# Generated by Django 4.0.6 on 2022-10-14 11:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ebookapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxLengthValidator(5)])),
            ],
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='books',
            name='review',
        ),
        migrations.AddField(
            model_name='books',
            name='genre',
            field=models.CharField(choices=[('fantasy', 'fantasy'), ('literary', 'literary'), ('mystery', 'mystery'), ('non-fiction', 'non-fiction'), ('science-fiction', 'science-fiction'), ('thriller', 'thriller')], default='', max_length=200),
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebookapi.books'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
