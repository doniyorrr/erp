import random
from django.db.models.signals import post_save
from django.db import models

from users.models  import CustomUser
from market.models import Market, Supplier


def random_number():
    return random.randint(10000, 99999)


UNITS = (
    ('kg', 'kg'),
    ('litr', 'litr'),
    ('dona', 'dona'),
)    

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sub Kategoriyalar"


class Product(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bar_code = models.CharField(max_length=128, unique=True)
    plu_code = models.PositiveIntegerField(default=random_number, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=10, default='dona', choices=UNITS)
    received_date = models.DateField(null=True, blank=True)
    date_of_manufacture = models.DateField(null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(default=0)
    expiry_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


    @property
    def get_remaining_quantity(self):
        if self.returnedproduct.is_returned:
            t = self.quantity - self.returnedproduct.quantity
            t.update()
        return t

    @property
    def is_discount(self):
        return self.discount != 0

    @property
    def get_real_price(self):
        return self.price - (self.price * self.discount) // 100


    class Meta:
        verbose_name_plural = "Produktlar"


class MoveProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='from_market')
    to_market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='to_market')
    quantity = models.IntegerField(default=0)
    sent_date = models.DateField(verbose_name="Jonatilgan sana")
    is_received = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def get_single_product_price(self):
        return self.quantity * self.product.price

    
    @property
    def get_total_products(self):
        return self.quantity
        


    class Meta:
        verbose_name_plural = "Tovarlarni Ko'chirish"


class ReturnedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_market = models.ForeignKey(Market, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    sent_date = models.DateField(verbose_name="Yuborilgan sana")
    is_returned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        return self.quantity * self.product.price


    class Meta:
        verbose_name_plural = "Qaytgan Produktlar"


class TrashProduct(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    thrown_date = models.DateField("Musirga Chiqarib yuborilgan sana")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_product_price(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name_plural = "Chiqarib Yuborilgan Produktlar"





def post_returned_product_created_signal(sender, instance, created, **kwargs):
    if created:
        if instance.is_returned == True:
            instance.product.quantity -= instance.quantity
            instance.product.save()


post_save.connect(post_returned_product_created_signal, sender=ReturnedProduct)


def post_move_product_created_signal(sender, instance, created, **kwargs):
    if created:
        if instance.is_received == True:
            instance.product.quantity -= instance.quantity
            instance.save()


post_save.connect(post_move_product_created_signal, sender=MoveProduct)







































