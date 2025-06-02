from django.db import models

class Item(models.Model):
    id_item = models.IntegerField()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

class ItemDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    image = models.CharField(max_length=64)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    contents = models.TextField()
    inventory = models.TextField()

    def __str__(self):
        return self.name
