#! -*- coding=utf-8 -*-

"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

    from django import forms

    class ContactForm(forms.Form):
        name = forms.CharField()
        phone = forms.CharField()
        email = forms.EmailField()
        message = forms.CharField(widget=forms.Textarea,required=False)

        def send_email(self):
            # send email using the self.cleaned_data dictionary
            plaintext = get_template('app/mail_detail.html')
            b= {'name':self.cleaned_data['name'],
                'phone':self.cleaned_data['phone'],
                'email':self.cleaned_data['email'],
                'text':self.cleaned_data['message']}
            message_body = plaintext.render(b)
            email = EmailMultiAlternatives('Письмо с сайта Столовой',
                             message_body,
                             #to=['che-email@yandex.ru'
                             to=['tanuffko24@gmail.com',
                                 #'pit-line@bk.ru',
                                 ])

            email.attach_alternative(message_body, "text/html")
            email.send()

