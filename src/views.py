from django.shortcuts import render

from  src.models.category import Category,Product
# Create your views here.
def index_page(request):
    ctg = Category.objects.all().order_by('-id')
    ctx = {
        'ctg':ctg
    }
    return render(request, 'index.html',ctx)
