from django.db import models
import jdatetime
from django_jalali.db import models as jalalimodels
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class Seller(AbstractUser):
    birthdate = jalalimodels.jDateField(null=True)
    national_code = models.CharField(max_length=10, null=True)


    @property
    def age(self):
        current_date = jdatetime.date.today().year
        age = current_date - self.birthdate.year
        return age
    
    @property
    def is_birthday(self):
        today = jdatetime.date.today()
        day_validation = self.birthdate.day == today.day
        month_validation = self.birthdate.month == today.month
        return day_validation and month_validation

    def save(self, *args, **kwargs):
        if not self.is_superuser:
            if self.pk is None or not self.password.startswith('pbkdf2_'):
                if self.password:
                    try:
                        validate_password(self.password, self)
                    except ValidationError as e:
                        raise e
                    self.set_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.username}'

class Product(models.Model):
    weight = models.FloatField()
    price = models.FloatField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return f'orange by {self.seller.username}'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    count = models.PositiveIntegerField()
    due_date = jalalimodels.jDateTimeField()
    created_at = jalalimodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return f'order {self.id}'
