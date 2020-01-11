from django.db import models

class List(models.Model):
    item = models.CharField(max_length = 200)
    added_date = models.DateTimeField(auto_now_add = True)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.item + ' Add on ' +  str(self.added_date)
