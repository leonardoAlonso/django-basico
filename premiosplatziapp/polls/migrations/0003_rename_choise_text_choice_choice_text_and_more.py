# Generated by Django 4.0.1 on 2022-02-07 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choices_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choise_text',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='questio',
            new_name='question',
        ),
    ]
