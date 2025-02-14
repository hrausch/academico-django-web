from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')


#view executada quando o formulário de cadastrado é submetido
def submit_register(request):
    if request.method == 'POST':
        nome = request.POST.get('registerName')
        pwd = request.POST.get('registerPassword')
        correio_eletronico = request.POST.get('registerEmail')

        print(f"Nome: {nome}, Email: {correio_eletronico}, Senha: {pwd}")

        if nome and pwd and correio_eletronico:
            message = f"Nome: {nome}, Email: {correio_eletronico}, Senha: {pwd}"
            return HttpResponse(message)
        else:
            return HttpResponse("Algum campo está vazio.")
    else:
        return HttpResponse("Erro ao processar.")