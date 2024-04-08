# Generated by Django 4.2.8 on 2024-04-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_tag_created_at_alter_tag_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, help_text='Stock Keeping Unit (SKU) will be generated automatically', max_length=255, null=True),
        ),
    ]