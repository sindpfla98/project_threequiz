from django.views.generic import TemplateView
from staff.models import DonationOrg
from plant.models import Diary
from user.models import User

import operator

# 190914 예림 수정
class FirstMixin(TemplateView):
    model = Diary

    def get_context_data(self, **kwargs):
        diry = super(FirstMixin, self).get_context_data(**kwargs)
        def user_diary_rank():
            user_rank = {}
            users = User.objects.all()
            for i in users:
                user = users.get(id=i.id)
                diary = Diary.objects.filter(user_id=i.id)
                user_exp = 0
                for j in diary:
                    user_exp += j.exp
                user_rank[user] = user_exp
            return sorted(user_rank.items(), key=operator.itemgetter(1), reverse=True)
        diry['diaries'] = user_diary_rank()[0:3]
        return diry

class SecondMixin(TemplateView):
    model = DonationOrg

    def get_context_data(self, **kwargs):
        ctx = super(SecondMixin, self).get_context_data(**kwargs)
        ctx['donationOrgs'] = DonationOrg.objects.filter(is_donate=1)
        return ctx


class HomeView(FirstMixin, SecondMixin):
    template_name = 'home.html'


