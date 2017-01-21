from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,CreateAPIView
from .serializers import dataSearializer
from Genre.forms import AddGenreForm
from Genre.models import Genres

def GenreList_View(request):
    queryset = Genres.objects.all().order_by("genre_name")
    context={
    "object_list": queryset
    }
    return render(request,"genrelist.html",context)
def CreateGenre_View(request):
    if request.method == "POST":
        genren=request.POST.get("genretitle")
        Genres.objects.create(genre_name=genren)
        return HttpResponseRedirect('/genre')
    context = {

    }
    return render(request,"creategenrelist.html",context)
def UpdateGenre_View(request, id=None):
    instance = get_object_or_404(Genres,id=id)
    form = AddGenreForm(request.POST or None , instance= instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/genresearch')
    context = {
        "form":form
    }
    return render(request,"updategenre.html",context)

class datalist(ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = dataSearializer

class detailAPIview(RetrieveAPIView):
    queryset = Genres.objects.all()
    serializer_class = dataSearializer

class updatelist(UpdateAPIView):
    queryset = Genres.objects.all()
    serializer_class = dataSearializer

class createapiview(CreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = dataSearializer