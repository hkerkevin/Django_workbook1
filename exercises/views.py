# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero, Animal, Car, Employee, Stock, Credit_Card, Blog, Friend, Graffiti, Food, Contact, Athlete, Task, Ajax_Task
from django.urls import reverse
import json

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
    
    tasks = Ajax_Task.objects.all().order_by("-priority")
    
    completed_tasks = Ajax_Task.objects.filter(is_completed=True).order_by("-priority")

    incomplete_tasks = Ajax_Task.objects.filter(is_completed=False).order_by("-priority")
    
    context = { "completed_tasks": completed_tasks, "incomplete_tasks": incomplete_tasks }
    
    return render(request, "exercises/ajax_task_list.html", context)

def add_ajax_task(request):
    
    task = request.POST["task"]
    priority = request.POST["priority"]
    
    new_task = Ajax_Task.objects.create(item=task, priority=priority)
    
    return HttpResponseRedirect(reverse("exercises:ajax_task_list"))

def test(request):
    
    task = request.POST["task"]
    priority = request.POST["priority"]
    
    new_task = Ajax_Task.objects.create(item=task, priority=priority)
    
    completed_tasks = Ajax_Task.objects.filter(is_completed=True).order_by("-priority")
    
    incomplete_tasks = Ajax_Task.objects.filter(is_completed=False).order_by("-priority")
    
    context = { "completed_tasks": completed_tasks, "incomplete_tasks": incomplete_tasks }
    return render(request, "exercises/ajax_task_snippet.html", context)

def toggle_complete(request):
    
    task = Ajax_Task.objects.get(id = request.POST["id"])
    task.is_completed = not task.is_completed
    task.save()
    
    completed_tasks = Ajax_Task.objects.filter(is_completed=True).order_by("-priority")
    
    incomplete_tasks = Ajax_Task.objects.filter(is_completed=False).order_by("-priority")
    
    context = { "completed_tasks": completed_tasks, "incomplete_tasks": incomplete_tasks }
    return render(request, "exercises/ajax_task_snippet.html", context)

def calendar(request):
    
    return render(request, "exercises/calendar.html")

