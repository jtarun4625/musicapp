from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from .forms import AddtrackForm
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,CreateAPIView
from .serializers import dataSearializer
from Genre.models import Genres
from Track.models import Tracks
import json


def List_View(request):
    queryset_list = Tracks.objects.all().order_by("-track_rating")
    query = request.GET.get('search')
    if query:
        queryset_list = queryset_list.filter(Q(track_name__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,

    }
    return render(request, "index.html", context)


def Track_detail(request, id=None):
    instance = get_object_or_404(Tracks, id=id)
    context = {
        "details": instance
    }
    return render(request, "track_details.html", context)


def Create_track(request):
    instance = Genres.objects.all()
    form = AddtrackForm()
    if request.method == "POST":
        trackn = request.POST.get("tracktitle")
        trackg = request.POST.getlist("trackgenre")
        trackr = request.POST.get("trackrating")
        n_track = ""
        print(trackg)
        for track_g in trackg:
            n_track = n_track + track_g + "|"
        print(n_track)
        Tracks.objects.create(track_name=trackn, track_genre=n_track, track_rating=trackr)
        return HttpResponseRedirect('/music')

    context = {
        "form": form,
        "instance": instance,

    }
    return render(request, "addtrack.html", context)


def Update_track(request, id=None):
    instance = get_object_or_404(Tracks, id=id)
    form = AddtrackForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/music')
    context = {
        "instance": instance,
        "form": form
    }
    return render(request, "edittrack.html", context)


def Delete_track(request, id=None):
    instance = get_object_or_404(Tracks, id=id)
    instance.delete()
    return HttpResponseRedirect('/music')
    return render(request, "deletetrack.html", {})


class SearchList(ListAPIView):
    serializer_class = dataSearializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return Tracks.objects.filter(track_name__icontains=username)

class datalist(ListAPIView):
    queryset = Tracks.objects.all()
    serializer_class = dataSearializer

class detailAPIview(RetrieveAPIView):
    queryset = Tracks.objects.all()
    serializer_class = dataSearializer

class updatelist(UpdateAPIView):
    queryset = Tracks.objects.all()
    serializer_class = dataSearializer

class createapiview(CreateAPIView):
    queryset = Tracks.objects.all()
    serializer_class = dataSearializer

