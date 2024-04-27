from django.db import models

# Create your models here.

class client(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null = False)
    email = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(null= False)
    def __str__(self) -> str:
        return self.name

class product(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=100, null=False)
    abbreviation = models.CharField(max_length=3, null=False)
    description = models.CharField(max_length=100, null=False)

    def _str_(self):
        return self.name
    
class ClientProduct(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    account_number = models.IntegerField(null=False)

    def _str_(self):
        return f"{self.client.name} - {self.product.name}"
    
class transaction_type  (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    abbreviation = models.CharField(max_length=3, null=False)
    description = models.CharField(max_length=100, null=False)

    def _str_(self):
        return self.name