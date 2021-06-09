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


class ShowTime(models.Model):
    """
        Represents a movie in a cinema at a specific time
    """

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='showtimes')
    
    start_time = models.DateTimeField(verbose_name='تاریخ اکران')
    end_time = models.DateTimeField(verbose_name='تاریخ پایان اکران')
    price = models.BigIntegerField(verbose_name='قیمت بلیت')
    saleable_seats = models.IntegerField(verbose_name='صندلی های قابل فروش')
    free_seats = models.IntegerField(verbose_name='صندلی های خالی')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKETS_SOLD, 'بلیت ها تمام شد'),
        (SALE_CLOSED, 'فروش بلیت بسته شد'),
        (MOVIE_PLAYED, 'فیلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد')
    )
    status = models.IntegerField(verbose_name='وضعیت سانس', choices=status_choices)
    
    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)
