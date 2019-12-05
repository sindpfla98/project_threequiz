from django.db import models
from user.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from staff.models import * #추가
from staff.models import DonationOrg

# 씨앗
class Seed(models.Model):
    name = models.CharField('씨앗명', max_length=10)
    photo = models.ImageField('사진', upload_to='seed/')
    desc = models.TextField('설명', max_length=300)
    count = models.IntegerField('씨앗재고')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "씨앗정보"
        verbose_name = "씨앗"

# 생육상태
class Growth(models.Model):
    name = models.CharField('상태명', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "생육상태"
        verbose_name = "생육상태"

# 씨앗상태
class SeedState(models.Model):
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, verbose_name='씨앗명')
    growth = models.ForeignKey(Growth, on_delete=models.CASCADE, verbose_name='상태명')
    photo = models.ImageField('사진', upload_to='seedState/')

    def __str__(self):
        return "{}-{}".format(self.seed, self.growth)

    class Meta:
        verbose_name_plural = "씨앗상태"
        verbose_name = "씨앗상태"

# 작물상태
class PlantState(models.Model):
    state = models.CharField('상태', max_length=10)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='도구')
    CHOICES = (
        ('+', '증가'),
        ('-', '감소'),
    )
    change = models.CharField('증감구분', choices=CHOICES, max_length=5)
    change_exp = models.IntegerField('증감경험치')

    def __str__(self):
        return self.state

    class Meta:
        verbose_name_plural = "작물상태"
        verbose_name = "작물상태"

# 작물일지
class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', verbose_name='회원이름')
    seedState = models.ForeignKey(SeedState, on_delete=models.CASCADE, verbose_name='씨앗상태')
    plantState = models.ForeignKey(PlantState, on_delete=models.CASCADE, verbose_name='작물상태',null=True,blank=True)
    date = models.DateTimeField('일시', auto_now_add=True)
    exp = models.IntegerField('경험치', default=0, validators=[MinValueValidator(0), MaxValueValidator(600)])
    donation = models.ForeignKey(DonationOrg, on_delete=models.CASCADE, related_name='donations', verbose_name='기부단체'
                                 , null=True, blank=True)
    delivery = models.CharField('배달현황', choices=(("배송 중", "배송 중"), ("배송 완료", "배송 완료")), max_length=10, null=True, blank=True)
    # 외래키의 필드 불러와서 출력

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "작물일지"
        verbose_name = "작물"
    
# 잡초
class Weeds(models.Model):
    photo = models.ImageField('사진', upload_to='weeds/')

    class Meta:
        verbose_name_plural = "잡초"
        verbose_name = "잡초"

# 회원잡초
class UserWeeds(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='회원이름')
    weeds = models.ForeignKey(Weeds, on_delete=models.CASCADE, verbose_name='잡초')

    class Meta:
        verbose_name_plural = "회원잡초"
        verbose_name = "회원잡초"
        
        
