from django.db import models

class Item(models.Model):
    item_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name