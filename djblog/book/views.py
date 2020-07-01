from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from djblog.book.forms import BookForm
from .models import Book


def book_list(request):
    object_list = Book.objects.all()
    return render(request, 'books/book_list.html', {'object_list': object_list})


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            object_list = Book.objects.all()
            data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
                'object_list': object_list
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    data = dict()
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        object_list = Book.objects.all()
        data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
            'object_list': object_list
        })
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        'books/includes/partial_book_create.html',
        context,
        request=request
    )
    return JsonResponse(data)


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'books/includes/partial_book_update.html')


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        object_list = Book.objects.all()
        data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
            'object_list': object_list
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/includes/partial_book_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)
