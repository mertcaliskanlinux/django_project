import mimetypes
from django.shortcuts import render
from .models import Account, Blog,Welcome,Skılls,Experience,Business_Areas,Certifica,Scholl,Interests,Expertise
# Create your views here.


def index(request):
    
    account_page = Account.objects.all()
    welcome_page = Welcome.objects.all()
    skılls_page = Skılls.objects.all()
    experience_page = Experience.objects.all()
    business_page = Business_Areas.objects.all()
    certifice_page = Certifica.objects.all()
    scholl_page = Scholl.objects.all()
    ınterests_page = Interests.objects.all()
    experties_page = Expertise.objects.all()
    blogs =  Blog.objects.order_by('?')[0:1]
    blog_rand = Blog.objects.order_by('?')[0:1]
    
    blog_rands = []
    for i in blog_rand:
        for j in blogs:
            if i != j:
                blog_rands.append(i)
            elif i == j:
                blog_rands = Blog.objects.filter()[0:1]

          

    
    context  = {
        'accounts':account_page,
        'welcomes':welcome_page,
        'skılls':skılls_page,
        'experiences':experience_page,
        'business':business_page,
        'certificas':certifice_page,
        'scholls':scholl_page,
        'ınterests':ınterests_page,
        'expertiess':experties_page,
        'blog':blogs,
        'blog_rand':blog_rands

    }

    return render (request,"blog-page/index.html",context)



from django.http import HttpResponse, Http404
import os
import mimetypes


def download_file(request):

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'test.pdf'
    # Define the full file path
    filepath = BASE_DIR + "/"+ filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value

    return response