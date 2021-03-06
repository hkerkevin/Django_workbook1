from django.core.management.base import BaseCommand, CommandError
from exercises.models import *
from exercises.data import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        #Populate data to Supehero
        Superhero.objects.all().delete()
        
        for obj in superhero_data:
            Superhero.objects.create(name=obj['fields']['name'], superpower=obj['fields']['superpower'],
                                        is_good=obj['fields']['is_good'], is_male=obj['fields']['is_male'], 
                                        rating=obj['fields']['rating'], age=obj['fields']['age'])
        
        #Populate data to Animal
        Animal.objects.all().delete()
        
        for obj in animal_data:
            Animal.objects.create(name=obj['fields']['name'], birthplace=obj['fields']['birthplace'],
                                        is_male=obj['fields']['is_male'])
        

        #Populate data to Car
        Car.objects.all().delete()
        
        for obj in car_data:
            Car.objects.create(make=obj['fields']['make'], model=obj['fields']['model'],
                                        year=obj['fields']['year'])
        
        
        
        #Populate data to Stock
        Stock.objects.all().delete()
        
        for obj in stock_data:
            Stock.objects.create(company=obj['fields']['company'], sector=obj['fields']['sector'],
                                        market_cap=obj['fields']['market_cap'])
        
    
        #Populate data to Message
        Message.objects.all().delete()
        
        for obj in message_data:
            Message.objects.create(text=obj['fields']['text'], is_hidden=obj['fields']['is_hidden'])
        
        
        #Populate data to Employee
        Employee.objects.all().delete()
        
        for obj in employee_data:
            Employee.objects.create(employee=obj['fields']['employee'], department=obj['fields']['department'],
                                    salary=obj['fields']['salary'])
        
        
        
        #Populate data to Credit_Card
        Credit_Card.objects.all().delete()
        
        for obj in credit_card_data:
            Credit_Card.objects.create(number=obj['fields']['number'], type=obj['fields']['type'],
                                    name=obj['fields']['name'])
        
        
        #Populate data to Blog
        Blog.objects.all().delete()
        
        for obj in blog_data:
            Blog.objects.create(title=obj['fields']['title'], body=obj['fields']['body'])
        
        
        
        #Populate data to Friend
        Friend.objects.all().delete()
        
        for obj in friend_data:
            Friend.objects.create(name=obj['fields']['name'])
            
        
        #Populate data to Graffiti
        Graffiti.objects.all().delete()
        
        for obj in graffiti_data:
            Graffiti.objects.create(message=obj['fields']['message'], author=obj['fields']['author'])
        
        
         #Populate data to Food
        Food.objects.all().delete()
        
        for obj in food_data:
            Food.objects.create(name=obj['fields']['name'])
        
        
        #Populate data to Contact
        Contact.objects.all().delete()
        
        for obj in contact_data:
            Contact.objects.create(name=obj['fields']['name'], phone=obj['fields']['phone'],
                                    address=obj['fields']['address'])
        
        
        #Populate data to Athlete
        Athlete.objects.all().delete()
        
        for obj in athlete_data:
            Athlete.objects.create(name=obj['fields']['name'], sport=obj['fields']['sport'])
        
        
        #Populate data to Task
        Task.objects.all().delete()
        
        for obj in task_data:
            Task.objects.create(item=obj['fields']['item'], priority=obj['fields']['priority'],
                                        is_completed=obj['fields']['is_completed'])
        
        
        #Populate data to Ajax_Task
        Ajax_Task.objects.all().delete()
        
        for obj in ajax_task_data:
            Ajax_Task.objects.create(item=obj['fields']['item'], priority=obj['fields']['priority'],
                                        is_completed=obj['fields']['is_completed'])
        