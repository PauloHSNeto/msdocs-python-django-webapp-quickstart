from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddAnimalForm
from .models.animais import *


def home(request):
	animal = Animal.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Você está logado...")
			return redirect('home')
		else:
			messages.success(request, "Houve um erro ao tentar logar...Tente novamente...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'animal':animal})


def login_user(request):
	records = Animal.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Você está logado...")
			return redirect('home')
		else:
			messages.success(request, "Houve um erro ao tentar logar...Tente novamente...")
			return redirect('login')
	else:
		return render(request, 'login.html', {'animais':records})


def logout_user(request):
	logout(request)
	messages.success(request, "Você saiu da sua conta...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Você foi registrado com sucesso, Bem vindo!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def registro_do_animal(request, pk):
	if request.user.is_authenticated:
		animais = Animal.objects.get(id=pk)
		return render(request, 'record.html', {'animais':animais})
	else:
		messages.success(request, "Voce precisa estar logado para fazer isso...")
		return redirect('home')



def delete_animal(request, pk):
	if request.user.is_authenticated:
		delete_it = Animal.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Animal Deletado com sucesso!")
		return redirect('home')
	else:
		messages.success(request, "Você precisa estar logado para fazer isso...")
		return redirect('home')


def add_animal(request):
	form = AddAnimalForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save(commit=False)
				messages.success(request, "Animal adcionado com sucesso")
				add_record.save()
				return redirect('home')
			messages.success(request, "formulário inválido")
			return redirect('home')
		return render(request, 'add_animal.html', {'form':form})
	else:
		messages.success(request, "Você precisa estar logado para fazer isso...")
		return redirect('home')




def update_animal(request, pk):
    if request.user.is_authenticated:
        current_animal = Animal.objects.get(id=pk)
        form = AddAnimalForm(request.POST or None, instance=current_animal)

        if 'ani_dnasc' in form.fields and current_animal.ani_dnasc:
            initial_date = current_animal.ani_dnasc.isoformat()
            form.fields['ani_dnasc'].initial = initial_date

        if form.is_valid():
            form.save()
            messages.success(request, "Animal Atualizado")
            return redirect('home')
        return render(request, 'update_animal.html', {'form':form})
    else:
        messages.success(request, "Você precisa estar logado para fazer isso...")
        return redirect('home')


def pet_list(request):
	if request.user.is_authenticated:
		animals = Animal.objects.all()
		return render(request, 'pet_list.html', {'animals':animals})
	else:
		messages.success(request, "Você precisa estar logado para fazer isso...")
		return redirect('home')

def animal_profile(request, pk):
	if request.user.is_authenticated:
		animal = Animal.objects.get(id=pk)
		return render(request, 'animal_profile.html', {'animal':animal})
	else:
		messages.success(request, "Você precisa estar logado para fazer isso...")
		return redirect('home')