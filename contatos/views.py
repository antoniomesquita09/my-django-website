from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from contatos.forms import ContatoModel2Form
from contatos.models import Pessoa
from django.views.generic.base import View


# Create your views here.
class ContatoListView(View):
    def get(selfself, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        context = {'pessoas': pessoas, }
        return render(request, 'contatos/listaContatos.html', context)


class ContatoCreateView(View):
    def get(self, request, *args, **kargs):
        context = {'formulario': ContatoModel2Form}
        return render(request, 'contatos/criaContato.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ContatoModel2Form(request.POST)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
