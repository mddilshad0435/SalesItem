
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
MEASURMENT_TYPE = (
    ('N','Nos'),
    ('M','Meter'),
    ('KG','Kilo Gram'),
    ('KM','Kilo Meter')
)
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

class Item(models.Model):
    Item_Code = models.IntegerField()
    Item_name = models.CharField(max_length=150)
    Item_Measurement = models.CharField(choices=MEASURMENT_TYPE,max_length=2)
    Item_stock = models.IntegerField()
    Item_Image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    Supplier_name = models.CharField(max_length=150)
    Requisition_By = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Create_date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Item_name)

