from django.db import migrations


def seed_packages(apps, schema_editor):
    ServicePackage = apps.get_model('services', 'ServicePackage')
    if ServicePackage.objects.exists():
        return

    packages = [
        {
            'name': 'Starter Social Set',
            'description': '10 portrait variants tailored for Instagram and TikTok profiles.',
            'base_price': 39.00,
            'number_of_images': 10,
            'turnaround_days': 2,
            'platform_type': 'instagram',
        },
        {
            'name': 'Creator Growth Pack',
            'description': '25 images covering banners, reels covers, and profile shots for FB/IG.',
            'base_price': 79.00,
            'number_of_images': 25,
            'turnaround_days': 3,
            'platform_type': 'facebook',
        },
        {
            'name': 'YouTube Pro Bundle',
            'description': '15 thumbnails and hero images tuned for YouTube branding.',
            'base_price': 99.00,
            'number_of_images': 15,
            'turnaround_days': 4,
            'platform_type': 'youtube',
        },
    ]

    ServicePackage.objects.bulk_create(ServicePackage(**data) for data in packages)


def unseed_packages(apps, schema_editor):
    ServicePackage = apps.get_model('services', 'ServicePackage')
    names = [
        'Starter Social Set',
        'Creator Growth Pack',
        'YouTube Pro Bundle',
    ]
    ServicePackage.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_servicepackage_updates'),
    ]

    operations = [
        migrations.RunPython(seed_packages, unseed_packages),
    ]
