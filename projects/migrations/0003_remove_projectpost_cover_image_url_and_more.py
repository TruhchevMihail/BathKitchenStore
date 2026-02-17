

import core.validators.validate_file_size_15mb
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectpost_delete_projestpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpost',
            name='cover_image_url',
        ),
        migrations.AddField(
            model_name='projectpost',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/', validators=[core.validators.validate_file_size_15mb.validate_file_size_15mb, django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])]),
        ),
    ]