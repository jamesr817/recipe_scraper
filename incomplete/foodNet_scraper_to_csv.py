import requests
from bs4 import BeautifulSoup
import csv
from csv import excel, writer





urls_List=["https://www.foodnetwork.com/content/food-com/en/recipes/food-network-kitchen/h/he/hea/heal/healthified-broccoli-cheddar-soup-recipe",
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
for url in urls_List:

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    recipesLocated = soup.body.find_all(class_="recipe-body")

    # To view webpage and further inspect its structure
    recipe = soup.findAll(class_="recipe-body")

    recipe_name = soup.find("h1").get_text().strip()
    total_time= soup.find(class_="o-RecipeInfo__a-Description m-RecipeInfo__a-Description--Total").get_text().strip()
    prep_time=soup.find(class_="o-RecipeInfo__m-Time").select(".o-RecipeInfo__a-Description")[0].get_text().strip()
    cook_time=soup.find(class_="o-RecipeInfo__m-Time").select(".o-RecipeInfo__a-Description")[1].get_text().strip()
    servings= soup.find(class_="o-RecipeInfo__m-Yield").select(".o-RecipeInfo__a-Description")[0].get_text()
    directions= []
    for i in soup.find(class_="o-Method__m-Body").select(".o-Method__m-Step"):
        directions.append(i.get_text().strip())

    instructions=''.join(directions).replace(".",".\n").strip()

    # Variable Tests
    #print(recipesLocated)
    # print(type(recipe_name))
    # print(type(total_time))
    # print(type(prep_time))
    # print(type(cook_time))
    # print(type(servings))
    # print(directions)
    # print(instructions)

    # To write or append for recipe's table. Just use 'a' the append and 'w' to write. When appending comment out "headers"
    # with open ("recipes.csv", "a") as csv_file:
    #     csv_writer = writer(csv_file, quoting=csv.QUOTE_ALL)
    #     headers = ["Recipe Name", "servings","Total Time", "Prep Time", "Cook Time", "Instruction" ]
    #     csv_writer.writerow(headers)
    #     rows=[recipe_name, servings,total_time,prep_time,cook_time,instructions]
    #     csv_writer.writerow(rows)



    ##For Ingredients
    ingredients =soup.find(class_="o-Ingredients__m-Body").get_text().strip().split("\n")
    for i in ingredients:
        print(i)
    


    # print(ingredients)


    # To write or append to ingredients table
    with open ("ingredients.csv","a") as csv_file:
        csv_writer = writer(csv_file, quoting=csv.QUOTE_ALL)
        headers = ["id","name","Ingredients"]
        csv_writer.writerow(headers)

        for i in ingredients:
            ingredient_id = ingredients.index(i)
            rows= [ingredient_id,recipe_name,i]
            csv_writer.writerow(rows)





