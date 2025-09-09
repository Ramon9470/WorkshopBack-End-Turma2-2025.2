from django.shortcuts import render
from .models import Endereco
from .forms import EnderecoForm
import requests

def home(request):
    form = EnderecoForm()
    return render(request, 'home.html', {'form': form})

def consulta_cep(request):
    form = EnderecoForm(request.GET or None)

    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if response.status_code == 200:
            data = response.json()
            endereco = Endereco(
                rua=data.get('logradouro', ''),
                bairro=data.get('bairro', ''),
                cidade=data.get('localidade', ''),
                estado=data.get('uf', ''),
                cep=data.get('cep', '')
            )

            endereco.save()
            return render(request, 'endereco.html', {'endereco': endereco})