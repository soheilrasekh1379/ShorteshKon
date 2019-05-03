from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
import string
# Create your models here.


class shortUrl(models.Model):
    url             = models.CharField(max_length=300)
    num_of_visits   = models.IntegerField(default=0)



class realUrl(models.Model):
    url         = models.CharField(max_length=300,null=False,blank=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    shorturl     = models.ForeignKey(shortUrl,on_delete=models.CASCADE,null=True,blank=True)


def random_gen(size=6):
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(size))



@receiver(pre_save,sender=realUrl)
def create_short(sender,instance,**kwargs):
        sh = shortUrl(url=random_gen())
        sh.save()
        instance.shorturl = sh


