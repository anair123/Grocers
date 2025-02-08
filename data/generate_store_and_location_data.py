import random
from faker import Faker
import pandas as pd

# Initialize the Faker instance
fake = Faker()

# Berlin's central coordinates (latitude and longitude)
berlin_center = (52.5200, 13.4050)

# Define the boundaries for Berlin (approximately)
latitude_range = (52.3, 52.7)  # Latitude range for Berlin
longitude_range = (13.0, 13.8)  # Longitude range for Berlin

# Function to generate random location within Berlin
def generate_random_location():
    lat = random.uniform(*latitude_range)
    lon = random.uniform(*longitude_range)
    return lat, lon

# Example locations in Berlin, each associated with a store
locations_berlin = [
    {"location_id": 1, "location_name": "Mitte", "store_id": 1, "latitude": None, "longitude": None},
    {"location_id": 2, "location_name": "Kreuzberg", "store_id": 1, "latitude": None, "longitude": None},
    {"location_id": 3, "location_name": "Charlottenburg", "store_id": 2, "latitude": None, "longitude": None},
    {"location_id": 4, "location_name": "Friedrichshain", "store_id": 2, "latitude": None, "longitude": None},
    {"location_id": 5, "location_name": "Prenzlauer Berg", "store_id": 3, "latitude": None, "longitude": None},
    {"location_id": 6, "location_name": "Neukölln", "store_id": 3, "latitude": None, "longitude": None},
    {"location_id": 7, "location_name": "Spandau", "store_id": 4, "latitude": None, "longitude": None},
    {"location_id": 8, "location_name": "Lichtenberg", "store_id": 4, "latitude": None, "longitude": None}
]

# Assigning random coordinates (latitude and longitude) to each location
for location in locations_berlin:
    location["latitude"], location["longitude"] = generate_random_location()

print(locations_berlin)

# Define the food_items categories
food_items = {
    "Grains & Pasta": [
        "Rice", "Oats", "Pasta", "Quinoa", "Couscous", "Barley", "Polenta", "Buckwheat", "Amaranth", 
        "Spaghetti", "Macaroni", "Fusilli", "Lasagna Sheets", "Ramen", "Whole Wheat Pasta", "Egg Noodles"
    ],
    "Snacks & Sweets": [
        "Chips", "Chocolate", "Cookies", "Nuts", "Candy", "Granola Bars", "Popcorn", "Pretzels", 
        "Fruit Snacks", "Gummy Bears", "Muffins", "Crisps", "Trail Mix", "Rice Cakes", "Protein Bars"
    ],
    "Beverages": [
        "Juice", "Soda", "Coffee", "Tea", "Water", "Energy Drink", "Iced Tea", "Milkshake", 
        "Beer", "Wine", "Sparkling Water", "Herbal Tea", "Iced Coffee", "Coconut Water", "Lemonade"
    ],
    "Dairy": [
        "Milk", "Butter", "Cheese", "Yogurt", "Cream", "Cottage Cheese", "Cream Cheese", "Sour Cream", 
        "Ricotta", "Feta", "Parmesan", "Mozzarella", "Goat Cheese", "Ice Cream", "Greek Yogurt"
    ],
    "Baking & Cooking": [
        "Baking Powder", "Flour", "Sugar", "Yeast", "Salt", "Vanilla Extract", "Baking Soda", "Cornstarch", 
        "Chocolate Chips", "Cocoa Powder", "Honey", "Molasses", "Maple Syrup", "Olive Oil", "Vinegar", 
        "Coconut Oil", "Cooking Spray", "Rice Vinegar", "Sesame Oil", "Soy Sauce"
    ],
    "Fruits": [
        "Apple", "Banana", "Orange", "Grapes", "Pineapple", "Strawberries", "Blueberries", "Lemon", 
        "Avocado", "Mango", "Peach", "Pear", "Plum", "Kiwi", "Pomegranate", "Cherries", "Watermelon", "Papaya"
    ],
    "Vegetables": [
        "Carrot", "Potato", "Broccoli", "Tomato", "Spinach", "Lettuce", "Cucumber", "Onion", "Garlic", 
        "Peas", "Cauliflower", "Eggplant", "Zucchini", "Bell Pepper", "Cabbage", "Asparagus", "Sweet Potato", 
        "Leek", "Kale", "Brussels Sprouts", "Artichoke"
    ],
    "Meat & Protein": [
        "Chicken", "Beef", "Pork", "Fish", "Sausages", "Turkey", "Lamb", "Bacon", "Steak", "Salmon", 
        "Cod", "Chicken Breast", "Ground Beef", "Chicken Thighs", "Veal", "Bison", "Venison", "Tofu", "Tempeh", 
        "Seitan", "Salami", "Ham", "Deli Meats"
    ],
    "Frozen Foods": [
        "Frozen Pizza", "Ice Cream", "Frozen Vegetables", "Frozen Fruit", "Frozen Fries", "Frozen Chicken Nuggets", 
        "Frozen Meals", "Frozen Fish", "Frozen Spinach", "Frozen Waffles", "Frozen Pies", "Frozen Berries", 
        "Frozen Corn", "Frozen Dumplings", "Frozen Lasagna"
    ],
    "Canned Goods": [
        "Canned Tomatoes", "Canned Beans", "Canned Tuna", "Canned Corn", "Canned Soup", "Canned Peas", 
        "Canned Pineapple", "Canned Mushrooms", "Canned Chickpeas", "Canned Coconut Milk", "Canned Carrots", 
        "Canned Sweetcorn", "Canned Baked Beans", "Canned Spinach", "Canned Sardines", "Canned Olives"
    ],
    "Condiments & Sauces": [
        "Ketchup", "Mayonnaise", "Mustard", "Hot Sauce", "Soy Sauce", "Olive Oil", "Vinegar", "Salad Dressing", 
        "Barbecue Sauce", "Mustard", "Teriyaki Sauce", "Worcestershire Sauce", "Pesto", "Tomato Sauce", 
        "Mango Chutney", "Tartar Sauce", "Garlic Butter"
    ],
    "Spices & Herbs": [
        "Salt", "Pepper", "Cumin", "Cinnamon", "Paprika", "Oregano", "Basil", "Garlic Powder", "Chili Powder", 
        "Turmeric", "Thyme", "Rosemary", "Bay Leaves", "Parsley", "Coriander", "Saffron", "Nutmeg", "Ginger"
    ],
    "Breakfast": [
        "Cereal", "Granola", "Pancake Mix", "Maple Syrup", "Honey", "Jam", "Muffins", "Bagels", "Eggs", "Butter", 
        "Oatmeal", "Toast", "Smoothies", "Nut Butter", "Jam", "Granola Bars", "Yogurt Parfait"
    ],
    "Bread & Bakery": [
        "White Bread", "Whole Wheat Bread", "Sourdough", "Rye Bread", "Baguette", "Ciabatta", "Pita Bread", 
        "Croissants", "Bagels", "English Muffins", "Buns", "Rolls", "Flatbread", "Donuts", "Cupcakes", "Brown Bread"
    ],
    "Seafood": [
        "Shrimp", "Lobster", "Crab", "Mussels", "Clams", "Oysters", "Sardines", "Anchovies", "Cod", "Tuna", 
        "Salmon", "Herring", "Mackerel", "Squid", "Octopus", "Trout", "Scallops"
    ],
    "Non-Dairy Alternatives": [
        "Almond Milk", "Soy Milk", "Coconut Milk", "Oat Milk", "Tofu", "Vegan Cheese", "Vegan Butter", 
        "Coconut Yogurt", "Rice Milk", "Cashew Milk", "Vegan Ice Cream", "Coconut Cream"
    ],
    "Frozen Desserts": [
        "Sorbet", "Frozen Yogurt", "Popsicles", "Frozen Chocolate", "Ice Lollies", "Gelato", "Frozen Cheesecake", 
        "Frozen Brownies", "Frozen Custard", "Frozen Banana Bites", "Frozen Pudding", "Frozen Mochi"
    ],
    "International Foods": [
        "Sushi", "Ramen", "Tacos", "Fajitas", "Kimchi", "Curry Paste", "Tandoori", "Paella", "Tempura", 
        "Biryani", "Moussaka", "Pho", "Chili Con Carne", "Dim Sum", "Falafel", "Tabbouleh", "Samosa"
    ],
    "Dietary & Health Foods": [
        "Gluten-Free Bread", "Vegan Protein", "Chia Seeds", "Flax Seeds", "Hemp Seeds", "Protein Powder", 
        "Almond Flour", "Coconut Flour", "Rice Cakes", "Nutritional Yeast", "Acai Bowls", "Kale Chips", 
        "Kombucha", "Rice Crackers", "Low Carb Pasta", "Vegan Snacks", "Sugar-Free Syrup"
    ]
}

