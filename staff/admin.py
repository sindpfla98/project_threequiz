from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
from plant.models import Diary
import operator

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_display_links = ['id', 'name', ]
    search_fields = ['name']
    ordering = ['name']

@admin.register(Board)
class BoardAdmin(SummernoteModelAdmin):
    list_display = ['id', 'user', 'title', ]
    list_display_links = ['id', 'user', 'title', ]
    list_filter = ['category']

@admin.register(QnA)
class QnAAdmin(SummernoteModelAdmin):
    list_display = ['id', 'user', 'title', ]
    list_display_links = ['id', 'user', 'title', ]

@admin.register(DonationOrg)
class DonationOrgAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_desc', 'url', ]
    list_display_links = ['id', 'name', 'short_desc', ]

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo', ]
    list_display_links = ['id', 'name', 'photo', ]

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', ]
    list_display_links = ['id', 'name', ]


@admin.register(DonationOrgSelect)
class DonationOrgSelectAdmin(admin.ModelAdmin):
    change_list_template = 'admin/donationOrg_select_change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset.order_by('id')
        except(AttributeError, KeyError):
            return response
        def donation_select():
            donation = DonationOrg.objects.all()
            user_diary = Diary.objects.all()
            cnt_lst = []
            for a in donation:
                count = 0
                for i in user_diary:
                    if a.id == i.donation_id:
                        count += 1
                cnt_lst.append(count)
            return cnt_lst
        dnt_lst ={}
        for i in range(0, DonationOrg.objects.all().count()):
            dnt_lst[qs[i]] = donation_select()[i]

        response.context_data['dnt_lst'] = sorted(dnt_lst.items(), key=operator.itemgetter(1), reverse=True)

        return response
