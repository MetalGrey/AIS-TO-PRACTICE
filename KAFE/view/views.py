from django.shortcuts import render
from user.models import Question

def index(request):
    model = Question.objects.order_by('-id_tovara')
    return render(request, 'view/index.html', {'model':model})
