from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.conf import settings
# Create your views here.


class AngularApp(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        print("helloo")
        context = super(AngularApp, self).get_context_data(**kwargs)
        context['ANGULAR_URL'] = settings.ANGULAR_URL
        context['API_URL'] = settings.API_URL
        return context


class SampleView(View):
    """View to render django template to angular"""

    def get(self, request):
        return render("OK!")
