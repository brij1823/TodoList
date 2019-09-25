from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import Tutorials,List

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login,logout,authenticate

from django.contrib import messages
from .forms import ListForm

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



def homepage(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request , ('Item has been added to List!'))
			return render(request , 'main/home.html' , {'all_items' : all_items})
	else:
		all_items = List.objects.all
		return render(request , 'main/home.html' , {'all_items' : all_items})


def todo(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request , ('Item has been added to List!'))
			return render(request , 'main/todo.html' , {'all_items' : all_items})
	else:
		all_items = List.objects.all
		return render(request , 'main/todo.html' , {'all_items' : all_items})
	
	
def register(request):

	if(request.method == 'POST'):
		form = UserCreationForm(request.POST)
		if(form.is_valid()):
				user = form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f"New Accounted Created: {username}")
				login(request,user)

				messages.info(request, f"You are now logged in as : {username}")
				return redirect("main:homepage")
		else:
				for msg in form.error_messages :
					messages.error(request, f"{msg} : {form.error_messages[msg]}")


	form = UserCreationForm
	return render(request,"main/register.html" , context={"form" : form})


def logout_request(request):
	logout(request)
	messages.info(request,"Logout Successfully")
	return redirect("main:homepage")

def login_request(request):
		if(request.method == 'POST'):
			form = AuthenticationForm(request,data = request.POST)

			if(form.is_valid()):
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')

				user = authenticate(username = username,password = password)

				if user is not None:
					login(request,user)
					messages.info(request, f"You are now logged in as : {username}")
					return redirect("main:homepage")
			else:
				messages.error(request , "Invalid username or password")
		else:
				messages.error(request , "Invalid username or password")
		form = AuthenticationForm()
		return render(request,"main/login.html",{"form" : form} )



def delete(request, list_id):
	item = List.objects.get(pk = list_id)
	item.delete()
	messages.success(request , ('Item Has Been Deleted!'))
	return redirect("/homepage/")



def cross_off(request , list_id):
	item = List.objects.get(pk = list_id)
	item.completed = True
	item.priority = 'Completed'
	item.save()
	return redirect("/homepage/")

def uncross(request , list_id):
	item = List.objects.get(pk = list_id)
	item.completed = False
	item.priority = 'Incomplete'
	item.save()
	return redirect('/homepage/')

def high(request , list_id):
	item = List.objects.get(pk = list_id)
	item.priority = 'High'
	item.save()
	return redirect('/homepage/')

def medium(request , list_id):
	item = List.objects.get(pk = list_id)
	item.priority = 'Medium'
	item.save()
	return redirect('/homepage/')

def low(request , list_id):
	item = List.objects.get(pk = list_id)
	item.priority = 'Low'
	item.save()
	return redirect('/homepage/')

def incomplete(request , list_id):
	item = List.objects.get(pk = list_id)
	item.priority = 'Incomplete'
	item.save()
	return redirect('/homepage/')

def edit(request , list_id):
	if request.method == 'POST':
		item = List.objects.get(pk = list_id)

		form = ListForm(request.POST or None , instance = item)

		if form.is_valid():
			form.save()
			messages.success(request,('Item has been Edited'))
			return redirect('/homepage/')
	else:
		item = List.objects.get(pk = list_id)
		return render(request , 'main/edit.html' , {'item' : item})


def priority(request , list_id):
	item = List.objects.get(pk = list_id)
	item.priority = 'Critical'
	item.save()
	return redirect('/homepage/')


def mail_request(request):
	if request.method == 'POST':
		all_items = List.objects.all()
		message = ''
		for i in all_items:
			message = message+i.item+' '+i.priority+'\n'
		to_mail = request.POST['to_email']
		send_mail('To-DO Report',
			message,
			settings.EMAIL_HOST_USER,
			[to_mail],
			fail_silently = False)
	messages.success(request , ('Email Sent Successfully!'))
	
	return redirect('/homepage/')

def email(request):
	all_items = List.objects.all
	todo_list = ''
	print(all_items)
	return render(request , 'main/email.html',{"items":all_items})