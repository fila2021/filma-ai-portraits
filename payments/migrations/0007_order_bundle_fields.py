from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bundle_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='bundle_label',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.PROTECT, related_name='orders', to='shop.product'),
        ),
    ]
