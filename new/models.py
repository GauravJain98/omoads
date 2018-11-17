from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User
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
def email(msg):
    user = User.objects.all()
    emails = []
    for i in user:
        emails.append(i.email)
    return send_mail("EMAIL FOR APP", msg, "test@project.com", emails)

class Banner(models.Model):
    start_date =models.DateField(auto_now=False, auto_now_add=False)
    end_date =models.DateField(auto_now=False, auto_now_add=False)
    _end_date_old =None
    price = models.IntegerField(default = 0)
    installation_date = models.DateField(auto_now=False, auto_now_add=False)
    removal_date = models.DateField(auto_now=False, auto_now_add=False)
    _installation_date_old = None
    _removal_date_old = None
    def __init__(self, *args, **kwargs):
        super(Banner, self).__init__(*args, **kwargs)
    def save(self, *args, **kwargs):
        if(self._end_date_old != self.end_date and self._end_date_old):
            self._end_date_old = self.end_date
            email("end date of banner id:"+str(self.id)+" ")
        if(self._installation_date_old != self.installation_date and self._installation_date_old):
            self._installation_date_old = self.installation_date
            email("installation date of banner id:"+str(self.id)+" ")
        if(self._removal_date_old != self.removal_date and self._removal_date_old):
            self._removal_date_old = self.removal_date
            email("removal date of banner id:"+str(self.id)+" ")
        super(Banner, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)

class Installation(models.Model):
    receiving_date =models.DateField(auto_now=False, auto_now_add=False)
    _receiving_date =None
    price = models.IntegerField()
    banner = models.ForeignKey("new.Banner",  on_delete=models.CASCADE)
    update = models.BooleanField()
    def save(self, *args, **kwargs):
        if(self._receiving_date_old != self.receiving_date):
            self._receiving_date_old = self.receiving_date
            email("receiving date of installation id:"+(self.id)+" and banner id:"+str(self.banner.id))
        super(Installation, self).save(*args, **kwargs) # Call the real save() method