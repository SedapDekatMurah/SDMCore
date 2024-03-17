from django.db import models
# import generation_scripts


class Restaurant(models.Model):
    name = models.TextField(default="")
    place_id = models.TextField(primary_key=True, default="")
    address = models.TextField(default="")
    loc_latitude = models.FloatField(default=0)
    loc_longitude = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    maps_url = models.TextField(default="")
    menu_1_item = models.TextField(default="")
    menu_1_price = models.TextField(default="")
    menu_2_item = models.TextField(default="")
    menu_2_price = models.TextField(default="")
    menu_3_item = models.TextField(default="")
    menu_3_price = models.TextField(default="")
    keyword_1 = models.TextField(default="")
    keyword_2 = models.TextField(default="")
    keyword_3 = models.TextField(default="")
    keyword_4 = models.TextField(default="")
    keyword_5 = models.TextField(default="")
    # Fields here


class Review(models.Model):
    place_id = models.TextField(default="")
    url = models.TextField(primary_key=True, default="")
    review = models.TextField(default="")
    # Fields here
