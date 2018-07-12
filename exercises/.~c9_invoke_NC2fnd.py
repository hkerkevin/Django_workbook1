# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero, Animal, Car, Employee, Stock, Credit_Card, Blog, Friend, Graffiti, Food, Contact, Athlete, Task, Ajax_Task
from django.urls import reverse


# Create your views here.
def superheroes(request):
    
    # code below!
    superheroes = Superhero.objects.filter(is_good=True).filter(is_male = True).filter(name__contains = 'e')
    
    context = { 'superheroes': superheroes }
    return render(request, 'exercises/superhero.html', context)       


def animals(request):
    animals = None
    
    # code below!
    animals = Animal.objects.all()
    
    context = { 'animals': animals }
    return render(request, 'exercises/animal.html', context)       

def cars(request):
    cars = None
    
    # code below!
    cars = Car.objects.filter(make = "toyota").filter(year__gte = 1995).order_by("-model")
    
    context = { 'cars': cars }
    return render(request, 'exercises/car.html', context)  

def templates(request):
    
    superheroes = Superhero.objects.filter(is_male=False).filter(rating__gte=7)
    animals = Animal.objects.filter(name__startswith="g").order_by("-name")
    cars = Car.objects.filter(year__gte=2010)
    
    context = { 'superheroes': superheroes, 'animals': animals, 'cars': cars  }
    return render(request, 'exercises/template.html', context)       

def summary(request):
    
    employees = Employee.objects.order_by("-salary")[:5]
    
    context = { 'employees': employees }
    return render(request, 'exercises/summary.html', context)       
    

def submit_form(request):
    context = { }
    return render(request, "exercises/submit_form.html", context)
    
def team_edward(request):
    return HttpResponse(request.POST['message'] + " is a fervent supporter of team edward")
    
def team_jacob(request):
    return HttpResponse(request.GET['first_name'] + " " + request.GET['last_name'] + " is a member of team jacob. ROAR!!")

def create_page(request):
    return HttpResponse("hello you")

def forrest_gump(request):
    return HttpResponse("life is like a box of chocolates.")
    
def wizard_of_oz(request):
    context = { }
    return render(request, 'exercises/wizard_of_oz.html', context)

def the_godfather(request):
    return HttpResponse("I'm gonna make him an offer he can't refuse.")

def casablanca(request):
    context = { }
    return render(request, 'exercises/casablanca.html', context)

def stocks(request):
    
    stocks = Stock.objects.order_by("-market_cap")[:5]
    
    context = { 'stocks': stocks }
    return render(request, 'exercises/stocks.html', context)

def credit_cards(request):
     
    credit_cards = Credit_Card.objects.all()
    
    context = { 'credit_cards': credit_cards }
    return render(request, 'exercises/credit_cards.html', context)

def my_new_template(request):
    
    context = { 'my_new_template': my_new_template }
    return render(request, 'exercises/my_new_template.html', context)

def animals_new(request):
    
    animals_new = Animal.objects.all()
    
    context = { 'animals_new': animals_new }
    return render(request, 'exercises/animals_new.html', context)

def cc(request, id):
    
    cc = Credit_Card.objects.get(id=id)
    
    context = { 'cc': cc }
    return render(request, 'exercises/cc.html', context)

def new_page(request):
    
    context = { 'new_page': new_page }
    return render(request, 'exercises/new_page.html', context)

def blog(request):
    
    blog = Blog.objects.all()
    
    context = { 'blog': blog }
    return render(request, 'exercises/blog.html', context)

def blog_details(request, id):
    
    blog_details = Blog.objects.get(id=id)
    
    context = { 'blog_details': blog_details }
    return render(request, 'exercises/blog_details.html', context)
    
def bert(request):
    
    context = { 'bert': bert }
    return render(request, 'exercises/bert.html', context)

def ernie(request):
    return HttpResponse(request.POST['body_text'])

