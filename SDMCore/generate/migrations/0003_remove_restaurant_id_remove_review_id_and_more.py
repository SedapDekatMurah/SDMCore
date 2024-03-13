# Generated by Django 5.0.1 on 2024-03-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate', '0002_remove_restaurant_name_remove_review_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='keyword_1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='keyword_2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='keyword_3',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='keyword_4',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='keyword_5',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='loc_latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='loc_longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='maps_url',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu_1_item',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu_1_price',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu_2_item',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu_2_price',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu_3_item',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu_3_price',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='place_id',
            field=models.TextField(default='', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='review',
            name='url',
            field=models.TextField(default='', primary_key=True, serialize=False),
        ),
    ]
