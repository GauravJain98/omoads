from django.db import models

# Create your models here.
'''
Banner is a product that is having following fields:
 -Booking Start Date 
 -Booking End Date*** 
 -Total Price 
 -No. of Installments - Eg. 2 *** 
 -Installment #1 
    - Installment Price 
    - Recieving Date*** 
-Installment #2 -
  Installment price 
  - Receiving Date*** 
-Banner Installation Date*** 
-Banner Removal Date *** 

'''

class Banner(models.Model):
    start_date =models.DateField(auto_now=False, auto_now_add=False)
    end_date =models.DateField(auto_now=False, auto_now_add=False)
    _end_date_old =None
    price = models.IntegerField(default = 0)
    installation_date = models.DateField(auto_now=False, auto_now_add=False)
    removal_date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.id 

    def __unicode__(self):
        return self.id

class Installation(models.Model):
    receiving_date =models.DateField(auto_now=False, auto_now_add=False)
    price = models.IntegerField()
    banner = models.ForeignKey("new.Banner",  on_delete=models.CASCADE)
    update = models.BooleanField()
    def save(self, *args, **kwargs):
        if self.update:
           self.banner.price = self.banner.price + price
        super(Installation, self).save(*args, **kwargs) # Call the real save() method