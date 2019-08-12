from django.http import HttpResponse
from django.template import loader
from .forms import publicacionForm, contactoForm
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
#probando unas cositas ricas que quiero
from .models import Publicacion
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

import sendgrid
import os
from sendgrid.helpers.mail import *






publicaciones = Publicacion.objects.all()

def index(request):
	publicaciones = Publicacion.objects.all()
	template = loader.get_template('src/index.html')
	context = {"publicaciones": publicaciones}
	return HttpResponse(template.render(context, request))

def detail(request, publicacion_id):
    template = loader.get_template('src/post.html')
    p = Publicacion.objects.get(pk=publicacion_id)
    context = {"p": p}

    if p.imagen:
        image_url = settings.MEDIA_URL + str(p.imagen)
        resized_url = image_url.replace(".png", ".large.png")
        context.update({
            "image_url": image_url,
            "resized_url": resized_url

        })


    return HttpResponse(template.render(context,request))

def nosotros(request):
	template = loader.get_template('src/about.html')
	context = {}
	return HttpResponse(template.render(context, request))

@login_required
def createPost(request):
    if request.method == "POST":
        form = publicacionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('detail', publicacion_id=post.pk)
    else:
        form = publicacionForm()
    return render(request, 'src/createPost.html', {'form': form})


@login_required
def editPost(request, publicacion_id):
	p = get_object_or_404(Publicacion, pk=publicacion_id)
	form = publicacionForm(request.POST or None, request.FILES or None,instance=p)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print(instance.get_absolute_url())
		return HttpResponseRedirect(instance.get_absolute_url())
	return render(
		request,
		"src/createPost.html",
		{'form': form}
	)
@login_required
def deletePost(request, publicacion_id):
	p = Publicacion.objects.get(pk=publicacion_id)
	p.delete()
	return redirect("index")


def contact(request):
	if request.method == 'GET':
		form = contactoForm()
	else:
		form = contactoForm(request.POST)
		if form.is_valid():
			tema = form.cleaned_data['tema']
			mensaje = form.cleaned_data['mensaje']
			email = form.cleaned_data['email']

			# print('nombre',tema,email,mensaje)

			send_mail(tema, mensaje, email, ['lautaro.matiasosa@gmail.com'], fail_silently=False)
			return redirect('index')
	return render(request, "src/contact.html", {'form': form})


# def login(request):
# 	template = loader.get_template('src/login.html')
# 	context = {}
# 	return HttpResponse(template.render(context, request))

def posts(request):
	publicaciones = Publicacion.objects.all()
	template = loader.get_template('src/posts.html')
	context = {"publicaciones": publicaciones,}
	return HttpResponse(template.render(context, request))