def pumba(request):
    animal_name = request.POST['animal_name']
    animals = Animal.objects.filter(name__startswith=animal_name)
    
    context = { 'animals': animals }
    return render(request, "exercises/pumba.html", context)

def timon(request):
    
    context = { }
    return render(request, "exercises/timon.html", context)
    
def hero_search(request):
    
    context = { }
    return render(request, "exercises/hero_search.html", context)

def hero_results(request):
    
    superhero_name = request.POST['superhero_name']
    superheroes = Superhero.objects.filter(name__startswith=superhero_name)
    num = len(superheroes)
    
    context = { 'superheroes': superheroes, 'num': num, 'superhero_name': superhero_name}
    return render(request, "exercises/hero_results.html", context)
    
def hero_details(request, id):
    
    hero_details = Superhero.objects.get(id=id)
    
    context = { 'superhero': hero_details }
    return render(request, "exercises/hero_details.html", context)

def friend_list(request):
    
    all_friends = Friend.objects.all()
    
    context = { 'all_friends': all_friends }
    return render(request, "exercises/friend_list.html", context)

def friend_save(request):
    friend_name = request.POST["name"]
    friend = Friend.objects.create(name=friend_name)
   
    return HttpResponseRedirect(reverse('exercises:friend_list'))

def delete_friend(request, id):
    
    friend = Friend.objects.get(id=id)
    friend.delete()
    
    return HttpResponseRedirect(reverse("exercises:friend_list"))
   
def graffiti(request):
    
    all_graffiti = Graffiti.objects.all()
    
    context = { 'all_graffiti': all_graffiti }
    return render(request, "exercises/graffiti.html", context)

def graffiti_save(request):
    graffiti_message = request.POST["message"]
    graffiti_author = request.POST["author"]
    
    graffiti = Graffiti.objects.create(message=graffiti_message, author=graffiti_author)
   
    return HttpResponseRedirect(reverse('exercises:graffiti'))

def food_list(request):
    
    all_food = Food.objects.all()
    
    context = { "all_food" : all_food }
    return render(request, "exercises/food_list.html", context)

def food_save(request):
    
    food_name = request.POST["name"]
    food = Food.objects.create(name=food_name)
    
    return HttpResponseRedirect(reverse('exercises:food_list'))

def edit_food(request, id):
    
    edit_food = Food.objects.get(id=id)
    
    context = { 'edit_food': edit_food }
    return render(request, "exercises/edit_food.html", context)

def edit_food_save(request, id):
    
    edit_food = Food.objects.get(id=id)
    update = request.POST["edit_food"]
    edit_food.name = update
    edit_food.save()
    
    return HttpResponseRedirect(reverse('exercises:food_list'))

def phone_book(request):
    
    if "q" in request.GET:
        contacts = Contact.objects.filter(name__istartswith=request.GET["q"]).order_by("name")
        search = request.GET['q']
    else:
        contacts = Contact.objects.all().order_by("name")
        search =""
        
    context = { "contacts" : contacts, "search": search }
    return render(request, "exercises/phone_book.html", context)

def add_phone(request):
    
    context = { }
    return render(request, "exercises/add_phone.html", context)
    
def phone_book_save(request):
    
    contact_name = request.POST["name"]
    contact_phone = request.POST["phone"]
    contact_address = request.POST["address"]
    
    contact = Contact.objects.create(name=contact_name, phone=contact_phone, address=contact_address)
    
    return HttpResponseRedirect(reverse('exercises:phone_book'))

def edit_phone(request, id):
    
    edit_phone = Contact.objects.get(id=id)
    
    context = { "edit_phone": edit_phone }
    return render(request, "exercises/edit_phone.html", context)

def edit_phone_save(request, id):
    
    edit_phone = Contact.objects.get(id=id)
    update_name = request.POST["name"]
    update_phone = request.POST["phone"]
    update_address = request.POST["address"]
    
    edit_phone.name = update_name
    edit_phone.phone = update_phone
    edit_phone.address = update_address
    edit_phone.save()
    
    return HttpResponseRedirect(reverse('exercises:phone_book'))

