from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbor(models.Model):
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30, null =True)
    occupants_count = models.PositiveIntegerField(default=0)
    admin_foreign_key = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.name

    def save_neighbor(self):
        self.save()

    def delete_neighbor(self):
        self.delete()

    @classmethod
    def get_neighbor(cls):
        neighbor= Neighbor.objects.all()
        return neighbor

    @classmethod
    def find_neighbor(cls,pk):
        neighbor=Neighbor.objects.filter(pk=Neighbor.pk)
        return neighbor

    @classmethod
    def update_neighbor(cls,id,name):
        updated = Neighbor.objects.filter(id=Neighbor.id).update(name=name)
        return updated

    @classmethod
    def update_occupants(cls,id,occupants_count):
        occupied = Neighbor.objects.filter(id=Neighbor.id).update(occupants_count=occupants_count)
        return occupied

class Business(models.Model):
    name = models.CharField(max_length=60)
    business_email = models.EmailField(max_length=60)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    jirani = models.ForeignKey(Neighbor,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def get_business(cls):
        biz = Business.objects.all()
        return biz

    @classmethod
    def find_business(cls,search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def update_business(cls,id,name):
        updated = Business.objects.filter(id=business.id).update(name=name)
