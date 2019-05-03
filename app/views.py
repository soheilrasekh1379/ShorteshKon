from django.shortcuts import render,redirect
from django.views.generic import View,RedirectView
from .forms import realUrlForm
from .models import shortUrl
# Create your views here.


class HomeView(View):
    template_name="home.html"

    def get(self,request):
        return render(request,self.template_name,{})

    def post(self,request):
        form = realUrlForm(request.POST)
        if form.is_valid():
            form.save()
            shorturl = form.instance.shorturl.url
            data = {'shorturl':shorturl}
            return render(request,self.template_name,data)



class RedirectUrlView(View):
    def get(self,request,id):
        url = shortUrl.objects.get(url=id).realurl_set.first().url
        return redirect(url)
