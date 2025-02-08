import pandas as pd
import random

# Store Data (as provided)
stores = [
    {"store_id": 1, "store_name": "Edeka"},
    {"store_id": 2, "store_name": "Rewe"},
    {"store_id": 3, "store_name": "Lidl"},
    {"store_id": 4, "store_name": "Aldi"}
]

# Food Items Categories (as provided)
food_items = {
    "Grains & Pasta": [
        "Rice", "Oats", "Pasta", "Quinoa", "Couscous", "Barley", "Polenta", "Buckwheat", "Amaranth", 
        "Spaghetti", "Macaroni", "Fusilli", "Lasagna Sheets", "Whole Wheat Pasta", "Egg Noodles"
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
        "Ricotta", "Feta", "Parmesan", "Mozzarella", "Goat Cheese", "Greek Yogurt"
    ],
    "Baking & Cooking": [
        "Baking Powder", "Flour", "Sugar", "Yeast", "Vanilla Extract", "Baking Soda", "Cornstarch", 
        "Chocolate Chips", "Cocoa Powder", "Honey", "Molasses", "Maple Syrup", "Olive Oil", 
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
        "Chicken", "Beef", "Pork", "Fish", "Sausages", "Turkey", "Lamb", "Bacon", "Steak", 
         "Chicken Breast", "Ground Beef", "Chicken Thighs", "Veal", "Bison", "Venison", "Tofu", "Tempeh", 
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
        "Ketchup", "Mayonnaise", "Hot Sauce", "Vinegar", "Salad Dressing", 
        "Barbecue Sauce", "Mustard", "Teriyaki Sauce", "Worcestershire Sauce", "Pesto", "Tomato Sauce", 
        "Mango Chutney", "Tartar Sauce", "Garlic Butter"
    ],
    "Spices & Herbs": [
        "Salt", "Pepper", "Cumin", "Cinnamon", "Paprika", "Oregano", "Basil", "Garlic Powder", "Chili Powder", 
        "Turmeric", "Thyme", "Rosemary", "Bay Leaves", "Parsley", "Coriander", "Saffron", "Nutmeg", "Ginger"
    ],
    "Breakfast": [
        "Cereal", "Granola", "Pancake Mix", "Jam", "Eggs",
        "Oatmeal", "Toast", "Smoothies", "Nut Butter", "Yogurt Parfait"
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
        "Almond Milk", "Soy Milk", "Coconut Milk", "Oat Milk", "Vegan Cheese", "Vegan Butter", 
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
        "Almond Flour", "Coconut Flour", "Nutritional Yeast", "Acai Bowls", "Kale Chips", 
        "Kombucha", "Rice Crackers", "Low Carb Pasta", "Vegan Snacks", "Sugar-Free Syrup"
    ]
}

# Prepare the Products Table with unique product_id and product_name
product_id = 1
products = []

for category, items in food_items.items():
    for item in items:
        product_entry = {
            "product_id": product_id,
            "product_name": item,
            "category": category
        }
        products.append(product_entry)
        product_id += 1

# Prepare the Store_Products Table (Mapping products to stores)
store_products = []

for product in products:
    # Randomly assign this product to stores
    stores_for_product = random.sample(stores, random.randint(1, len(stores)))
    
    # Create mapping
    for store in stores_for_product:
        store_products.append({
            "store_id": store["store_id"],
            "product_id": product["product_id"]
        })

# Create DataFrames for the tables
products_df = pd.DataFrame(products)
store_products_df = pd.DataFrame(store_products)

# Display the DataFrames (tables)
print("\nProducts Table:")
print(products_df.head())

print("\nStore_Products Table (Mapping Products to Stores):")
print(store_products_df.head())

# Optional: Ensure uniqueness

dup = products_df[products_df['product_name'].duplicated()]
print(dup)
assert products_df['product_name'].nunique() == len(products_df)
assert products_df['product_id'].nunique() == len(products_df)

products_df.to_excel("products.xlsx", index=False)
store_products_df.to_excel("store_product.xlsx", index=False)
