from django.db import models


class Movie(models.Model):
    """
        Represent a move
    """

    name = models.CharField(max_length=254, verbose_name='نام فیلم')
    director = models.CharField(max_length=64, verbose_name='کارگردان')
    year = models.PositiveIntegerField(verbose_name='تاریخ انتشار')
    length = models.PositiveIntegerField(verbose_name='زمان فیلم')
    country = models.CharField(max_length=64, verbose_name='کشور سازنده')
    language = models.CharField(max_length=32, verbose_name='زبان فیلم')
    description = models.TextField(verbose_name='توضیحات', blank=True)
    cover = models.ImageField(verbose_name='تصویر فیلم', upload_to='movie/covers/')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
        Represent a Cinema saloon
    """

    cinema_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254, verbose_name='نام سینما')
    city = models.CharField(max_length=254, verbose_name='شهر')
    capacity = models.IntegerField(verbose_name='گنچایش سینما')
    phone = models.CharField(max_length=12, verbose_name='شماره تلفن', blank=True)
    address = models.TextField(verbose_name='آدرس')

    def __str__(self):
        return self.name
