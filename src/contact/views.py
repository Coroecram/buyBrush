from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import contactForm


# Create your views here.
def contact(request):
	title = 'Contact'
	form = contactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		formData = form.cleaned_data
		subject = formData['subject']
		message = formData['comment']
		name = formData['name']
		emailFrom = formData['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail( subject, message, emailFrom, emailTo, fail_silently=True )
		title = "Thanks!"
		form = None
		confirm_message = "Thanks for the message, we will get right back to you!"

	context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
	template = 'contact.html'
	return render(request, template, context)
