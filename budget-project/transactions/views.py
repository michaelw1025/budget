from django.shortcuts import render
from .models import Recurring


# Create your views here.
def index(request):
    recurrings = Recurring.objects
    return render(request, 'transactions/index.html', {'recurrings': recurrings})
