import random
import tkinter as tk
from tkinter import *

# Extended recipe categories and their corresponding ingredients
recipe_categories = {
    "Italian": [
        ("pasta", (100, 300), "g"), ("tomatoes", (1, 5), "pcs"), ("olive oil", (20, 100), "ml"), ("basil", (5, 20), "g"), ("garlic", (1, 5), "cloves"), 
        ("parmesan cheese", (20, 100), "g"), ("mozzarella", (50, 150), "g"), ("oregano", (2, 10), "g"), ("red wine", (50, 150), "ml"), ("mushrooms", (50, 200), "g")
    ],
    "Mexican": [
        ("tortillas", (2, 6), "pcs"), ("beans", (100, 300), "g"), ("rice", (100, 200), "g"), ("salsa", (50, 150), "ml"), ("avocado", (1, 2), "pcs"), 
        ("cheese", (50, 150), "g"), ("jalapenos", (20, 100), "g"), ("cilantro", (5, 20), "g"), ("lime", (1, 2), "pcs"), ("corn", (50, 200), "g")
    ],
    "Chinese": [
        ("rice", (100, 200), "g"), ("soy sauce", (20, 50), "ml"), ("ginger", (5, 20), "g"), ("garlic", (1, 5), "cloves"), ("vegetables", (100, 300), "g"), 
        ("chicken", (100, 300), "g"), ("scallions", (20, 100), "g"), ("sesame oil", (10, 30), "ml"), ("tofu", (100, 200), "g"), ("hoisin sauce", (20, 50), "ml")
    ],
    "Indian": [
        ("rice", (100, 200), "g"), ("lentils", (50, 150), "g"), ("turmeric", (2, 10), "g"), ("cumin", (2, 10), "g"), ("garam masala", (2, 10), "g"), 
        ("chicken", (100, 300), "g"), ("yogurt", (50, 150), "ml"), ("coriander", (5, 20), "g"), ("ginger", (5, 20), "g"), ("tomatoes", (1, 5), "pcs")
    ],
    "French": [
        ("baguette", (1, 2), "pcs"), ("brie cheese", (50, 150), "g"), ("wine", (50, 150), "ml"), ("herbs de Provence", (2, 10), "g"), ("garlic", (1, 5), "cloves"), 
        ("butter", (20, 100), "g"), ("cream", (50, 150), "ml"), ("thyme", (2, 10), "g"), ("mushrooms", (50, 200), "g"), ("shallots", (20, 100), "g")
    ],
    # Add more recipe categories and ingredients as needed
}

# Cooking phrases with required ingredients and utensils
cooking_phrases = [
    ("Chop the vegetables finely.", ["vegetables"], ["knife", "cutting board"]),
    ("Sauté the garlic until golden brown.", ["garlic"], ["pan", "spatula"]),
    ("Simmer the sauce for 20 minutes.", ["sauce"], ["pot", "spatula"]),
    ("Boil the pasta until al dente.", ["pasta"], ["pot"]),
    ("Grill the chicken until fully cooked.", ["chicken"], ["grill", "tongs"]),
    ("Mix all ingredients thoroughly.", [], ["bowl", "spoon"]),
    ("Garnish with fresh herbs.", ["herbs"], []),
    ("Stir-fry the vegetables until tender.", ["vegetables"], ["pan", "spatula"]),
    ("Marinate the chicken for 30 minutes.", ["chicken"], ["bowl"]),
    ("Roast the vegetables in the oven.", ["vegetables"], ["oven"]),
    ("Blend the ingredients into a smooth paste.", [], ["blender"]),
    ("Steam the rice until cooked.", ["rice"], ["steamer"]),
    ("Whisk the eggs until fluffy.", ["eggs"], ["whisk", "bowl"]),
    ("Toast the bread until golden brown.", ["bread"], ["toaster"]),
    ("Caramelize the onions in a pan.", ["onions"], ["pan", "spatula"]),
    ("Poach the eggs in simmering water.", ["eggs"], ["pot"]),
    ("Grate the cheese finely.", ["cheese"], ["grater"])
]

# Common cooking steps with no specific requirements
common_steps = [
    "Wash all the vegetables thoroughly.",
    "Season with salt and pepper to taste.",
    "Serve hot and enjoy your meal!",
    "Add a pinch of salt.",
    "Drizzle with olive oil.",
    "Sprinkle with fresh herbs.",
    "Mix well before serving.",
    "Serve with a side of bread.",
    "Top with grated cheese.",
    "Add a squeeze of lemon juice."
]

