# forms.py
from django import forms
from .models import ContactForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['nom_complet', 'objet', 'email', 'contenu_message']

    def save(self, commit=True):
        contact = super(ContactForms, self).save(commit=False)
        if commit:
            contact.save()
        return contact
    
    def __init__(self, *args, **kwargs):
        super(ContactForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            'nom_complet',
            'objet',
            'email',
            'contenu_message',
            Submit('submit', 'Submit', css_class='btn-success')
        )