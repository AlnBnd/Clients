from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, ChangeStatusForm
from .models import Client

def client_list(request):
    responsible = request.user.id
    print(responsible)
    clients = Client.objects.filter(responsible_person=responsible)
    if request.method == 'POST':
        form = ChangeStatusForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            account_number = cd['account_number']
            try:
                client = Client.objects.filter(account_number=account_number, responsible_person=responsible)
                client.status = cd['status']
                client.save()
            except Client.DoesNotExist:
                pass
        return redirect('client_list')
    else:
        form = ChangeStatusForm()
    return render(request, 'client_list.html', {'clients': clients, 'form': form})

def update_client_status(request, client_id):
    if request.method == 'POST':
        status = request.POST.get('status')
        client = Client.objects.get(id=client_id)
        client.status = status
        client.save()
    return redirect('client_list')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('client_list')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})