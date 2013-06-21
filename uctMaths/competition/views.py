# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import loader, Context
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django import forms
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from competition.forms import StudentForm, SchoolForm, InvigilatorForm, VenueForm, testForm #, StudentFilter
from competition.models import SchoolStudent, School, Invigilator, Venue 


def index(request):
	return render_to_response('base.html', {})

def content (request):
   #t = loader.get_template('base.html')
   return render_to_response('contents.html',{})
   #return HttpResponse(t.render(base.html))

def profile(request):
    return render_to_response('profile.html',{})

def main (request):
   return render_to_response('main.html',{})


# def regStudent (request, ):
#    return render_to_response('regStudent.html',{})

#def index(request):
 #   return render_to_response('onlinemaths.html', {})

#******************************************
def students(request):
    return render_to_response('profile.html',{})

def schools(request):
    return render_to_response('profile.html',{})

def venues(request):
    return render_to_response('profile.html',{})

def invigilators(request):
    return render_to_response('profile.html',{})

#Register Students    
def newstudents(request):
   if request.method == 'POST': # If the form has been submitted...
        form = (request.POST) # A form bound to the POST data
        #print "FORM ", form
        print "here1", form
       # print "here1", form1
       # print "here2", form.is_valid()
        #if form.is_valid(): 
        for i in range (2):
          firstname = form.getlist('firstname',"")[i]
          surname = form.getlist('surname',"")[i]
          language = form.getlist('language',"")[i]
          reference = 1234
          school = School.objects.get(pk=int(form.getlist('school',"")[i]))
          print "here2 ", firstname
          print "here3 ", school
          grade = form.getlist('grade',"")[i]
          sex = form.getlist('sex',"")[i]              
          query = SchoolStudent(firstname = firstname , surname = surname, language = language,reference = reference,
                  school = school, grade = grade , sex = sex)
          query.save()
        return HttpResponseRedirect("IT'S BEEN SUBMITTED") # Redirect after POST
  else:
        form = StudentForm() # An unbound form

   schoolOptions = School.objects.all()
   c = {'schools':schoolOptions, 'range':range(2)}
   c.update(csrf(request))
   return render_to_response('newstudents.html', c)


#*****************************************
#Register Schools
def newschools (request):
  if request.method == 'POST': # If the form has been submitted...
        form = SchoolForm(request.POST) # A form bound to the POST data
        #print "FORM ", form
        print "here1", form
        print "here2", form.is_valid()
        if form.is_valid(): 
            name = form.cleaned_data['name']
            key = "1234" #************FIX!!!!!!!!!!!!!!!!
            language = form.cleaned_data['language']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            fax = form.cleaned_data['fax']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            
            query = School(name = name ,key = key ,  language = language  ,
                address = address, phone = phone , fax = fax, contact = contact , email = email)
            query.save()

            return HttpResponseRedirect("IT'S BEEN SUBMITTED") # Redirect after POST
  else:
        form = SchoolForm() # An unbound form
  
  c = {}
  c.update(csrf(request))
  return render_to_response('newschools.html', c)

#******************************************
#Register Invigilators
def newinvigilators (request):
  if request.method == 'POST': # If the form has been submitted...
        form = InvigilatorForm(request.POST) # A form bound to the POST data
        #print "FORM ", form
        print "here1", form
        print "here2", form.is_valid()
        if form.is_valid(): 
            school = form.cleaned_data['school']
            firstname = form.cleaned_data['firstname']
            surname = form.cleaned_data['surname']
            grade = form.cleaned_data['grade']
            venue = form.cleaned_data['venue']
            inv_reg = form.cleaned_data['inv_reg']
            phone_h = form.cleaned_data['phone_h']
            phone_w = form.cleaned_data['phone_w']
            fax = form.cleaned_data['fax']
            fax_w = form.cleaned_data['fax_w']
            email = form.cleaned_data['email']
            responsible = form.cleaned_data['responsible']
            
            
            query = Invigilator(school = school , firstname = firstname,surname = surname, grade = grade ,
                venue = venue ,inv_reg = inv_reg,
                phone_h = phone_h , phone_w = phone_w, 
                fax = fax, fax_w = fax_w , email = email, responsible = responsible)
            query.save()

            return HttpResponseRedirect("ITS BEEN SUBMITTED") # Redirect after POST
  else:
        form = InvigilatorForm() # An unbound form
  schoolOptions = School.objects.all()
  c = {'schools':schoolOptions}
  c.update(csrf(request))
  return render_to_response('newinvigilators.html', c)

#***************************************
#Register Venues
def newvenues (request):
  if request.method == 'POST': # If the form has been submitted...
        form = VenueForm(request.POST) # A form bound to the POST data
        #print "FORM ", form
        print "here1", form
        print "here2", form.is_valid()
        if form.is_valid(): 
            code = form.cleaned_data['code']
            building = form.cleaned_data['building']
            seats = form.cleaned_data['seats']
            bums = form.cleaned_data['bums']
            grade = form.cleaned_data['grade']
            pairs = form.cleaned_data['pairs']
                        
            query = Venue(code = code , building = building  ,
                seats = seats, bums = bums , grade = grade, pairs = pairs)
            query.save()

            return HttpResponseRedirect("IT'S BEEN SUBMITTED") # Redirect after POST
  else:
        form = VenueForm() # An unbound form
   
  c = {}
  c.update(csrf(request))
  return render_to_response('newvenues.html', c)

#******************************************  
def search_form (request):
  building = ""
  #code = ""
  if request.method == 'POST': # If the form has been submitted...
        form = testForm(request.POST) # A form bound to the POST data
        #print "FORM ", form
        print "here1", form
        print "here2", form.is_valid()
        if form.is_valid():
            building = form.cleaned_data['building']
            #code = form.cleaned_data['code']
            
            #return HttpResponseRedirect("IT'S BEEN SUBMITTED") # Redirect after POST
  else:
        form = testForm() # An unbound form
  venueOptions = Venue.objects.filter(building=building)
  #venueOptions1 = Venue.objects.filter(code=code)
  print venueOptions
  c = {'temp':venueOptions}#, 'temp1':venueOptions1}
  c.update(csrf(request))
  return render_to_response('search_form.html', c)
    
