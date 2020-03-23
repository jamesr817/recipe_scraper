import recipe_scrapers
from recipe_scrapers import scrape_me
import requests
from bs4 import BeautifulSoup
import csv
from csv import excel, writer



foodnet_urls_List=[
"https://www.foodnetwork.com/content/food-com/en/recipes/food-network-kitchen/h/he/hea/heal/healthified-broccoli-cheddar-soup-recipe",
"https://www.foodnetwork.com/content/food-com/en/recipes/food-network-kitchen/h/ha/has/hash/hash-brown-casserole-recipe",
"https://www.foodnetwork.com/content/food-com/en/recipes/ellie-krieger/p/po/por/pork/pork-tenderloin-with-seasoned-rub-recipe",
"https://www.foodnetwork.com/content/food-com/en/recipes/food-network-kitchen/c/ch/chi/chic/chicken-and-broccoli-stir-fry-recipe",
"https://www.foodnetwork.com/content/food-com/en/recipes/giada-de-laurentiis/r/ro/rom/roma/roman-style-chicken-recipe",
"https://www.foodnetwork.com/content/food-com/en/recipes/alton-brown/g/gu/gua/guac/guacamole-recipe",
"https://www.foodnetwork.com/content/food-com/en/recipes/ina-garten/r/ro/roa/roas/roasted-brussels-sprouts-recipe2",
"https://www.foodnetwork.com/content/food-com/en/recipes/no-chef/o/ov/ove/oven/oven-baked-salmon-recipe",
"https://www.foodnetwork.com/content/food-com/en/recipes/giada-de-laurentiis/c/ch/chi/chic/chicken-saltimbocca-recipe",
"https://www.foodnetwork.com/content/food-com/en/recipes/alton-brown/l/le/len/lent/lentil-soup-recipe",
"https://www.foodnetwork.com/recipes/food-network-kitchen/chicken-scampi-pasta-5588113",
"https://www.foodnetwork.com/recipes/ellie-krieger/pasta-with-escarole-white-beans-and-chicken-sausage-recipe-1949665",
"https://www.foodnetwork.com/recipes/rachael-ray/chicken-sausage-pepper-and-onion-pasta-fake-bake-recipe-1945284",
"https://www.foodnetwork.com/recipes/jambalaya-pasta-with-penne-chicken-shrimp-and-andouille-3644624",
"https://www.foodnetwork.com/recipes/food-network-kitchen/herbed-chicken-marsala-recipe-2121049",
"https://www.foodnetwork.com/recipes/food-network-kitchen/healthy-lemony-yogurt-loaf-cake-recipe-2112126",
"https://www.foodnetwork.com/recipes/ellie-krieger/sloppy-joes-recipe-1946755",
"https://www.foodnetwork.com/recipes/food-network-kitchen/pan-seared-salmon-with-kale-and-apple-salad-recipe-3361718",
"https://www.foodnetwork.com/recipes/food-network-kitchen/breakfast-casserole-3362652",
"https://www.foodnetwork.com/recipes/food-network-kitchen/whole30-bacon-and-egg-cups-3881819",
"https://www.foodnetwork.com/recipes/food-network-kitchen/slow-cooker-pork-tacos-recipe-1972753",
"https://www.foodnetwork.com/recipes/alton-brown/angel-food-cake-recipe-1938726",
"https://www.foodnetwork.com/recipes/ellie-krieger/blueberry-compote-recipe-1946907",
"https://www.foodnetwork.com/recipes/ellie-krieger/roasted-cauliflower-and-broccoli-recipe-1947594",
"https://www.foodnetwork.com/recipes/food-network-kitchen/buffalo-cauliflower-with-blue-cheese-sauce-3362800",
"https://www.foodnetwork.com/recipes/food-network-kitchen/roasted-brussels-sprouts-with-grapes-3894868",
"https://www.foodnetwork.com/recipes/food-network-kitchen/brussels-sprouts-in-a-blanket-3757604",
"https://www.foodnetwork.com/recipes/ina-garten/roasted-brussels-sprouts-recipe2-1941953",
"https://www.foodnetwork.com/recipes/ree-drummond/roasted-brussels-sprouts-and-kale-3531763",
"https://www.foodnetwork.com/recipes/ree-drummond/beautiful-brussels-sprouts-3166862",
"https://www.foodnetwork.com/recipes/food-network-kitchen/air-fryer-brussels-sprouts-5565493",
"https://www.foodnetwork.com/recipes/ina-garten/shaved-brussels-sprouts-with-pancetta-5509453",
"https://www.foodnetwork.com/recipes/ina-garten/balsamic-roasted-brussels-sprouts-recipe-1996813",
"https://www.foodnetwork.com/recipes/giada-de-laurentiis/charred-brussels-sprout-crostini-3164927",
"https://www.foodnetwork.com/recipes/dave-lieberman/slow-cooked-brussels-sprouts-recipe-1945032",
"https://www.foodnetwork.com/recipes/food-network-kitchen/bacon-wrapped-brussels-sprouts-with-creamy-lemon-dip-3364562",
"https://www.foodnetwork.com/recipes/food-network-kitchen/grilled-brussels-sprouts-7561803",
"https://www.foodnetwork.com/recipes/alton-brown/basic-brussels-sprouts-recipe-1944719",
"https://www.foodnetwork.com/recipes/ina-garten/sauteed-shredded-brussels-sprouts-3160644",
"https://www.foodnetwork.com/in-season-now/packages/winter-produce-guide",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-butternut-squash-soup-5449624",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-barbecue-pulled-pork-sandwiches-3649647",
"https://www.foodnetwork.com/recipes/food-network-kitchen/5-ingredient-instant-pot-mac-and-cheese-3649854",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-greek-chicken-bowls-5453420",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-carnitas-5449432",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-chicken-adobo-3649636",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-indian-shrimp-biriyani-5474376",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-chicken-noodle-soup-5195671",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-chicken-cacciatore-5449726",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-pasta-marinara-7262988",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-butter-chicken-5486200",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-creamy-ranch-chicken-pasta-8100706",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-mini-frittatas-5451507",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-beef-stew-5339970",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-saag-paneer-5486174",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-black-bean-soup-3649853",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-lemon-frozen-chicken-with-orzo-7246221",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-taco-night-5450003",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-spaghetti-squash-with-marinara-5500659",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-pozole-rojo-5486199",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-korean-style-short-ribs-5450025",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-chicken-and-dumplings-5453423",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-pot-roast-5195673",
"https://www.foodnetwork.com/recipes/food-network-kitchen/instant-pot-sunday-sauce-5453596"
]

