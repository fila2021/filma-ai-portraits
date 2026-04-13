from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_seed_service_packages'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepackage',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
