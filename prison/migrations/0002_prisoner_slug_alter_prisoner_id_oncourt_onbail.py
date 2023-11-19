# Generated by Django 4.2.7 on 2023-11-19 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prison', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prisoner',
            name='slug',
            field=models.SlugField(default=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Oncourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('court_name', models.CharField(max_length=50)),
                ('date_of_attending', models.DateField()),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prison.prisoner', verbose_name='Prisoner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Onbail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prison.oncourt', verbose_name='Court')),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prison.prisoner', verbose_name='Prisoner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
