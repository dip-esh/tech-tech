from django.shortcuts import HttpResponseRedirect, render, reverse
from django.views import generic
from .models import Book, CustomUser
from .forms import RegisterUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

def members(request):
  context = {"first_name": "Dipesh Regmi"}
  return render(request, "my_form.html", context)


def get_data(request):
    print(request.POST["name"])
    context = {"first_name": "Dipesh Regmi"}
    return render(request, "my_form.html", context)


class BookListView(generic.ListView):
    model = Book
    template_name = "book_list.html"


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "confirm_delete.html"
    success_url = "/polls/books"

class BookDetailView(generic.DetailView):
    model = Book
    template_name = "book_detail.html"

    def get_queryset(self):
        return super().get_queryset()

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/polls")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterUserForm()

    return render(request, "registration/profile.html", {"form": form})
