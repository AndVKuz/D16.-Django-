from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from django.views.generic import ListView
from datetime import datetime
from .models import Article


class ArticleList(ListView):
    raise_exception = True
    model = Article
    ordering = '-time_in'
    template_name = 'Article.html'
    context_object_name = 'articles'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now', 'is_reg'] = datetime.utcnow(), \
            self.request.user.groups.filter(name='Зарегистрированные пользователи').exists()
        return context


# @permission_required('polls.add_choice', raise_exception=True)
# @login_required
# def my_view(request):
#     return HttpResponse(content={'count': count_var})
#
#
# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'