def details_phone(request, id):
    
    details_phone = Contact.objects.get(id=id)
    
    context = { "details_phone" : details_phone }
    return render(request, "exercises/details_phone.html", context)

def athlete_list(request):
    
    all_athletes = Athlete.objects.all().order_by("sport", "name")
    
    context = { "all_athletes" : all_athletes }
    return render(request, "exercises/athlete_list.html", context)
    
def add_athlete(request):
    
    athlete_name = request.POST["name"]
    athlete_sport = request.POST["sport"]
    
    Athlete.objects.create(name=athlete_name, sport=athlete_sport)
    
    return HttpResponseRedirect(reverse("exercises:athlete_list"))

def delete_athlete(request, athlete_id):
    
    athlete = Athlete.objects.get(id=athlete_id)
    athlete.delete()
    
    return HttpResponseRedirect(reverse("exercises:athlete_list"))

def task_list(request):
    
    if "q" in request.GET:
        if request.GET["q"] == "":
            completed_tasks = Task.objects.filter(item__istartswith=request.GET["q"]).filter(priority=request.GET["priority"]).filter(is_completed=True).order_by("-priority")
            incomplete_tasks = Task.objects.filter(item__istartswith=request.GET["q"]).filter(priority=request.GET["priority"]).filter(is_completed=False).order_by("-priority")
            search = request.GET['q']
            priority = int(request.GET['priority'])
        elif request.GET["priority"] == "0":
            completed_tasks = Task.objects.filter(item__istartswith=request.GET["q"]).filter(is_completed=True).order_by("-priority")
            incomplete_tasks = Task.objects.filter(item__istartswith=request.GET["q"]).filter(is_completed=False).order_by("-priority")
            search = request.GET['q']
            priority = int(request.GET['priority'])
        else:
            completed_tasks = Task.objects.filter(item__istartswith=request.GET["q"]).filter(priority=request.GET["priority"]).filter(is_completed=True).order_by("-priority")
            incomplete_tasks = Task.objects.filter(item__istartswith=request.GET["q"]).filter(priority=request.GET["priority"]).filter(is_completed=False).order_by("-priority")
            search = request.GET['q']
            priority = int(request.GET['priority'])
    else:
        completed_tasks = Task.objects.filter(is_completed=True).order_by("-priority")
        incomplete_tasks = Task.objects.filter(is_completed=False).order_by("-priority")
        search = ""
        priority = ""
    
    context = {  "completed_tasks" : completed_tasks, "incomplete_tasks" : incomplete_tasks , "search": search , "priority": priority}
    return render(request, "exercises/task_list.html", context)

def delete_task(request, task_id):
    
    task = Task.objects.get(id=task_id)
    task.delete()
    
    return HttpResponseRedirect(reverse("exercises:task_list"))

def add_task(request):
    
    task_item = request.POST["task"]
    task_priority = request.POST["priority"]
    
    task = Task.objects.create(item=task_item, priority=task_priority)
    
    return HttpResponseRedirect(reverse("exercises:task_list"))

def update_task(request, task_id):
    
    task = Task.objects.get(id=task_id)
    
    if task.is_completed == True:
        task.is_completed = False
    else:
        task.is_completed = True
    
    task.save()
    return HttpResponseRedirect(reverse("exercises:task_list"))

def edit_task(request, task_id):
    
    task = Task.objects.get(id=task_id)
    
    context = { "task" : task }
    return render(request, "exercises/edit_task.html", context)
    
def edit_task_save(request, task_id):
    
    task = Task.objects.get(id=task_id)
    update_item = request.POST["task"]
    update_priority = request.POST["priority"]
    
    task.item = update_item
    task.priority = update_priority
    task.save()
    
    return HttpResponseRedirect(reverse("exercises:task_list"))

def ajax_task_list(request):
    
    tasks = Ajax_Task.objects.all()
    
    context = { "tasks" : tasks }
    
    return render(request, "exercises/ajax_task_list.html")

def add_a