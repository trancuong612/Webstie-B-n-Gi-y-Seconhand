from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# thay doi from
class TaiKhoan(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
class DanhMuc(models.Model):
    sub_category = models.ForeignKey('self', on_delete = models.CASCADE, related_name = 'ten_dm', null = True, blank = True)
    is_sub = models.BooleanField(default = False)
    name = models.CharField(max_length = 200, null = True)
    vt = models.CharField(max_length = 200, null = True)
    slug = models.SlugField(max_length = 200, unique = True)
    def __str__(self):
        return self.name

class SanPham(models.Model):
    category = models.ManyToManyField(DanhMuc, related_name='sanpham')
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField()
    Describe = models.CharField(max_length = 200, null = True)
    Type = models.CharField(max_length = 200, null = True)
    image = models.ImageField(null = True, blank = True)
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class GioHang(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = False)
    data_oder = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 200, null = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_items(self):
        donhangs = self.donhang_set.all()
        total = sum([item.quantity for item in donhangs])
        return total
    @property
    def get_cart_total(self):
        donhangs = self.donhang_set.all()
        total = sum([item.get_total for item in donhangs])
        return total
    
class DonHang(models.Model):
    product = models.ForeignKey(SanPham, on_delete = models.SET_NULL, null = True, blank = False)
    order = models.ForeignKey(GioHang, on_delete = models.SET_NULL, null = True, blank = False)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ChiTietDongHang(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = False)
    order = models.ForeignKey(GioHang, on_delete = models.SET_NULL, null = True, blank = False)
    address = models.CharField(max_length = 200, null = True)
    city = models.CharField(max_length = 200, null = True)
    state = models.CharField(max_length = 200, null = True)
    mobile = models.CharField(max_length = 11, null = True)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.address