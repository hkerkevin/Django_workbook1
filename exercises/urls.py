from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'exercises'


urlpatterns = [
    
    path('', views.superheroes, name='superheroes'),
    path('animals', views.animals, name='animals'),
    path('cars', views.cars, name='cars'),
    path('templates', views.templates, name='templates'),
    path('summary', views.summary, name='summary'),
    
    path('submit_form', views.submit_form, name='submit_form'),
    path('team_edward', views.team_edward, name='team_edward'),
    path('team_jacob', views.team_jacob, name='team_jacob'),
    
    # add new capture here
    path('create_page', views.create_page, name='create_page'),
    path('forrest_gump', views.forrest_gump, name='forrest_gump'),
    path('wizard_of_oz', views.wizard_of_oz, name='wizard_of_oz'),
    path('the_godfather', views.the_godfather, name='the_godfather'),
    path('casablanca', views.casablanca, name='casablanca'),
    path('stocks', views.stocks, name='stocks'),
    path('new_credit_card_link', views.credit_cards, name='credit_cards'),
    path('my_new_template', views.my_new_template, name='my_new_template'),
    path('animals_new', views.animals_new, name='animals_new'),
    path('new_credit_card_details/<int:id>', views.cc, name="cc"),
    path('new_page', views.new_page, name="new_page"),
    path('blog', views.blog, name='blog'),
    path('blog_details/<int:id>', views.blog_details, name='blog_details'),
    path('bert', views.bert, name='bert'),
    path('ernie', views.ernie, name="ernie"),
    path('pumba', views.pumba, name="pumba"),
    path('timon', views.timon, name="timon"),
    path('search_superheroes', views.hero_search, name="hero_search"),
    path('results_superheroes', views.hero_results, name="hero_results"),
    path('details_superhero/<int:id>', views.hero_details, name="hero_details"),
    path('friend_list', views.friend_list, name="friend_list"),
    path('friend_save', views.friend_save, name="friend_save"),
    path('delete_friend/<int:friend_id>', views.delete_friend, name="delete_friend"),
    path('graffiti', views.graffiti, name="graffiti"),
    path('graffiti_save', views.graffiti_save, name="graffiti_save"),
    path('food_list', views.food_list, name="food_list"),
    path('food_save', views.food_save, name="food_save"),
    path('edit_food/<int:food_id>', views.edit_food, name="edit_food"),
    path('edit_food_save/<int:food_id>', views.edit_food_save, name="edit_food_save"),
    path('phone_book', views.phone_book, name="phone_book"),
    path('add_phone', views.add_phone, name="add_phone"),
    path('phone_book_save', views.phone_book_save, name="phone_book_save"),
    path('edit_phone/<int:id>', views.edit_phone, name="edit_phone"),
    path('edit_phone_save/<int:id>', views.edit_phone_save, name="edit_phone_save"),
    path('details_phone/<int:id>', views.details_phone, name="details_phone"),
    path('athlete_list', views.athlete_list, name="athlete_list"),
    path('delete_athlete/<int:athlete_id>', views.delete_athlete, name="delete_athlete"),
    path('add_athlete', views.add_athlete, name="add_athlete"),
    path('task_list', views.task_list, name="task_list"),
    path('delete_task/<int:task_id>', views.delete_task, name="delete_task"),
    path("add_task", views.add_task, name="add_task"),
    path("update_task/<int:task_id>", views.update_task, name="update_task"),
    path("edit_task/<int:task_id>", views.edit_task, name="edit_task"),
    path("edit_task_save/<int:task_id>", views.edit_task_save, name="edit_task_save"),
    path("ajax_task_list", views.ajax_task_list, name="ajax_task_list"),
    path("add_ajax_task", views.add_ajax_task, name="add_ajax_task"),
    path("test", views.test, name="test"),
    path("toggle_complete", views.toggle_complete, name="toggle_complete"),
    path("calendar", views.calendar, name="calendar"),
    path("fbview", views.fbview, name="fbview"),
]
