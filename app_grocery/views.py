from django.shortcuts import render, redirect
import requests
import os
from django.http import HttpResponse
from . keys import api_key
apikey = api_key()
# user_choice = 

def home(request):
    if request.method=='POST':
        print('hello')
        params = {
    'instructionsRequired':True,
    'query':request.POST['dish'],
    'addChildren':True,
    'number':20,
    'excludeIngredients':True,#comeback to as well
    'addRecipeInformation':True,
}#this is how you can take the input and put in your search.  'dish' is in home.html

        url = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apikey}",params=params)
        recipe = url.json()
        recipe_image = [recipe['results'][0]['title'],recipe['results'][0]['image']]
        recipe_image_url = recipe_image[1]##Dec28
        recipe_title = recipe_image[0]
        #print("picture of food",picture_of_food)
        whats_at_home = requests.get(f"https://api.spoonacular.com/food/ingredients/search?apiKey={apikey}",params=params)
        url = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apikey}",params=params)##added 27Dec from test file

        recipe = url.json()##added 27Dec from test file
        info = recipe['results'][0]['id']##added 27Dec from test file
        url2= requests.get(f"https://api.spoonacular.com/recipes/{info}/information?apiKey={apikey}")##added 27Dec from test file
        recipe2 = url2.json()
        recipe = url.json()
        instructions=recipe2["instructions"] 
# print(recipe['results'][0]['title'])##stopped 28 Dec
# print(recipe['results'][0]['image'])##stopped 28 Dec
        picture_of_food = requests.get(recipe['results'][0]['image'])
        extend_ingred = recipe2["extendedIngredients"]
        def recipe_list():  
            items = []
            for numz in range(0,len(extend_ingred)):

                items.append(extend_ingred[numz]['name'])
            return items

        item_to_get=recipe_list()

        context = {
            'recipe_image_url':recipe_image_url,##28Dec
            'recipe_title':recipe_title,
            'picture_of_food':picture_of_food,
            'instructions':instructions,##added 27Dec from test file
            'item_to_get':item_to_get,

            #recipe is the key and we are using it as the value. THis is what is in the home.html file and is listed in the {{}}
            # make a for loop for the results in the html file.
        }
        return render(request, 'pages/home.html',context)# this is app_grocery/home

    else:
            
        return render(request, 'pages/home.html')# this is app_grocery/home.  This is the GET method
"""
BIG CHANGE WHICH IS ME TRYING TO TAB EVERYTING AFTER LINE 46 OVER TO FIT IN THE HOME FUNCTION

"""
##Dec29 changed from about to home
def about(request):
    return render(request, 'pages/home.html')# this is app_grocery/about
#params is the request object and the = is the var
params = {
     'instructionsRequired':'True',
     'query':'True',
     'addRecipeInformation':True
 }
##params.update({"query":True})##added 28 Dec

whats_at_home = requests.get(f"https://api.spoonacular.com/food/ingredients/search?apiKey={apikey}",params=params)
url = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apikey}",params=params)##added 27Dec from test file

recipe = url.json()##added 27Dec from test file
info = recipe['results'][0]['id']##added 27Dec from test file
url2= requests.get(f"https://api.spoonacular.com/recipes/{info}/information?apiKey={apikey}")##added 27Dec from test file
recipe2 = url2.json()
recipe = url.json()
instructions=recipe2["instructions"] 
# print(recipe['results'][0]['title'])##stopped 28 Dec
# print(recipe['results'][0]['image'])##stopped 28 Dec
picture_of_food = requests.get(recipe['results'][0]['image'])

def recipe(request):
    return render(request, 'pages/home.html')##Dec29 changed from about to home
#Ask if I should remove this code and place it in html. 

# recipe1 = whats_at_home.json()   ##added 27Dec from test file
# def recipe1(request):
#     return render(request, 'pages/about.html')
    ##Testing 29Dec

   
##params.update({"instructions":instructions})##This is what I need help with##Dec28


# print(recipe1['results'][0]['image'])
# def recipe1(request):
#     return render(request, 'pages/about.html')