# Reviews
reviews = [
    "John: \"Delicious and easy to make!\"",
    "Jane: \"My family loved it!\"",
    "Alex: \"A new favorite in our household.\"",
    "Sam: \"Simple and tasty!\"",
    "Chris: \"Will definitely make this again.\""
]

# Generate a random recipe with detailed instructions
def generate_recipe(selected_category=None):
    recipe = "Recipe: \n"
    
    # Select a random recipe category if none is selected
    if selected_category is None:
        recipe_category = random.choice(list(recipe_categories.keys()))
    else:
        recipe_category = selected_category
    recipe += "Category: " + recipe_category + "\n"
    
    recipe += '\n'

    # Randomly select ingredients based on the recipe category
    recipe += "Ingredients: \n"
    ingredients = random.sample(recipe_categories[recipe_category], 6)
    for ingredient, (min_amount, max_amount), unit in ingredients:
        amount = random.randint(min_amount, max_amount)
        recipe += f"{amount} {unit} {ingredient}\n"
    
    recipe += '\n'
    
    recipe += "Instructions: \n"
    used_utensils = set()
    selected_phrases = random.sample(cooking_phrases, 10)
    for phrase, required_ingredients, utensils in selected_phrases:
        if all(ingredient in [i[0] for i in ingredients] for ingredient in required_ingredients):
            recipe += phrase + "\n"
            used_utensils.update(utensils)
    
    common_steps_selected = random.sample(common_steps, 3)
    for step in common_steps_selected:
        recipe += step + "\n"
    
    if "oven" in used_utensils and random.choice([True, False]):
        preheat_temp = random.randint(160, 220)
        recipe += f"Preheat the oven to {preheat_temp}°C.\n"
    
    if "oven" in used_utensils and random.choice([True, False]):
        bake_time = random.randint(20, 60)
        recipe += f"Bake for {bake_time} minutes.\n"
    
    if random.choice([True, False]):
        rest_time = random.randint(5, 20)
        recipe += f"Let it rest for {rest_time} minutes before serving.\n"
    
    recipe += '\n'

    recipe += "Utensils: " + ", ".join(used_utensils) + "\n"
    
    cooking_temperature = random.randint(160, 220)
    cooking_time = random.randint(20, 60)
    recipe += f"Cooking Temperature: {cooking_temperature}°C\n"
    recipe += f"Cooking Time: {cooking_time} minutes\n"
    
    serving_size = random.choice([2, 4, 6, 8])
    recipe += f"Serving Size: {serving_size} servings\n"
    
    recipe += '\n'

    num_reviews = random.randint(1, len(reviews))
    selected_reviews = random.sample(reviews, num_reviews)
    recipe += "Reviews: \n"
    for review in selected_reviews:
        recipe += review + "\n"
    
    calories = random.randint(300, 700)
    recipe += f"Calories: {calories} kcal per serving\n"
    
    return recipe

def display_recipe():
    selected_category = category_var.get()
    if selected_category == "Random":
        selected_category = None
    recipe = generate_recipe(selected_category)
    recipe_text.delete(1.0, tk.END)
    recipe_text.insert(tk.END, recipe)

def on_space(event):
    display_recipe()

def on_enter(event):
    event.widget['background'] = '#d3d3d3'  # Color on hover

def on_leave(event):
    event.widget['background'] = 'SystemButtonFace'  # Initial color

# Create a GUI window
window = tk.Tk()
window.title("Recipe Generator")
window.geometry("500x600")

store_name_label = tk.Label(window, text="Menu", font=("Arial", 16))
store_name_label.pack(pady=10)

menu_active = False

category_var = tk.StringVar(window)
category_var.set("Random")
category_menu = tk.OptionMenu(window, category_var, "Random", *recipe_categories.keys())
category_menu.config(activebackground='#d3d3d3') 
category_menu.pack(pady=10)
category_menu.bind("<Enter>", on_enter)
category_menu.bind("<Leave>", on_leave)

generate_button = tk.Button(window, text="Generate Recipe", command=display_recipe, activebackground="#A9A9A9")
generate_button.pack(pady=10)
window.bind('<space>', on_space)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

# Create a frame for the Text widget and Scrollbar
frame = tk.Frame(window)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create vertical and horizontal Scrollbars
v_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

h_scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Create a Text widget
recipe_text = tk.Text(frame, wrap=tk.NONE, yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set, font=("Arial", 12))
recipe_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Configure the Scrollbars
v_scrollbar.config(command=recipe_text.yview)
h_scrollbar.config(command=recipe_text.xview)

window.mainloop()
