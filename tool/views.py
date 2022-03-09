from django.shortcuts import render
from tool import models


# Create your views here.
# 登出
def site(request):
    sites = models.Site.objects.all()
    return render(request, 'tool/site.html',
                  {'sites': sites})
