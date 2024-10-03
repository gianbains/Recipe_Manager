# 1. Setting up project structure for storing recipe data
def load_recipes():
    recipes = []
    with open("recipe_list.txt", "r", encoding="utf-8") as data:
        for line in data:
            parts = line.strip().split("|")
            if len(parts) == 3:  # Ensure the line has exactly 3 parts: name, ingredients, steps
                name, ingredients, steps = parts
                recipes.append({
                    "name": name,
                    "ingredients": ingredients.split(),
                    "steps": steps.split(",")
                })
            else:
                print(f"Skipping malformed line: {line.strip()}")
    return recipes
 
# 2. Save recipes to file
def save_recipes(recipes):
    with open("recipe_list.txt", "w", encoding="utf-8") as file:
        for recipe in recipes:
            file.write("{}|{}|{}\n".format(
                recipe["name"], " ".join(recipe["ingredients"]), ",".join(recipe["steps"])
            ))
 
# 3. View all recipes from file
def view_recipes():
    recipes = load_recipes()
    if recipes:
        for recipe in recipes:
            print(f"Recipe: {recipe['name']}")
            print(f"Ingredients: {' '.join(recipe['ingredients'])}")
            print(f"Steps: {', '.join(recipe['steps'])}\n")
    else:
        print("No recipes found.")
 
# 4. Add a recipe
def add_recipe():
    name = input("Recipe name: ")
    ingredients = input("Write ingredients (with spaces in between): ").split()
    steps = []
    while True:
        step = input("Enter cooking steps, finish by pressing enter: ")
        if step == "":
            break
        steps.append(step)
    new_recipe = {"name": name, "ingredients": ingredients, "steps": steps}
    recipes = load_recipes()
    recipes.append(new_recipe)
    save_recipes(recipes)
    print(f"Recipe '{name}' added successfully!")
 
# 5. Search for a recipe
def search_recipe():
    recipes = load_recipes()
    ask = input("Search for a recipe by name or ingredients used: ").lower()
    found = False
    for recipe in recipes:
        if ask in recipe["name"].lower() or ask in " ".join(recipe["ingredients"]).lower():
            print(f"Recipe found: {recipe['name']}")
            print(f"Ingredients: {' '.join(recipe['ingredients'])}")
            print(f"Steps: {', '.join(recipe['steps'])}\n")
            found = True
    if not found:
        print("Recipe not found.")
 
# 6. Edit a recipe
def edit_recipe():
    recipes = load_recipes()
    search = input("Search for a recipe to edit: ").lower()
    for recipe in recipes:
        if search in recipe["name"].lower():
            print(f"Editing Recipe: {recipe['name']}")
            print(f"Current ingredients: {' '.join(recipe['ingredients'])}")
            new_ingredients = input("Enter new ingredients (with spaces in between): ").split()
            recipe["ingredients"] = new_ingredients
            new_steps = []
            while True:
                step = input("Enter new cooking steps, finish by pressing enter: ")
                if step == "":
                    break
                new_steps.append(step)
            recipe["steps"] = new_steps
            save_recipes(recipes)
            print(f"Recipe '{recipe['name']}' updated successfully!")
            return
    print("Recipe not found.")
 
# 7. Delete a recipe
def delete_recipe():
    recipes = load_recipes()
    delete = input("Which recipe would you like to delete?: ").lower()
    for i, recipe in enumerate(recipes):
        if delete in recipe["name"].lower():
            print(f"Recipe '{recipe['name']}' has been deleted.")
            recipes.pop(i)
            save_recipes(recipes)
            return
    print("Recipe not found.")
 
# 8. User interface menu
def menu():
    while True:
        print("\nMenu")
        print("1. Add recipe")
        print("2. View available recipes")
        print("3. Search recipe")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("6. Exit")
        option = input("Select from the options above (1-6): ")
        if option == "1":
            add_recipe()
        elif option == "2":
            view_recipes()
        elif option == "3":
            search_recipe()
        elif option == "4":
            edit_recipe()
        elif option == "5":
            delete_recipe()
        elif option == "6":
            print("Exiting...")
            break
        else:
            print("Error, option not recognized.")
 
# Start the program
menu()
