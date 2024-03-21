from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from .models import User, Tutor, Pet
import requests

def endereco(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if not response.ok:
        return None
    data = response.json()
    if 'erro' in data:
        return False
    endereco = {
        'uf': data.get('uf'),
        'localidade': data.get('localidade'),
        'bairro': data.get('bairro')
    }
    return endereco

def raca(raca):
    url = f'https://dog.ceo/api/breeds/list/all'
    response = requests.get(url)
    if not response.ok:
        return None
    data = response.json()
    racaPet = {
        'uf': data.get('uf'),
        'localidade': data.get('localidade'),
        'bairro': data.get('bairro')
    }
    return racaPet

def usuario(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == "GET":
        dados_usuario = User.objects.filter(username=request.user).first()
        if dados_usuario:
            return render(request, 'cadastrar.html', {'usuario': dados_usuario})

def tutor(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == "GET":
        dados_tutor = Tutor.objects.filter(user=request.user).first()
        if dados_tutor:
            return render(request, 'tutor.html', {'tutor': dados_tutor, 'endereco': endereco(dados_tutor.cep)})
        else:
            return render(request, 'tutor.html', {'tutor': ('','','')})
    if request.method == "POST":
        tutor, celular, cep = (
            request.POST.get(key) for key in ['tutor', 'celular', 'cep']
        )
        if endereco(cep) == False or len(cep) < 8:
            messages.error(request, 'Cep incorreto!')
            return redirect('/perfil/tutor')
        if len(celular) != 11:
            messages.error(request, 'Celular incompleto!')
            return redirect('/perfil/tutor')
        try:
            update = Tutor.objects.filter(user=request.user).first()
            if not update:
                Tutor.objects.create(
                    user=request.user,
                    tutor=tutor,
                    celular=celular,
                    cep=cep
                )
                messages.success(request, 'Tutor registrado com sucesso.')
            else:
                Tutor.objects.update(
                    user=request.user,
                    tutor=tutor,
                    celular=celular,
                    cep=cep
                )
                messages.success(request, 'Tutor atualizado com sucesso.')
            return redirect('/feed')
        except Exception as e:
            messages.error(request, f'Erro ao registrar tutor: {str(e)}')
            return redirect('/perfil/tutor')

def pet(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == "GET":
        dados_pet = Pet.objects.filter(user=request.user).first()
        if dados_pet:
            return render(request, 'pet.html', {'pet': dados_pet})
        else:
            return render(request, 'pet.html', {'pet': None}) #('','','')})

    if request.method == "POST":
        pet_data = {
            'user': request.user,
            'pet': request.POST.get('pet'),
            'fotos': request.FILES.get('fotos', None),
            'raca': request.POST.get('raca'),
            'dtVaci': request.POST.get('dtVaci'),
            'dtNasc': request.POST.get('dtNasc'),
            'sexo': request.POST.get('sexo'),
            'pedigree': request.POST.get('pedigree', False),
            'obs': request.POST.get('obs', None)
        }
        print(pet_data)
        # Aqui você pode adicionar validações adicionais conforme necessário
        if not all(pet_data.values()):
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('/perfil/pet')
        # ...
        try:
            update = Pet.objects.filter(user=request.user).first()
            if not update:
                Pet.objects.create(**pet_data)
                messages.success(request, 'Dados do pet registrados com sucesso.')
            else:
                for key, value in pet_data.items():
                    setattr(update, key, value)
                update.save()
                messages.success(request, 'Dados do pet atualizados com sucesso.')
                return redirect('/perfil/pet')
            
        except Exception as e:
            messages.error(request, f'Erro ao registrar dados do pet: {str(e)}')
            return redirect('/perfil/pet')