from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render,redirect


@login_required
def register(request):
	if request.user.username!='admin':
		return redirect('unauth')
	if request.method=='POST':
		registerform=UserCreationForm(request.POST)
		if registerform.is_valid():
			registerform.save()
			messages.success(request, f'Student added!')
			return redirect('dashboard')
	else:
		registerform=UserCreationForm()
	return render(request,'users/register.html', {'form' : registerform})