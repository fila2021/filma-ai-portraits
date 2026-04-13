from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_noop_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
