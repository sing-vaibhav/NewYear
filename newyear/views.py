from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "Monday": now.weekday() == 0,
        "Tuesday": now.weekday() == 1,  
        "Wednesday": now.weekday() == 2,
        "Thursday": now.weekday() == 3,
        "Friday": now.weekday() == 4,
        "Saturday": now.weekday() == 5,
        "Sunday": now.weekday() == 6,
        })