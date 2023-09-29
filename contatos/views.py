from django.shortcuts import render
from contatos.models import Pessoa
from django.views.generic.base import View


# Create your views here.
class ContatoListView(View):
    def get(selfself, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        context = {'pessoas': pessoas, }
        return render(request, 'contatos/listaContatos.html', context)
