from django.shortcuts import render

# Create your views here.
def beranda(request):
    judul = ["MATEMATIKA"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'beranda.html', konteks)