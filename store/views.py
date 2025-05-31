from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'store/index.html', {'books': books})

def Project2(request):
    return render(request, 'store/Project2.html')

def Project3(request):
    return render(request, 'store/Project3.html')

def Project4(request):
    return render(request, 'store/Project4.html')


from django.http import JsonResponse
from .models import Book, CartItem
def Project2(request):
    items = CartItem.objects.all()
    return render(request, 'store/Project2.html', {'items': items})


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Book, CartItem

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        quantity = int(request.POST.get('quantity', 1))
        book = Book.objects.get(id=book_id)
        CartItem.objects.create(book=book, quantity=quantity)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Book, CartItem

# ✅ دالة إفراغ السلة
@csrf_exempt
def clear_cart(request):
    if request.method == 'POST':
        CartItem.objects.all().delete()
    return redirect('project2')

