from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

from .models import Show
def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        "Shows": Show.objects.all(),
        }
    return render(request, "tv_app/index.html", context)

def showtab(request, num):
    newDate = Show.objects.get(id=num).release_date.strftime("%d-%m-%Y")
    context = {
        "ID": num,
        "Title": Show.objects.get(id=num).title,
        "Network": Show.objects.get(id=num).network,
        "Release": newDate,
        "Description": Show.objects.get(id=num).description,
        "Update": Show.objects.get(id=num).updated_at
    }
    return render(request, "tv_app/showtab.html", context)

def newshows(request):
    return render(request, "tv_app/newshow.html")

def create(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST, None)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/new")
        else:
            Show.objects.create(title = request.POST["title"], network = request.POST["network"], release_date = request.POST["release"], description = request.POST["description"])
            newid = Show.objects.last().id
            print(newid)
            return redirect("/shows/" + str(newid))
    else:
        redirect("/shows/new")

def delete(request, num):
    rem = Show.objects.get(id=num)
    rem.delete()
    return redirect("/shows")

def edit(request, num):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST, num)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/" + num + "/edit")
        else:
            change = Show.objects.get(id=num)
            change.title = request.POST["title"]
            change.network = request.POST["network"]
            change.release_date = request.POST["release"]
            change.description = request.POST["description"]
            change.save()
            return redirect("/shows/" + num)
    else:
        newDate = Show.objects.get(id=num).release_date.strftime("%Y-%m-%d")
        context = {
            "ID": num,
            "Title": Show.objects.get(id=num).title,
            "Network": Show.objects.get(id=num).network,
            "Release": newDate,
            "Description": Show.objects.get(id=num).description,
        }
        print(context["Description"])
        return render(request, "tv_app/edit.html", context)