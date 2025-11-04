from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")
def vaibhav(request):
    return HttpResponse("Hello, Vaibhav!")
def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})
def html(request):
    return HttpResponse("""
    <html>
        <head><title>Sample HTML</title></head>
        <body>
            <h1>This is sooooooooooooooooooooooooooooooooooo a sample HTML page</h1>
            <p>Welcome to the HTML response!</p>
        </body>
    </html>
    """)
# def hi(request):
#     return render(request, "hello/index.html")
