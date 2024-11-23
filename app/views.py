from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sites.shortcuts import get_current_site
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.http import  HttpResponse, JsonResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
# from .serializers import EmailSerializer
from rest_framework.views import APIView
from django.db.models import Max, Count
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import status
from django.conf import settings
# from .utils import search_title
from django.views import View
from .models import *
# Create your views here.
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class Home(TemplateView):
    template_name = "index.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
             
        if 'name' in request.POST and 'email' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            try:
                validate_email(email)
                comment = request.POST.get('comments', None)
                if comment != None:
                    # UserMail.objects.create(email=email)
                    Gettouch.objects.create(name=name, email=email, comments = comment)
                    messages.success(request, "Successfully.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        
        return redirect('home')
    
class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        
        if 'firstname' in request.POST and 'lastname' in request.POST and 'contactemail' in request.POST:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            contactemail = request.POST.get('contactemail')
            subject = request.POST.get('subject')
            comments = request.POST.get('comments')
            privacypollicy = request.POST.get('privacypollicy')
            try:   
                validate_email(contactemail)
                comments = request.POST.get('comments', None)
                contactus.objects.create(first_name=firstname, last_name=lastname, email=contactemail ,subject=subject, comments=comments,privacy_policy_accepted=privacypollicy)
                messages.success(request, "Successfully.")
            except ValidationError:
                messages.error(request, "Invalid email address.")

        return redirect('contact')

class AboutUS(TemplateView):
    template_name = "about.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('about')

class Applcation(TemplateView):
    template_name = "application.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'name' in request.POST and 'email' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            try:
                validate_email(email)
                comment = request.POST.get('comments', None)
                if comment != None:
                    # UserMail.objects.create(email=email)
                    Gettouch.objects.create(name=name, email=email, comments = comment)
                    messages.success(request, "Successfully.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
                
        return redirect('applcation')
    
class SplitguargumProduct(TemplateView):
    template_name = "split-guar-gum.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('splitguargum')
    
class ChuriProduct(TemplateView):
    template_name = "churi.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('churiproduct')

class FastHydrationProduct(TemplateView):
    template_name = "fast-hydration.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('fastHydrationproduct')

class FoodGradeProduct(TemplateView):
    template_name = "food-grade.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('foodgradeproduct')

class IndustrialGradeProduct(TemplateView):
    template_name = "industrial-grade.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('industrialgradeproduct')

class KormaProduct(TemplateView):
    template_name = "korma.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('kormaproduct')

class PackagingStorage(TemplateView):
    template_name = "packaging-storage.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('packagingstorage')

class QualityControl(TemplateView):
    template_name = "quality-control.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'name' in request.POST and 'email' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            try:
                  
                validate_email(email)
                comment = request.POST.get('comments', None)
                if comment != None:
                    # UserMail.objects.create(email=email)
                    Gettouch.objects.create(name=name, email=email, comments = comment)
                    messages.success(request, "Successfully.")
            except ValidationError:
                messages.error(request, "Invalid email address.")

        return redirect('qualitycontrol')

