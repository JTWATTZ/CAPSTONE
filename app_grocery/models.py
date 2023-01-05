from django.db import models
 

class Blog(models.Model):
        dish_name = models.CharField(max_length = 30)
        text = models.TextField(max_length = 5000)
        pub_date = models.DateField()

        def __str__(self):
            return self.dish_name

# Create your models here.