# Flatten the list of all product names across categories
all_products = [item for sublist in food_items.values() for item in sublist]

# Prepare the products table and product categories table
products = []
product_categories = []

# Assign product id and category_id to each product
category_id = 1
for category, items in food_items.items():
    category_entry = {"category_id": category_id, "category_name": category}
    product_categories.append(category_entry)

    for item in items:
        product_entry = {"product_id": len(products) + 1, "product_name": item, "product_category": category}
        products.append(product_entry)

    category_id += 1

# Ensure no duplicates in product names by shuffling the list
random.shuffle(all_products)

# Prepare the store data
stores = [
    {"store_id": 1, "store_name": "Edeka"},
    {"store_id": 2, "store_name": "Rewe"},
    {"store_id": 3, "store_name": "Lidl"},
    {"store_id": 4, "store_name": "Aldi"}
]

# Generate store-products relationships
def generate_store_products():
    store_products = []
    
    # Create a mapping from product names to product_ids (ensuring uniqueness)
    product_mapping = {product["product_name"]: product["product_id"] for product in products}

    # Ensure each product is assigned to at least one store
    for product_name in all_products:
        # Randomly choose stores for each product
        stores_for_product = random.sample(stores, random.randint(1, len(stores)))
        
        # Generate store-product pairs for the chosen stores
        for store in stores_for_product:
            product_id = product_mapping[product_name]  # Get the unique product_id
            store_products.append({"store_id": store["store_id"], "product_id": product_id})

    return store_products

# Generate store-products table
store_products = generate_store_products()

# Create DataFrames
products_df = pd.DataFrame(products)
product_categories_df = pd.DataFrame(product_categories)
store_products_df = pd.DataFrame(store_products)
store_df = pd.DataFrame(stores)
locations_berlin_df = pd.DataFrame(locations_berlin)

# Display the result
print("\nProducts:")
print(products_df.head())
print("\nProduct Categories:")
print(product_categories_df.head())
print("\nStore Products:")
print(store_products_df.head())
print("\nStores:")
print(store_df.head())
print("\nLocations:")
print(locations_berlin_df.head())

# Assert no duplicates
assert products_df['product_name'].nunique() == len(products_df)


# Save to Excel files
products_df.to_excel("products.xlsx", index=False)
product_categories_df.to_excel("product_category.xlsx", index=False)
store_products_df.to_excel("store_product.xlsx", index=False)
store_df.to_excel("store.xlsx", index=False)
locations_berlin_df.to_excel("locations.xlsx", index=False)
