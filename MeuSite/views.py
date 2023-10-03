from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# função que retorna True/False
def testaAcesso(user):
    # coloque aqui os testes que você precisar
    if user.has_perm('contatos.change_pessoa'):
        return True
    else:
        return False


# Create your views here.
def homeSec(request):
    return render(request, "registro/homeSec.html")


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
        context = {'form': formulario, }
        return render(request, 'registro/registro.html', context)


@login_required
@user_passes_test(testaAcesso)
def paginaSecreta(request):
    return render(request, 'registro/paginaSecreta.html')
