from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Adolescente
from .forms import AdolescenteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("listar_adolescentes")  # Redireciona para a lista após login
        else:
            messages.error(request, "Usuário ou senha inválidos. Por favor, verifique suas credenciais e tente novamente.")


    return render(request, "adolescentes/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")  # Redireciona para a tela de login após logout

@login_required
def listar_adolescentes(request):
    adolescentes = Adolescente.objects.all()
    return render(request, 'adolescentes/listar.html', {'adolescentes': adolescentes})

@login_required
def criar_adolescente(request):
    if request.method == "POST":
        data_nascimento = request.POST.get("data_nascimento")

        # Limpa mensagens antigas
        storage = get_messages(request)
        list(storage)  # Isso esvazia o iterador de mensagens

        # Validação de data
        if data_nascimento:
            try:
                data = datetime.strptime(data_nascimento, '%d/%m/%Y')
                if data > datetime.now():
                    messages.error(request, "A data de nascimento não pode ser no futuro.")
                    return redirect('criar_adolescente')
            except ValueError:
                messages.error(request, "Formato de data inválido. Use dia/mês/ano.")
                return redirect('criar_adolescente')

        # Processa formulário
        form = AdolescenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_adolescentes')
    else:
        form = AdolescenteForm()
    return render(request, 'adolescentes/criar_adolescente.html', {'form': form})

@login_required
def editar_adolescente(request, id):
    adolescente = get_object_or_404(Adolescente, id=id)
    if request.method == "POST":
        form = AdolescenteForm(request.POST, request.FILES, instance=adolescente)
        if form.is_valid():
            form.save()
            return redirect('listar_adolescentes')
    else:
        form = AdolescenteForm(instance=adolescente)
    return render(request, 'adolescentes/criar_adolescente.html', {'form': form})

@login_required
def excluir_adolescente(request, id):
    adolescente = get_object_or_404(Adolescente, id=id)
    if request.method == "POST":
        adolescente.delete()
        return redirect('listar_adolescentes')
    return render(request, 'adolescentes/confirmar_exclusao.html', {'adolescente': adolescente})
