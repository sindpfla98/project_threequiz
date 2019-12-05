from django.contrib import admin
from .models import *

# 씨앗
@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

# 생육상태
@admin.register(Growth)
class GrowthAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

# 씨앗상태
@admin.register(SeedState)
class SeedStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'seed', 'growth')
    list_display_links = ('id', 'seed', 'growth')

# 작물상태
@admin.register(PlantState)
class PlantStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state')
    list_display_links = ('id', 'state')

# 작물일지
@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'seedState')
    list_display_links = ('id', 'user', 'seedState')

    def date_at(self, obj):
        return obj.date.strftime("%Y-%m-%d")

    date_at.short_description = '날짜'

# 잡초
@admin.register(Weeds)
class WeedsAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')
    list_display_links = ('id', 'photo')

# 회원잡초
@admin.register(UserWeeds)
class UserWeedsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'weeds')
    list_display_links = ('id', 'user', 'weeds')

