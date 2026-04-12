from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicepackage',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='servicepackage',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='servicepackage',
            name='platform_type',
            field=models.CharField(choices=[('instagram', 'Instagram'), ('facebook', 'Facebook'), ('tiktok', 'TikTok'), ('youtube', 'YouTube'), ('other', 'Other')], default='other', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicepackage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicepackage',
            name='base_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='servicepackage',
            name='number_of_images',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='servicepackage',
            name='turnaround_days',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='customrequest',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests', to='services.servicepackage'),
        ),
        migrations.AlterField(
            model_name='customrequest',
            name='platform_type',
            field=models.CharField(choices=[('instagram', 'Instagram'), ('facebook', 'Facebook'), ('tiktok', 'TikTok'), ('youtube', 'YouTube'), ('other', 'Other')], default='other', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customrequest',
            name='style_choice',
            field=models.CharField(choices=[('realistic', 'Realistic'), ('cartoon', 'Cartoon'), ('cinematic', 'Cinematic'), ('studio', 'Studio'), ('other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customrequest',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='customrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_requests', to='auth.user'),
        ),
    ]
