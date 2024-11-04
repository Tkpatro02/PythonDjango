from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Chaivarity

# Create your views here.
def all_chai(request):
   chais= Chaivarity.objects.all()
   return render(request, 'chai/all_chai.html',{'chais':chais})

def chai_detail(request, chai_id):
   chai=get_object_or_404(Chaivarity,pk=chai_id)
   return render(request,'chai/chai_detail.html',{'chai':chai})

def chai_Store_view(request):
    return render(request,'chai/chai_Stores.html')