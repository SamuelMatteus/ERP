from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from erp.forms import FuncionarioForms
from erp.models import Funcionario


def home(request: HttpRequest):
    if request.method == 'GET':
        return render(request, template_name='erp/index.html')


def cria_funcionario(request: HttpRequest):
    if request.method == 'GET':
        form = FuncionarioForms()
        return render(
            request,
            template_name='erp/funcionarios/novo.html',
            context={'form': form}
        )

    elif request.method == 'POST':
        form = FuncionarioForms(request.POST)
        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)
            funcionario.save()
            return HttpResponseRedirect(redirect_to='/')


def lista_funcionarios(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        funcionarios = Funcionario.objects.all()

        return render(
            requisicao,
            template_name='erp/funcionarios/lista.html',
            context={'funcionarios': funcionarios}
        )


def busca_funcionario_por_id(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None
        return render(
            requisicao,
            template_name='erp/funcionarios/detalhe.html',
            context={'funcionario': funcionario}
        )


def atualiza_funcionario(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForms(instance=funcionario)
        return render(
            requisicao,
            template_name='erp/funcionarios/atualiza.html',
            context={'form': form}
        )

    elif requisicao.method == 'POST':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForms(requisicao.POST, instance=funcionario)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')
