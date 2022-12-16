from django.shortcuts import render
import requests
import os
from . keys import api_key
apikey = api_key()

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')



#params is the request object and the = is the var
params = {
    'instructionsRequired':'true',
    'query':'pasta',
    # 'cuisine':'italian',#there is a big list but will come back to
    # 'intolerances':'gluten',#there is a big list but will come back to
    # 'includeIngredients':'tomato,cheese',#have to comeback to or leave
    # 'excludeIngredients':'eggs',#comeback to as well
    'type':'main course' #will comeback to
    
    # 'addRecipeInformation':'true',
    # 'addRecipeNutrition':'true',
    # 'ignorePantry':'true',
    # 'sort':'calories'
}

url = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apikey}",params=params)
recipe = url.json()
# print(recipe['results'][0]['title'])
def recipe():
    return
