from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, entry):
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/title.html", {
        "entry": util.get_entry(entry),
        "title": title
    })
