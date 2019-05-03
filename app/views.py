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
        shorturl = shortUrl.objects.get(url=id)
        shorturl.num_of_visits +=1
        shorturl.save()
        url = shorturl.realurl_set.first().url
        return redirect(url)
