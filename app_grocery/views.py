from django.shortcuts import render, redirect
import requests
import os
from django.http import HttpResponse
from . keys import api_key
apikey = api_key()
# user_choice = 

def home(request):
    if request.method=='POST':
        params = {
    'instructionsRequired':True,
    'query':request.POST['dish'],
    'addChildren':True,
    'number':20,
    #this is how you can take the input and put in your search.  'dish' is in home.html
    #'cuisine':'italian',#there is a big list but will come back to
    # 'intolerances':'gluten',#there is a big list but will come back to
    # 'includeIngredients':'tomato,cheese',#have to comeback to or leave
    # 'excludeIngredients':'eggs',#comeback to as well
    'type':'main course', #will comeback to
    
    # 'addRecipeInformation':'true',
    # 'addRecipeNutrition':'true',
    # 'ignorePantry':'true',
    # 'sort':'calories'
}

        url = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apikey}",params=params)
        recipe = url.json()
        recipe_image = recipe['results'][0]['title'],recipe['results'][0]['image']
        recipe_image_url = recipe_image[1]
        recipe_title = recipe_image[0]
        # recipe_items = recipe_  # Need to get the actual items from the json.
        print(recipe_image[1])

        context = {
            'recipe_image_url':recipe_image_url,
            'recipe_title':recipe_title,
            'picture_of_food':picture_of_food,

            #recipe is the key and we are using it as the value. THis is what is in the home.html file and is listed in the {{}}
            # make a for loop for the results in the html file.
        }
        return render(request, 'pages/home.html', context)# this is app_grocery/home

    else:
            
        return render(request, 'pages/home.html')# this is app_grocery/home.  This is the GET method

def about(request):
    return render(request, 'pages/about.html')# this is app_grocery/about



#params is the request object and the = is the var
params = {
     'instructionsRequired':'true',
     'query':'true'
    # 'cuisine':'italian',#there is a big list but will come back to
    # 'intolerances':'gluten',#there is a big list but will come back to
    # 'includeIngredients':'tomato,cheese'#have to comeback to or leave
    # 'excludeIngredients':'eggs',#comeback to as well
    # 'type':'main course', #will comeback to
    
    #  'addRecipeInformation':'true',
    # 'addRecipeNutrition':'true',
    #  'ignorePantry':'true',
    # 'sort':'calories'
 }
whats_at_home = requests.get(f"https://api.spoonacular.com/food/ingredients/search?apiKey={apikey}",params=params)
url = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apikey}",params=params)
recipe = url.json()
print(recipe['results'][0]['title'])
print(recipe['results'][0]['image'])
picture_of_food = requests.get(recipe['results'][0]['image'])
def recipe(request):
    return render(request, 'pages/about.html')
#Ask if I should remove this code and place it in html. 
def hungry_name(request, user):
    return HttpResponse(f"Hello hungry person.  Lets get your food choices, {user}")
recipe1 = whats_at_home.json()   
def recipe1(request):
    return render(request, 'pages/about.html')

# print(recipe1['results'][0]['image'])
# def recipe1(request):
#     return render(request, 'pages/about.html')
