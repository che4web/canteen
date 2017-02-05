#! -*- coding=utf-8 -*-
"""
Definition of views.
"""
from app import forms
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from newsApp.models import New
from menuApp.models import CategoryMenu
#from app.models import New

#from forms import ContactForm
#from django.views.generic.edit import FormView

from django.views.generic import ListView, DetailView
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'news':New.objects.all().order_by('-date')[0:3],
            'dishes':[CategoryMenu.objects.get(title=u'Горячее'),CategoryMenu.objects.get(title=u'Гарниры')]
            #'title':'Home Page',
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            #'title':u'Контакты',
            #'message':'Your contact page.',
            #'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

#class ContactView(FormView):
#    template_name = 'contact.html'
#    form_class = ContactForm
#    success_url = '/thanks/'

#    def form_valid(self, form):
#        # This method is called when valid form data has been POSTed.
#        # It should return an HttpResponse.
#        form.send_email()
#        return HttpResponse('{"data": "OK"}')

#    def form_invalid(self, form):
#        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
#        #error_list=[]
#        #for k, v in form.errors.items():
#        #    for e in v:
#        #        error_list.append(e)
#        #errors_dict =','.join(error_list)
#        return HttpResponseBadRequest(errors_dict)