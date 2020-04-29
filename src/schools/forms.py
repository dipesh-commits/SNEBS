from django import forms

from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
	class Meta:
		model = ContactMessage
		fields = ['contact_name','contact_email','contact_subject','contact_message']