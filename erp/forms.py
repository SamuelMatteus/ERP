from django import forms
from erp.models import Funcionario


class FuncionarioForms(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'email',
            'remuneracao'
        ]






