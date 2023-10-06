from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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


class ContatoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        formulario = ContatoModel2Form(instance=pessoa)
        context = {'pessoa': formulario}
        return render(request, 'contatos/atualizaContato.html', context)

    def post(self, request, pk, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=pessoa)
        if formulario.is_valid():
            pessoa = formulario.save()
            pessoa.save()
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
        else:
            context = {'pessoa': formulario}
            return render(request, 'contatos/atualizaContato.html', context)


class ContatoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = {'pessoa': pessoa, }
        return render(request, 'contatos/apagaContato.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
