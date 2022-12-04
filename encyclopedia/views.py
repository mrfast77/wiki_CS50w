from django.shortcuts import render
from re import search
from . import util
from markdown2 import Markdown

def convert_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    entries_list = util.list_entries()
    searched_entries = []

    message = "No results found"

    for entry in entries_list:
        if query.lower() == entry.lower():
            return render(request, "encyclopedia/title.html", {
            "entry": convert_to_html(query),
            "title": title         
            })

        if query.lower() in entry.lower():
            searched_entries.append(entry)
        
        else:
            return render(request, "encyclopedia/search.html", {
            "message": message
            })

    return render(request, "encyclopedia/search.html", {
    "entries": searched_entries
    })
         

def title(request, entry):
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/title.html", {
        "entry": convert_to_html(entry),
        "title": title
    })
