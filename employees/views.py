from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from employees.models import Employees
from django.core.mail import EmailMultiAlternatives, BadHeaderError

def sendmail(request):
    latest_employees_list = Employees.objects.all()
    return render_to_response('employees/index.html', {'latest_employees_list': latest_employees_list},
        context_instance=RequestContext(request))

def send(request):
    #get Post from view
    mails_list = request.POST.getlist('employees')

    #mount mail
    if request.POST['subject']:
        subject = request.POST['subject']
    else:
        subject = "Sem titulo"

    if request.POST['body']:
        message = request.POST['body']
    else:
        message = "nenhuma mensagem"
    
    from_email = "brunousml@gmail.com"
    msg = EmailMultiAlternatives(subject, message, from_email, mails_list)
    msg.attach_alternative(message, "text/html")

    #sendMail
    if subject and message and from_email:
        try:
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/employees/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')