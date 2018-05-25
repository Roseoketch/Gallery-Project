from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbor(models.Model):
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30, null =True)
    occupants_count = models.PositiveIntegerField(default=0)
    admin_foreign_key = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    health_number = models.CharField(max_length=13)
    police_number = models.CharField(max_length=13)


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
    def find_business(cls):
        biz = Business.objects.all()
        return biz

    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def update_business(cls,id,name):
        updated = Business.objects.filter(id=business.id).update(name=name)

class MyUser(models.Model):
    name = models.CharField(max_length=60)
    id_no = models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to ='upload/',blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    jirani = models.ForeignKey(Neighbor,on_delete=models.CASCADE)
    business = models.ForeignKey(Business,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    @classmethod
    def get_user(cls):
        users = MyUser.objects.all()
        return users

class Post(models.Model):
    post = models.TextField()
    editor = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    post_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post

    class Meta:
        ordering=['-post_date']

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_post(cls):
        post = Post.objects.all()
        return post
