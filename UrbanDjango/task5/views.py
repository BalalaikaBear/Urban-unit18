from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import ContactForm


users: list = [
    {'username': 'One', 'password': hash('11111111'), 'age': 22},
    {'username': 'Two', 'password': hash('22222222'), 'age': 22},
]


def registration(request: HttpRequest,
                 username: str,
                 password: str,
                 repeat_password: str,
                 age: int,
                 form: ContactForm | None = None) -> HttpResponse:

    # совпадение пароля
    if password != repeat_password:
        return render(request,
                      'fifth_task/registration_page.html',
                      {'answer': 'Пароли не совпадают', 'form': form})

    # проверка на возраст
    if age < 18:
        return render(request,
                      'fifth_task/registration_page.html',
                      {'answer': 'Вы должны быть старше 18 лет', 'form': form})

    # совпадение логина
    if list(filter(lambda user: user['username'] == username, users)):
        return render(request,
                      'fifth_task/registration_page.html',
                      {'answer': 'Пользователь уже существует', 'form': form})

    # добавление нового пользователя
    new_user: dict = {'username': username, 'password': hash(password), 'age': age}
    users.append(new_user)

    return render(request,
                  'fifth_task/registration_page.html',
                  {'answer': f'Приветствуем {username}!', 'form': form})


def sign_up_by_html(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        return registration(request, username, password, repeat_password, age)

    # если это GET
    return render(request,
                  'fifth_task/registration_page.html',
                  {'answer': 'Регистрация'})


def sign_up_by_django(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # проверка заполненности всех полей
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            return registration(request, username, password, repeat_password, age, form)

    else:
        form = ContactForm()

    return render(request,
                  'fifth_task/registration_page.html',
                  {'answer': 'Регистрация', 'form': form})
