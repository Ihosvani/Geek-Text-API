# Generated by Django 4.0.5 on 2022-06-28 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_comments_commentdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratings',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='ISBN',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.books'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='ISBN',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.books'),
        ),
    ]
