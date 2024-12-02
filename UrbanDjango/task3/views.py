from django.shortcuts import render

def main(request):
    return render(request, 'third_task/main.html')

def cart(request):
    return render(request, 'third_task/cart.html')

def shop(request):
    return render(request, 'third_task/shop.html')
