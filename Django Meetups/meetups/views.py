
from django.shortcuts import render, redirect 
#from django.http import HttpResponse

# getting data from database
from .models import Meetup, Participant
# to handle form which is initiated at forms.py file
from .forms import RegistrationForm


# Create your views here.

def index(request):
    # return HttpResponse('Hello meetups!!')

    meet = Meetup.objects.all()
    # should not include 'templates/' because django knows that it is in templates
    return render(request, 'meetups/index.html', {
        'show_meetup': True,
        'meetup': meet
    })

def details(request, meetup_slug):
    print(meetup_slug)
    print(request.method)
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registrationForm = RegistrationForm()
            print(selected_meetup)
        elif request.method == 'POST':
            # request.POST is a property which carries the posted data by the user
            registrationForm = RegistrationForm(request.POST)
            if registrationForm.is_valid():
                # participant= registrationForm.save()
                user_email = registrationForm.cleaned_data['email']
                # get_or_create -> returns a tuple where it checks if the participant iscreated and adds in the second argument
                participant, _ = Participant.objects.get_or_create(email=user_email)
                #first participant is a variable where model is created and second participant the registrationForm saved variable
                selected_meetup.participant.add(participant)
                return redirect('reg-success', meetup_slug = meetup_slug)

        return render(request, 'meetups/details.html', {
                'meetup_found' : True,
                'detail': selected_meetup,
                'form': registrationForm,
            })
    except Exception as e:
        print(e)
        return render (request, 'meetups/details.html', {
            'meetup_found' : False
        })

def registrationSuccess(request, meetup_slug):
    print(meetup_slug)
    meetup = Meetup.objects.get(slug = meetup_slug)
    print(meetup.orgainser_email)
    return render(request, 'meetups/registrationSuccess.html', {
        'organiser_email': meetup.orgainser_email
    })
