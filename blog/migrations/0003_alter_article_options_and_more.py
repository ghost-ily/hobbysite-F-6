# Generated by Django 5.1.7 on 2025-03-08 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_articlecategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Created_on',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Updated_on',
            new_name='updated_on',
        ),
    ]
