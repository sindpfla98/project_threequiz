from django.contrib import admin
from .models import Rank, User, Item, HaveItem

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'rank')
    list_display_links = ('id', 'rank')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'birth', 'joined_at', 'last_login_at', 'is_superuser', 'is_active')
    list_display_links = ('id', 'email')
    exclude = ('password',)                           # 사용자 상세 정보에서 비밀번호 필드를 노출하지 않음

    fieldsets = (
        (None, {
                    'fields': ('name', 'email', 'birth', 'postcode', 'address', 'detail_address', 'ref_address', 'phone',
                       'ticket', 'ticketing', 'rank')
        }),
        ('회원관리', {
            'classes': ('collapse',),
            'fields': ('date_joined', 'is_staff', 'is_active', 'is_superuser')
        })
    )

    def joined_at(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d")

    def last_login_at(self, obj):
        if not obj.last_login:
            return ''
        return obj.last_login.strftime("%Y-%m-%d %H:%M")

    joined_at.admin_order_field = '-date_joined'      # 가장 최근에 가입한 사람부터 리스팅
    joined_at.short_description = '가입일'
    last_login_at.admin_order_field = 'last_login_at'
    last_login_at.short_description = '최근로그인'


# 5.28
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(HaveItem)
class HaveItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'item_count',)
    list_display_links = ('item', 'user',)