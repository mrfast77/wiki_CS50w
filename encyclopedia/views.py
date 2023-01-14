from django.shortcuts import render
from re import search
from . import util
from markdown2 import Markdown
import random

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

def add(request):

    if request.method == "POST":

        title = request.POST.get('title')
        new_entry = request.POST.get('new_entry')
        existing_entries = util.list_entries()

        for entry in existing_entries:
            if title.lower() == entry.lower():
                return render(request, "encyclopedia/add.html", {
                    "message": "This title already exists. Please select a new title"
                })

        markdowner = Markdown()
        new_converted_entry = markdowner.convert(new_entry)

        util.save_entry(title, new_converted_entry)

        return render(request, "encyclopedia/new.html", {
            "title": title,
            "new_entry": new_converted_entry
            })
    
    return render(request, "encyclopedia/add.html")


def search_view(request):
    query = request.GET.get("q")
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

       
    return render(request, "encyclopedia/search.html", {
    "entries": searched_entries,
    "message": message
    })
         

def title(request, entry):
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/error.html")
    
    return render(request, "encyclopedia/title.html", {
        "entry": convert_to_html(entry),
        "title": entry
    })


def edit(request):
    if request.method == 'POST':
        title = request.POST["title"]
        content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

def save(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "entry": convert_to_html(title)
        })


def rand(request):
    entries = util.list_entries()
    rand_int = random.randint(0, (len(entries)-1))
    random_entry = entries[rand_int]
    return render(request, "encyclopedia/title.html", {
        "title": random_entry,
        "entry": convert_to_html(random_entry)
    })

