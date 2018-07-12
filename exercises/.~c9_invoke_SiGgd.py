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
    path('graffiti', views.graffiti, name="graffiti"),
    path('graffiti_save', views.graffiti_save, name="graffiti_save"),
    path('food_list', views.food_list, name="food_list"),
    path('food_save', views.food_save, name="food_save"),
    path('update_food', views.update_food, name="update_food")
    path('edit_food_save/<int:id>', views.edit_food_save, name="edit_food_save"),
    path
    
]
