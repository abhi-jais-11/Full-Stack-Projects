from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.


def IndexView(request):
    if request.user.is_authenticated:
        return render(
            request,
            "app/index.html",
            {"notes": Note.objects.filter(user_name=request.user).order_by('-pk').all()},
        )
    else:
        return render(
            request,
            "app/index.html",
            {"notes": []},
        )


def CreateView(request):
    if request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return redirect("/")

        form = CreateNoteForm()
        return render(request, "app/create.html", {"form": form})

    form = CreateNoteForm()
    return render(request, "app/create.html", {"form": form})


def EditView(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("/")

    form = EditNoteForm(instance=note)
    return render(request, "app/edit.html", {"form": form})


def DeleteView(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("/")
