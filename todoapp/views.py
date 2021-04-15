from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ToDo
# Create your views here.
def index(request):
    todo=ToDo.objects.all()
    if request.method=='POST':
        new_todo=ToDo(
            title=request.POST['addtitle']
        )
        new_todo.save()
        # return HttpResponse("<h1>success fully added</h1>")
        return redirect('/')
    return render(request,'index.html',{'todos':todo})

def delete(request,pk):
    todo=ToDo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

