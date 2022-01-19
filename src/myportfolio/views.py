from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from django.core.mail import send_mail
import environ


# Setting up environment file
env = environ.Env()
environ.Env.read_env('/portfolio/.env')


# Create your views here.
"""
Get repository titles and descriptions 
(if possible: repositories marked with a star)

TODO: use a more stable method of getting github data (if repos are pinned or the 
      start screen of the repo is not the default one: does not work!)
"""
def get_github_data():
    url = env('GITHUB_URL')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    repositories = soup.find_all(class_="repo")
    repo_dict = {}  # <name, description>
    for repo in repositories:
        title = repo.text
        d = repo.parent.parent.find_next_sibling("p").text
        description = d.lstrip().rstrip()   # remove whitespace
        repo_dict.update({title:description})
    return repo_dict



def index(request):
    # get first 3 github repositories ({title:description})
    repo_dict = get_github_data()
    first_three = {}
    counter = 0
    for key, value in repo_dict.items():
        if counter < 3:
            first_three.update({key:value})
            counter+=1;
        else:
            break
    

    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
        send_mail('Portfolio Mail!', message, '', [env('EMAIL_USER')])
        

    return render(request, 'myportfolio/index.html', {"repo_dict":first_three})