def fbview(request):
    data = [{"RegistrationOptions":None,"Sessions":None,"EventKey":"51d3a697-bcff-4cb9-90b6-ad786039002f","Address":{"Address1":"","Address2":"","Address3":"","AddressKey":"92cbdb40-8463-4bb3-a037-561538288fac","AddressType":"","City":"","CityStateCounty":"","CityStateCountyCountry":"","ContactKey":"00000000-0000-0000-0000-000000000000","CountryCode":"","CountryName":"","County":"","EmailAddress":"","FormattedAddress":"","FormattedAddressOneLine":"","FormattedAddressText":"","IsListCityState":False,"IsLoggingEnabled":True,"IsNew":False,"IsPreferredBill":False,"IsPreferredList":False,"IsPreferredMail":False,"ItemCreatedOn":"2018-04-26T14:55:13.557Z","ItemEntityName":"Address","ItemName":None,"ItemOwnerContactKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","Latitude":0,"LegacyAddressKey":"","Longitude":0,"NearText":"","Phone1":"","Phone1Type":"","Phone2":"","Phone2Type":"","Phone3":"","Phone3Type":"","Phone4":"","Phone4Type":"","PostalCode":"","Region":"","StateProvinceCode":"","TimeZoneKey":"ebd87123-3b99-40bc-a1bd-c10765f52d88","Town":"","TownOrCity":""},"ParticipationType":0,"DialInInstructions":"","EventURL":"","LoginInstructions":"","EventTitle":"test","ShortTitle":"test","EventTypeKey":"6a32f91a-0dcc-493d-b4a8-af6dec9222b1","EventType":{"EventTypeKey":"6a32f91a-0dcc-493d-b4a8-af6dec9222b1","EventTypeName":"Chapter Meeting","EventTypeDescription":"Chapter meetings support onlne registration and payment.  Member registration rates and early/late rates can also be established. Complex registrations are not supported.","AllowMultipleRegistrations":True,"AllowMultipleOptions":False,"AllowMultipleSessions":False,"AcceptPayment":True,"AcceptOfflinePayment":False,"IsActive":True,"AllowRegistration":True,"AllowSameSelections":False,"ShowAddEditScreenDescription":False,"AllowNonMemberRegistration":True,"AllowPublicUserRegistration":False,"AllowMultiPricesByDate":False,"AllowEarlyRegistrationRate":True,"AllowLateRegistrationRate":True,"AllowMultiPricesByRegistrantType":False,"AllowMemberNonMemberPricing":False,"AllowMultiPricesByRegistrantClass":False,"AddEditScreenDescription":"Enter Event Type description.  Specify the sort of options available for this event type, such as “Does not allow registration” or “Allows for registrations but not payments” or “Ideal for complex events.\"","HasPaymentProvider":True,"AllowMultiDay":True,"AllowPhysicalAddress":True,"AllowOnlinePhone":True,"AllowEventLogo":True,"AllowCommunityAdminToUse":True,"AllowCommunityMemberToUse":True,"AllowEventVisibilityChanges":True,"SuppressOptionDisplay":False,"SuppressSessionDisplay":False,"AllowCredits":True,"RegistrationProcessOption":1},"CommunityKey":"00000000-0000-0000-0000-000000000000","Community":None,"StartDateTime":"2018-04-26T14:53:00Z","StartDateTimeUTC":"2018-04-26T21:53:00Z","EndDateTime":"2018-07-12T14:53:00Z","EndDateTimeUTC":"2018-07-12T21:53:00Z","EndDateTimeCalculated":"2018-07-12T14:53:00Z","ArchiveDateTime":"0001-01-01T00:00:00Z","TimeZoneKey":"00000000-0000-0000-0000-000000000000","TimeZone":{"TimeZoneKey":"ebd87123-3b99-40bc-a1bd-c10765f52d88","TimeZoneDesc":"(UTC-8:00) America/Los_Angeles","GMTOffsetMinutes":-480,"IsDaylightSavings":True,"WindowsId":"Pacific Standard Time","Abbreviation":"PT"},"EventListDisplayType":3,"SearchResultsDisplayType":3,"ContactKey":"00000000-0000-0000-0000-000000000000","ContactFirstName":"","ContactFirstLast":None,"ContactLastName":"","ContactEmail":"","ContactPhone":"","EventDescription":"<p>If you are interested in presenting a case at one of the CCGCoP case conference sessions, please submit a GCRA Case Submission form by following the link below:</p>\n<ul>\n<li><strong>GCRA Case Submission Form</strong><span> </span>(complete<span> </span><strong><span>one form for each case</span></strong><span> </span>you wish to submit).\n<ol>\n<li>Link to form: <a href=\"https://redcap.coh.org/surveys/?s=wotp5q\">https://redcap.coh.org/surveys/?s=wotp5q</a></li>\n</ol>\n</li>\n</ul>\n<p>*<em>Note, the form asks you to upload an electronic copy (e.g., scanned, photo, etc) of your ANONYMIZED case pedigree (can be in any format, Progeny, neatly handwritten, etc) and genetic test results, if testing was done. This way you don't have to send them in an email. Everything is together in one form.</em></p>\n<ul>\n<li>AFTER you've presented your case, you can also link on to the following brief form so you can summarize the discussion and recommendations generated for your case:  <strong>GCRA Case Presentation Assessment</strong><span> </span>(best to complete  within 24 hours AFTER presenting a case – tracks most important learning points and case recommendations/follow up):\n<ol>\n<li>Link to form: <a href=\"https://redcap.coh.org/surveys/?s=fmAhCb\">https://redcap.coh.org/surveys/?s=fmAhCb</a></li>\n</ol>\n</li>\n</ul>\n<p><strong>IMPORTANT NOTE</strong>:  If you have questions about this new case submission process please contact Kathleen Blazer at<span> </span><a href=\"mailto:kblazer@coh.org\">kblazer@coh.org</a><span> </span>or Randy Lee at RanLee@coh.org . Thank you!</p>","PictureFileName":"","PictureUrl":"","PictureHeight":0,"PictureWidth":0,"RegistrationProcessOption":1,"RegRedirectURL":"","CurrencyType":None,"UseBadgeName":False,"UseDisabilityOrSpecial":False,"SpecialInstructions":False,"SpecialInstructionsLabelText":None,"EarlyRegistrationDate":"0001-01-01T00:00:00Z","RegularRegistrationDate":"0001-01-01T00:00:00Z","RegularRegistrationEndDate":"0001-01-01T00:00:00Z","LateRegistrationEndDate":"0001-01-01T00:00:00Z","SuppressSessionDisplay":False,"ShowPriceDetails":False,"LegacyEventKey":"","ConfirmationEmailText":"","DetailURL":"","EventTypeName":"Chapter Meeting","FormatedDateRange":"Apr 26 - Jul 12, (PT)","FormatedDateRangeLong":"Thursday, April 26 - Thursday, July 12, 2018","FormatedDateRangeLongMonth":"April 26 - July 12, (PT)","FormatedDateRangeYear":"Apr 26 - Jul 12, 2018, (PT)","HasPricing":False,"ICalendarData":"BEGIN:VCALENDAR\r\nVERSION:2.0\r\nMETHOD:PUBLISH\r\nPRODID:-//HigherLogic//Calendar1.0.0.0//EN\r\nX-MS-OLK-FORCEINSPECTOROPEN:TRUE\r\nBEGIN:VTIMEZONE\r\nTZID:America/Los_Angeles\r\nBEGIN:STANDARD\r\nDTSTART:20070101T020000\r\nRRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=1SU;BYMONTH=11\r\nTZOFFSETFROM:-0700\r\nTZOFFSETTO:-0800\r\nEND:STANDARD\r\nBEGIN:DAYLIGHT\r\nDTSTART:20070101T020000\r\nRRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=2SU;BYMONTH=3\r\nTZOFFSETFROM:-0800\r\nTZOFFSETTO:-0700\r\nEND:DAYLIGHT\r\nEND:VTIMEZONE\r\nBEGIN:VEVENT\r\nDESCRIPTION: If you are interested in presenting a case at one of the CCGCo\r\n P case conference sessions, please submit a GCRA Case Submission form by f\r\n ollowing the link below: \\n \\n  GCRA Case Submission Form    (complete    \r\n  one form for each case     you wish to submit).\\n \\n Link to form:  https\r\n ://redcap.coh.org/surveys/?s=wotp5q  \\n \\n \\n \\n * Note, the form asks you\r\n  to upload an electronic copy (e.g., scanned, photo, etc) of your ANONYMIZ\r\n ED case pedigree (can be in any format, Progeny, neatly handwritten, etc) \r\n and genetic test results, if testing was done. This way you don't have to \r\n send them in an email. Everything is together in one form.  \\n \\n AFTER yo\r\n u've presented your case, you can also link on to the following brief form\r\n  so you can summarize the discussion and recommendations generated for you\r\n r case:   GCRA Case Presentation Assessment    (best to complete  within 2\r\n 4 hours AFTER presenting a case – tracks most important learning points an\r\n d case recommendations/follow up):\\n \\n Link to form:  https://redcap.coh.\r\n org/surveys/?s=fmAhCb  \\n \\n \\n \\n  IMPORTANT NOTE :  If you have question\r\n s about this new case submission process please contact Kathleen Blazer at\r\n     kblazer@coh.org    or Randy Lee at RanLee@coh.org . Thank you! \\n\\nVie\r\n w Event: https://testcommunity.ccgcop.org/events/event-description?Calenda\r\n rEventKey=51d3a697-bcff-4cb9-90b6-ad786039002f&Home=%2fapi%2fv2.0%2fEvents\r\n %2fGetUpcoming\r\nUID:51D3A697BCFF4CB990B6AD786039002FHLCCGCOP\r\n\r\nSUMMARY:test\r\nDTSTART;TZID=America/Los_Angeles:20180426T145300\r\nDTEND;TZID=America/Los_Angeles:20180712T145300\r\nCLASS:PUBLIC\r\nPRIORITY:5\r\nDTSTAMP:20180426T145513Z\r\nTRANSP:OPAQUE\r\nSTATUS:CONFIRMED\r\nSEQUENCE:0\r\nLOCATION:Not specified\r\nURL:https://testcommunity.ccgcop.org/events/event-description?CalendarEvent\r\n Key=51d3a697-bcff-4cb9-90b6-ad786039002f&Home=%2fapi%2fv2.0%2fEvents%2fGet\r\n Upcoming\r\nX-ALT-DESC;FMTTYPE=text/html:<p>If you are interested in presenting a case \r\n at one of the CCGCoP case conference sessions, please submit a GCRA Case S\r\n ubmission form by following the link below:</p>\\n<br/><ul>\\n<br/><li><stro\r\n ng>GCRA Case Submission Form</strong><span> </span>(complete<span> </span>\r\n <strong><span>one form for each case</span></strong><span> </span>you wish\r\n  to submit).\\n<br/><ol>\\n<br/><li>Link to form: <a href=\"https://redcap.co\r\n h.org/surveys/?s=wotp5q\">https://redcap.coh.org/surveys/?s=wotp5q</a></li>\r\n \\n<br/></ol>\\n<br/></li>\\n<br/></ul>\\n<br/><p>*<em>Note, the form asks you\r\n  to upload an electronic copy (e.g., scanned, photo, etc) of your ANONYMIZ\r\n ED case pedigree (can be in any format, Progeny, neatly handwritten, etc) \r\n and genetic test results, if testing was done. This way you don't have to \r\n send them in an email. Everything is together in one form.</em></p>\\n<br/>\r\n <ul>\\n<br/><li>AFTER you've presented your case, you can also link on to t\r\n he following brief form so you can summarize the discussion and recommenda\r\n tions generated for your case:  <strong>GCRA Case Presentation Assessment<\r\n /strong><span> </span>(best to complete  within 24 hours AFTER presenting \r\n a case – tracks most important learning points and case recommendations/fo\r\n llow up):\\n<br/><ol>\\n<br/><li>Link to form: <a href=\"https://redcap.coh.o\r\n rg/surveys/?s=fmAhCb\">https://redcap.coh.org/surveys/?s=fmAhCb</a></li>\\n<\r\n br/></ol>\\n<br/></li>\\n<br/></ul>\\n<br/><p><strong>IMPORTANT NOTE</strong>\r\n :  If you have questions about this new case submission process please con\r\n tact Kathleen Blazer at<span> </span><a href=\"mailto:kblazer@coh.org\">kbla\r\n zer@coh.org</a><span> </span>or Randy Lee at RanLee@coh.org . Thank you!</\r\n p>\\n<br/>\\n<br/>View Event: <a href=\"https://testcommunity.ccgcop.org/even\r\n ts/event-description?CalendarEventKey=51d3a697-bcff-4cb9-90b6-ad786039002f\r\n &Home=%2fapi%2fv2.0%2fEvents%2fGetUpcoming\">test</a>\r\nBEGIN:VALARM\r\nTRIGGER:-PT15M\r\nACTION:DISPLAY\r\nDESCRIPTION:Reminder\r\nEND:VALARM\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n","IsAcceptingRegistrations":False,"IsActive":True,"IsReadyForRegistration":False,"LinkToEventDetails":"https://testcommunity.ccgcop.org/events/event-description?CalendarEventKey=51d3a697-bcff-4cb9-90b6-ad786039002f&Home=%2fapi%2fv2.0%2fEvents%2fGetUpcoming","MemberFee":0,"NonMemberFee":0,"RegistrantCount":0,"RegThankyouMessage":"","SuppressOptionDisplay":False,"UseForm":False,"CreatedByUser":"","CreatedByUserKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","CreatedOn":"2018-04-26T14:55:13.62Z","UpdatedByUser":"","UpdatedByUserKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","UpdatedOn":"2018-04-26T14:55:13.62Z"},{"RegistrationOptions":None,"Sessions":None,"EventKey":"026c7d6e-7fc1-4a01-874f-a10445beaa5f","Address":{"Address1":"","Address2":"","Address3":"","AddressKey":"81f1862d-4c67-41d1-9708-e5af7831f945","AddressType":"","City":"","CityStateCounty":"","CityStateCountyCountry":"","ContactKey":"00000000-0000-0000-0000-000000000000","CountryCode":"","CountryName":"","County":"","EmailAddress":"","FormattedAddress":"","FormattedAddressOneLine":"","FormattedAddressText":"","IsListCityState":False,"IsLoggingEnabled":True,"IsNew":False,"IsPreferredBill":False,"IsPreferredList":False,"IsPreferredMail":False,"ItemCreatedOn":"2018-07-02T23:29:47.377Z","ItemEntityName":"Address","ItemName":None,"ItemOwnerContactKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","Latitude":0,"LegacyAddressKey":"","Longitude":0,"NearText":"","Phone1":"","Phone1Type":"","Phone2":"","Phone2Type":"","Phone3":"","Phone3Type":"","Phone4":"","Phone4Type":"","PostalCode":"","Region":"","StateProvinceCode":"","TimeZoneKey":"ebd87123-3b99-40bc-a1bd-c10765f52d88","Town":"","TownOrCity":""},"ParticipationType":0,"DialInInstructions":"","EventURL":"","LoginInstructions":"","EventTitle":"Test 2","ShortTitle":"Test 2","EventTypeKey":"87c93176-886b-4189-8569-5c125949d188","EventType":{"EventTypeKey":"87c93176-886b-4189-8569-5c125949d188","EventTypeName":"Professional Development","EventTypeDescription":"The Professional Development Event Type supports special pricing for kinds of users/members, multiple sessions and additional options to be purchased at registration.  It does not support the registration of multiple people by one user.","AllowMultipleRegistrations":True,"AllowMultipleOptions":True,"AllowMultipleSessions":True,"AcceptPayment":True,"AcceptOfflinePayment":False,"IsActive":True,"AllowRegistration":True,"AllowSameSelections":False,"ShowAddEditScreenDescription":True,"AllowNonMemberRegistration":False,"AllowPublicUserRegistration":True,"AllowMultiPricesByDate":False,"AllowEarlyRegistrationRate":True,"AllowLateRegistrationRate":True,"AllowMultiPricesByRegistrantType":False,"AllowMemberNonMemberPricing":False,"AllowMultiPricesByRegistrantClass":False,"AddEditScreenDescription":"Enter Event Type description.  Specify the sort of options available for this event type, such as “Does not allow registration” or “Allows for registrations but not payments” or “Ideal for complex events.\"","HasPaymentProvider":True,"AllowMultiDay":True,"AllowPhysicalAddress":True,"AllowOnlinePhone":True,"AllowEventLogo":True,"AllowCommunityAdminToUse":True,"AllowCommunityMemberToUse":True,"AllowEventVisibilityChanges":True,"SuppressOptionDisplay":False,"SuppressSessionDisplay":False,"AllowCredits":True,"RegistrationProcessOption":1},"CommunityKey":"00000000-0000-0000-0000-000000000000","Community":None,"StartDateTime":"2018-07-02T23:28:00Z","StartDateTimeUTC":"2018-07-03T06:28:00Z","EndDateTime":"2018-07-31T23:28:00Z","EndDateTimeUTC":"2018-08-01T06:28:00Z","EndDateTimeCalculated":"2018-07-31T23:28:00Z","ArchiveDateTime":"0001-01-01T00:00:00Z","TimeZoneKey":"00000000-0000-0000-0000-000000000000","TimeZone":{"TimeZoneKey":"ebd87123-3b99-40bc-a1bd-c10765f52d88","TimeZoneDesc":"(UTC-8:00) America/Los_Angeles","GMTOffsetMinutes":-480,"IsDaylightSavings":True,"WindowsId":"Pacific Standard Time","Abbreviation":"PT"},"EventListDisplayType":2,"SearchResultsDisplayType":2,"ContactKey":"00000000-0000-0000-0000-000000000000","ContactFirstName":"","ContactFirstLast":None,"ContactLastName":"","ContactEmail":"","ContactPhone":"","EventDescription":"Test 2","PictureFileName":"","PictureUrl":"","PictureHeight":0,"PictureWidth":0,"RegistrationProcessOption":1,"RegRedirectURL":"","CurrencyType":None,"UseBadgeName":False,"UseDisabilityOrSpecial":False,"SpecialInstructions":False,"SpecialInstructionsLabelText":None,"EarlyRegistrationDate":"0001-01-01T00:00:00Z","RegularRegistrationDate":"0001-01-01T00:00:00Z","RegularRegistrationEndDate":"0001-01-01T00:00:00Z","LateRegistrationEndDate":"0001-01-01T00:00:00Z","SuppressSessionDisplay":False,"ShowPriceDetails":False,"LegacyEventKey":"","ConfirmationEmailText":"","DetailURL":"","EventTypeName":"Professional Development","FormatedDateRange":"Jul 2 - 31, (PT)","FormatedDateRangeLong":"Monday, July 2 - Tuesday, July 31, 2018","FormatedDateRangeLongMonth":"July 2 - 31, (PT)","FormatedDateRangeYear":"Jul 2 - 31, 2018, (PT)","HasPricing":False,"ICalendarData":"BEGIN:VCALENDAR\r\nVERSION:2.0\r\nMETHOD:PUBLISH\r\nPRODID:-//HigherLogic//Calendar1.0.0.0//EN\r\nX-MS-OLK-FORCEINSPECTOROPEN:TRUE\r\nBEGIN:VTIMEZONE\r\nTZID:America/Los_Angeles\r\nBEGIN:STANDARD\r\nDTSTART:20070101T020000\r\nRRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=1SU;BYMONTH=11\r\nTZOFFSETFROM:-0700\r\nTZOFFSETTO:-0800\r\nEND:STANDARD\r\nBEGIN:DAYLIGHT\r\nDTSTART:20070101T020000\r\nRRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=2SU;BYMONTH=3\r\nTZOFFSETFROM:-0800\r\nTZOFFSETTO:-0700\r\nEND:DAYLIGHT\r\nEND:VTIMEZONE\r\nBEGIN:VEVENT\r\nDESCRIPTION:Test 2\\n\\nView Event: https://testcommunity.ccgcop.org/events/e\r\n vent-description?CalendarEventKey=026c7d6e-7fc1-4a01-874f-a10445beaa5f&Hom\r\n e=%2fapi%2fv2.0%2fEvents%2fGetUpcoming\r\nUID:026C7D6E7FC14A01874FA10445BEAA5FHLCCGCOP\r\n\r\nSUMMARY:Test 2\r\nDTSTART;TZID=America/Los_Angeles:20180702T232800\r\nDTEND;TZID=America/Los_Angeles:20180731T232800\r\nCLASS:PUBLIC\r\nPRIORITY:5\r\nDTSTAMP:20180702T232947Z\r\nTRANSP:OPAQUE\r\nSTATUS:CONFIRMED\r\nSEQUENCE:0\r\nLOCATION:Not specified\r\nURL:https://testcommunity.ccgcop.org/events/event-description?CalendarEvent\r\n Key=026c7d6e-7fc1-4a01-874f-a10445beaa5f&Home=%2fapi%2fv2.0%2fEvents%2fGet\r\n Upcoming\r\nX-ALT-DESC;FMTTYPE=text/html:Test 2\\n<br/>\\n<br/>View Event: <a href=\"https\r\n ://testcommunity.ccgcop.org/events/event-description?CalendarEventKey=026c\r\n 7d6e-7fc1-4a01-874f-a10445beaa5f&Home=%2fapi%2fv2.0%2fEvents%2fGetUpcoming\r\n \">Test 2</a>\r\nBEGIN:VALARM\r\nTRIGGER:-PT15M\r\nACTION:DISPLAY\r\nDESCRIPTION:Reminder\r\nEND:VALARM\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n","IsAcceptingRegistrations":False,"IsActive":True,"IsReadyForRegistration":False,"LinkToEventDetails":"https://testcommunity.ccgcop.org/events/event-description?CalendarEventKey=026c7d6e-7fc1-4a01-874f-a10445beaa5f&Home=%2fapi%2fv2.0%2fEvents%2fGetUpcoming","MemberFee":0,"NonMemberFee":0,"RegistrantCount":0,"RegThankyouMessage":"","SuppressOptionDisplay":False,"UseForm":False,"CreatedByUser":"","CreatedByUserKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","CreatedOn":"2018-07-02T23:29:47.457Z","UpdatedByUser":"","UpdatedByUserKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","UpdatedOn":"2018-07-02T23:29:47.457Z"},{"RegistrationOptions":None,"Sessions":None,"EventKey":"51662eb3-42e0-4d86-a80d-90bfec1c3651","Address":{"Address1":"","Address2":"","Address3":"","AddressKey":"8cfd01f3-194c-4f5b-9bcf-8d3e0da10eca","AddressType":"","City":"","CityStateCounty":"","CityStateCountyCountry":"","ContactKey":"00000000-0000-0000-0000-000000000000","CountryCode":"","CountryName":"","County":"","EmailAddress":"","FormattedAddress":"","FormattedAddressOneLine":"","FormattedAddressText":"","IsListCityState":False,"IsLoggingEnabled":True,"IsNew":False,"IsPreferredBill":False,"IsPreferredList":False,"IsPreferredMail":False,"ItemCreatedOn":"2018-07-02T23:30:18.307Z","ItemEntityName":"Address","ItemName":None,"ItemOwnerContactKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","Latitude":0,"LegacyAddressKey":"","Longitude":0,"NearText":"","Phone1":"","Phone1Type":"","Phone2":"","Phone2Type":"","Phone3":"","Phone3Type":"","Phone4":"","Phone4Type":"","PostalCode":"","Region":"","StateProvinceCode":"","TimeZoneKey":"ebd87123-3b99-40bc-a1bd-c10765f52d88","Town":"","TownOrCity":""},"ParticipationType":0,"DialInInstructions":"","EventURL":"","LoginInstructions":"","EventTitle":"Test 3","ShortTitle":"Test 3","EventTypeKey":"f141d1da-5e07-43a7-b959-13ab88bba9ac","EventType":{"EventTypeKey":"f141d1da-5e07-43a7-b959-13ab88bba9ac","EventTypeName":"Committee Meeting","EventTypeDescription":"Committee Meetings allow for multiple tracks and sessions, but do not allow for payments to be collected online.","AllowMultipleRegistrations":True,"AllowMultipleOptions":False,"AllowMultipleSessions":True,"AcceptPayment":False,"AcceptOfflinePayment":False,"IsActive":True,"AllowRegistration":True,"AllowSameSelections":False,"ShowAddEditScreenDescription":False,"AllowNonMemberRegistration":False,"AllowPublicUserRegistration":True,"AllowMultiPricesByDate":False,"AllowEarlyRegistrationRate":False,"AllowLateRegistrationRate":False,"AllowMultiPricesByRegistrantType":False,"AllowMemberNonMemberPricing":False,"AllowMultiPricesByRegistrantClass":False,"AddEditScreenDescription":"Enter Event Type description.  Specify the sort of options available for this event type, such as “Does not allow registration” or “Allows for registrations but not payments” or “Ideal for complex events.\"","HasPaymentProvider":True,"AllowMultiDay":True,"AllowPhysicalAddress":True,"AllowOnlinePhone":True,"AllowEventLogo":True,"AllowCommunityAdminToUse":True,"AllowCommunityMemberToUse":True,"AllowEventVisibilityChanges":True,"SuppressOptionDisplay":False,"SuppressSessionDisplay":False,"AllowCredits":True,"RegistrationProcessOption":1},"CommunityKey":"00000000-0000-0000-0000-000000000000","Community":None,"StartDateTime":"2018-07-02T23:30:00Z","StartDateTimeUTC":"2018-07-03T06:30:00Z","EndDateTime":"2018-08-22T23:30:00Z","EndDateTimeUTC":"2018-08-23T06:30:00Z","EndDateTimeCalculated":"2018-08-22T23:30:00Z","ArchiveDateTime":"0001-01-01T00:00:00Z","TimeZoneKey":"00000000-0000-0000-0000-000000000000","TimeZone":{"TimeZoneKey":"ebd87123-3b99-40bc-a1bd-c10765f52d88","TimeZoneDesc":"(UTC-8:00) America/Los_Angeles","GMTOffsetMinutes":-480,"IsDaylightSavings":True,"WindowsId":"Pacific Standard Time","Abbreviation":"PT"},"EventListDisplayType":2,"SearchResultsDisplayType":2,"ContactKey":"00000000-0000-0000-0000-000000000000","ContactFirstName":"","ContactFirstLast":None,"ContactLastName":"","ContactEmail":"","ContactPhone":"","EventDescription":"Test 3","PictureFileName":"","PictureUrl":"","PictureHeight":0,"PictureWidth":0,"RegistrationProcessOption":1,"RegRedirectURL":"","CurrencyType":None,"UseBadgeName":False,"UseDisabilityOrSpecial":False,"SpecialInstructions":False,"SpecialInstructionsLabelText":None,"EarlyRegistrationDate":"0001-01-01T00:00:00Z","RegularRegistrationDate":"0001-01-01T00:00:00Z","RegularRegistrationEndDate":"0001-01-01T00:00:00Z","LateRegistrationEndDate":"0001-01-01T00:00:00Z","SuppressSessionDisplay":False,"ShowPriceDetails":False,"LegacyEventKey":"","ConfirmationEmailText":"","DetailURL":"","EventTypeName":"Committee Meeting","FormatedDateRange":"Jul 2 - Aug 22, (PT)","FormatedDateRangeLong":"Monday, July 2 - Wednesday, August 22, 2018","FormatedDateRangeLongMonth":"July 2 - August 22, (PT)","FormatedDateRangeYear":"Jul 2 - Aug 22, 2018, (PT)","HasPricing":False,"ICalendarData":"BEGIN:VCALENDAR\r\nVERSION:2.0\r\nMETHOD:PUBLISH\r\nPRODID:-//HigherLogic//Calendar1.0.0.0//EN\r\nX-MS-OLK-FORCEINSPECTOROPEN:TRUE\r\nBEGIN:VTIMEZONE\r\nTZID:America/Los_Angeles\r\nBEGIN:STANDARD\r\nDTSTART:20070101T020000\r\nRRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=1SU;BYMONTH=11\r\nTZOFFSETFROM:-0700\r\nTZOFFSETTO:-0800\r\nEND:STANDARD\r\nBEGIN:DAYLIGHT\r\nDTSTART:20070101T020000\r\nRRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=2SU;BYMONTH=3\r\nTZOFFSETFROM:-0800\r\nTZOFFSETTO:-0700\r\nEND:DAYLIGHT\r\nEND:VTIMEZONE\r\nBEGIN:VEVENT\r\nDESCRIPTION:Test 3\\n\\nView Event: https://testcommunity.ccgcop.org/events/e\r\n vent-description?CalendarEventKey=51662eb3-42e0-4d86-a80d-90bfec1c3651&Hom\r\n e=%2fapi%2fv2.0%2fEvents%2fGetUpcoming\r\nUID:51662EB342E04D86A80D90BFEC1C3651HLCCGCOP\r\n\r\nSUMMARY:Test 3\r\nDTSTART;TZID=America/Los_Angeles:20180702T233000\r\nDTEND;TZID=America/Los_Angeles:20180822T233000\r\nCLASS:PUBLIC\r\nPRIORITY:5\r\nDTSTAMP:20180702T233018Z\r\nTRANSP:OPAQUE\r\nSTATUS:CONFIRMED\r\nSEQUENCE:0\r\nLOCATION:Not specified\r\nURL:https://testcommunity.ccgcop.org/events/event-description?CalendarEvent\r\n Key=51662eb3-42e0-4d86-a80d-90bfec1c3651&Home=%2fapi%2fv2.0%2fEvents%2fGet\r\n Upcoming\r\nX-ALT-DESC;FMTTYPE=text/html:Test 3\\n<br/>\\n<br/>View Event: <a href=\"https\r\n ://testcommunity.ccgcop.org/events/event-description?CalendarEventKey=5166\r\n 2eb3-42e0-4d86-a80d-90bfec1c3651&Home=%2fapi%2fv2.0%2fEvents%2fGetUpcoming\r\n \">Test 3</a>\r\nBEGIN:VALARM\r\nTRIGGER:-PT15M\r\nACTION:DISPLAY\r\nDESCRIPTION:Reminder\r\nEND:VALARM\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n","IsAcceptingRegistrations":False,"IsActive":True,"IsReadyForRegistration":False,"LinkToEventDetails":"https://testcommunity.ccgcop.org/events/event-description?CalendarEventKey=51662eb3-42e0-4d86-a80d-90bfec1c3651&Home=%2fapi%2fv2.0%2fEvents%2fGetUpcoming","MemberFee":0,"NonMemberFee":0,"RegistrantCount":0,"RegThankyouMessage":"","SuppressOptionDisplay":False,"UseForm":False,"CreatedByUser":"","CreatedByUserKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","CreatedOn":"2018-07-02T23:30:18.327Z","UpdatedByUser":"","UpdatedByUserKey":"5222c306-1fb6-410b-8deb-70dc33b39c84","UpdatedOn":"2018-07-02T23:30:18.327Z"}]
    return HttpResponse(json.dumps(data), content_type='application/json')