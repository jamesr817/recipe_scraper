import mysql.connector
import requests
from bs4 import BeautifulSoup
from mysql.connector import Error


# Establishing connection to DB
mydb =mysql.connector.connect(
     host = "localhost",
     user = "recipe_user",
     passwd = "root%recipe5",
     database = "health_recipe"
)
# Testing connection
print(mydb)

# Initialzing cursor
my_cursor = mydb.cursor()

# Checking to see if liftoff db exist and is recognized when running our code
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

# Creating DB tables
# my_cursor.execute("CREATE TABLE recipes (recipe_id INT PRIMARY KEY AUTO_INCREMENT, recipe_name VARCHAR(255), servings VARCHAR(255), total_time VARCHAR(255), prep_time VARCHAR(255), cook_time VARCHAR(255), instructions VARCHAR(20000))ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci")
# my_cursor.execute("CREATE TABLE ingredients (ingredient_id INT PRIMARY KEY AUTO_INCREMENT, ingredient_name VARCHAR(255), measurement VARCHAR(255), recipe_id INT, FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id))ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci")

# Testing tables
for tables in my_cursor:
    print(tables)

my_cursor.close()
mydb.close()



# urls_List=["https://www.foodnetwork.com/content/food-com/en/recipes/food-network-kitchen/h/he/hea/heal/healthified-broccoli-cheddar-soup-recipe",
# "https://www.foodnetwork.com/content/food-com/en/recipes/food-network-kitchen/h/ha/has/hash/hash-brown-casserole-recipe",
# "https://www.foodnetwork.com/content/food-com/en/recipes/ellie-krieger/p/po/por/pork/pork-tenderloin-with-seasoned-rub-recipe",
# "https://www.foodnetwork.com/content/food-com/en/recipes/food-network-kitchen/c/ch/chi/chic/chicken-and-broccoli-stir-fry-recipe",
# "https://www.foodnetwork.com/content/food-com/en/recipes/giada-de-laurentiis/r/ro/rom/roma/roman-style-chicken-recipe",
# "https://www.foodnetwork.com/content/food-com/en/recipes/alton-brown/g/gu/gua/guac/guacamole-recipe",
# "https://www.foodnetwork.com/content/food-com/en/recipes/ina-garten/r/ro/roa/roas/roasted-brussels-sprouts-recipe2",
# "https://www.foodnetwork.com/content/food-com/en/recipes/no-chef/o/ov/ove/oven/oven-baked-salmon-recipe",
# "https://www.foodnetwork.com/content/food-com/en/recipes/giada-de-laurentiis/c/ch/chi/chic/chicken-saltimbocca-recipe",
# "https://www.foodnetwork.com/content/food-com/en/recipes/alton-brown/l/le/len/lent/lentil-soup-recipe",
# "https://www.foodnetwork.com/recipes/food-network-kitchen/chicken-scampi-pasta-5588113",
# "https://www.foodnetwork.com/recipes/ellie-krieger/pasta-with-escarole-white-beans-and-chicken-sausage-recipe-1949665",
# "https://www.foodnetwork.com/recipes/rachael-ray/chicken-sausage-pepper-and-onion-pasta-fake-bake-recipe-1945284",
# "https://www.foodnetwork.com/recipes/jambalaya-pasta-with-penne-chicken-shrimp-and-andouille-3644624",
# "https://www.foodnetwork.com/recipes/food-network-kitchen/herbed-chicken-marsala-recipe-2121049",
# "https://www.foodnetwork.com/recipes/food-network-kitchen/healthy-lemony-yogurt-loaf-cake-recipe-2112126",
# "https://www.foodnetwork.com/recipes/ellie-krieger/sloppy-joes-recipe-1946755",
# "https://www.foodnetwork.com/recipes/food-network-kitchen/pan-seared-salmon-with-kale-and-apple-salad-recipe-3361718",
# "https://www.foodnetwork.com/recipes/food-network-kitchen/breakfast-casserole-3362652",
# "https://www.foodnetwork.com/recipes/food-network-kitchen/whole30-bacon-and-egg-cups-3881819",
# "https://www.foodnetwork.com/recipes/food-network-kitchen/slow-cooker-pork-tacos-recipe-1972753",
# "https://www.foodnetwork.com/recipes/alton-brown/angel-food-cake-recipe-1938726",
# "https://www.foodnetwork.com/recipes/ellie-krieger/blueberry-compote-recipe-1946907",
# "https://www.foodnetwork.com/recipes/ellie-krieger/roasted-cauliflower-and-broccoli-recipe-1947594",
# "https://www.foodnetwork.com/recipes/food-network-kitchen/buffalo-cauliflower-with-blue-cheese-sauce-3362800",
# ]
# for url in urls_List:

    # response = requests.get(url)

    # soup = BeautifulSoup(response.text, "html.parser")

    # recipesLocated = soup.body.find_all(class_="recipe-body")

    # To view webpage and further inspect its structure
    # recipe = soup.findAll(class_="recipe-body")

    # recipe_name = soup.find("h1").get_text().strip()
    # total_time= soup.find(class_="o-RecipeInfo__a-Description m-RecipeInfo__a-Description--Total").get_text().strip()
    # prep_time=soup.find(class_="o-RecipeInfo__m-Time").select(".o-RecipeInfo__a-Description")[0].get_text().strip()
    # cook_time=soup.find(class_="o-RecipeInfo__m-Time").select(".o-RecipeInfo__a-Description")[1].get_text().strip()
    # servings= soup.find(class_="o-RecipeInfo__m-Yield").select(".o-RecipeInfo__a-Description")[0].get_text()
    # directions= []
    # # Let's try this:
    #for i in soup.find(class_="o-Method__m-Body").select(".o-Method__m-Step"):
        #directions.append(i.get_text().strip())

    #instructions=''.join(directions).replace(".",".\n").strip()

    # Variable Tests
    #print(recipesLocated)
    # print(type(recipe_name))
    # print(type(total_time))
    # print(type(prep_time))
    # print(type(cook_time))
    # print(type(servings))
    # print(directions)
    # print(instructions)





    ##For Ingredients
    # ingredients =soup.find(class_="o-Ingredients__m-Body").get_text().strip().split("\n")
    # for i in ingredients:
    #     print(i)
    


    # print(ingredients)







# TODO Figure out how to get the scraped data into the db. DB keeps rejecting the data. From what I'm interpreting, its from the data type from instructions and data type of ingredients
