from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class TimeStampModel(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract=True



class Category(TimeStampModel):
    name= models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class Supplier(TimeStampModel):
    name= models.CharField(max_length=50,unique=True)
    email= models.EmailField(unique=True)
    phone= models.CharField(max_length=25,null=True,blank=True)
    company=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    product=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name

class Purchase(TimeStampModel):
    name= models.CharField(max_length=50,unique=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier,null=True,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    quantity=models.CharField(max_length=5)
    expiry_date=models.DateField()
    image= models.ImageField(upload_to='purchases/', null=True, blank=True)


class Notification(TimeStampModel):
    type = models.CharField(max_length=255)
    notifiable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    notifiable_id = models.PositiveIntegerField()
    notifiable = GenericForeignKey('notifiable_type', 'notifiable_id')
    data = models.TextField()
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.type

class Product(TimeStampModel):
    purchase= models.ForeignKey(Purchase,null=True,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    discount=models.DecimalField(default=0,max_digits=15,decimal_places=2)
    description=models.TextField()

    def __str__(self):
        return str(self.id)

class Sale(TimeStampModel):
     
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()
    total_price=models.FloatField(null=True, blank=True, )
