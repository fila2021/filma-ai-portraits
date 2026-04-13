from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PromptBundle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('count', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('description', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['count'],
            },
        ),
        migrations.CreateModel(
            name='PromptSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
    ]