ingredient_List = []
for urls in foodnet_urls_List:
    scraper =scrape_me(urls)
    ingredients = scraper.ingredients()
    for i in ingredients:
        name = scraper.title()
        item = i
        ingredientList = [[name, item]]
        ingredient_List.extend(ingredientList)

# Writing CSV for Recipe Table
with open ("recipe_list.csv", "w") as csv_file:
    csv_writer = writer(csv_file,) #quoting=csv.QUOTE_ALL)
    headers = ["id","name", "serve_time", "servings", "steps" ]
    csv_writer.writerow(headers)
    # Appending to recipe_list CSV file 
    for url in foodnet_urls_List:
        scraper = scrape_me(url)
        recipe_ID = foodnet_urls_List.index(url)
        name = scraper.title()
        serve_time = scraper.total_time()
        servings = scraper.yields()
        steps = scraper.instructions()        
        rows=[recipe_ID, name, serve_time, servings, steps]
        csv_writer.writerow(rows)
   

# Writing CSV for Ingredients Table
with open ("ingredients_list.csv","w") as csv_file:
    csv_writer = writer(csv_file, quoting=csv.QUOTE_ALL)
    headers = ["id","name","ingredients"]
    csv_writer.writerow(headers)
    for i in ingredient_List:
        ingredient_ID = ingredient_List.index(i)
        name = i[0]
        ingredient = i[1]
        rows= [ingredient_ID,name,ingredient]
        csv_writer.writerow(rows)
        
