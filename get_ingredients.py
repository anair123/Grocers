import openai
from openai import OpenAI
import config
import os
import pandas as pd
from fuzzywuzzy import process


products = pd.read_excel("products.xlsx")
store_product = pd.read_excel("store_product.xlsx")
store = pd.read_excel("store.xlsx")     
df_final = pd.DataFrame()

# -------------------------------------- Get list of ingredients for a given dish from OpenAI
client = OpenAI(
    api_key=config.openai_apikey,  # This is the default and can be omitted
)

print("Enter your dish: ")
dish = input()
# Example: Call the function with a custom prompt
prompt = f"List the ingredients for the following dish: {dish}. Separate each ingredient by '-'."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
            ],
        }
    ],
)

response_content = response.choices[0].message.content
# Print the response from the model
print(f'Ingredients for {dish}: \n{response_content}')
ingredients = response_content.split('-')
ingredients = [i.strip(" ") for i in ingredients if i]
print(f"Number of ingredients: {len(ingredients)}")
print(f'Ingredients: {ingredients}')


# ----------------------------------------------------- Find the product_ids for each product ------------------------------ 

# Function to get the best fuzzy match for each item
def get_best_match(query, choices, threshold=85):
    # Use fuzzywuzzy to get the best match
    best_match, score = process.extractOne(query, choices)
    if score >= threshold:
        return best_match
    else:
        return "No matches"  # Return None if the match is below the threshold

# Create a new column in the DataFrame with the matched food items from food_list
products['matched_food'] = products['product_name'].apply(lambda x: get_best_match(x, ingredients))

matched_products = products[products['matched_food']!="No matches"]

matched_product_ids = matched_products[['product_id', 'product_name', 'matched_food']]
matched_product_ids = matched_product_ids.merge(store_product, how='left', on='product_id')
matched_product_ids = matched_product_ids.merge(store, how='left', on='store_id')
print(matched_product_ids.head(10))



# get all the product_ids while minimizing unique number of product_ids (greedy algorithm)

desired_products = matched_product_ids['product_id'].unique()

# greedy set cover algorithm
selected_stores = set()
remaining_products = set(desired_products)

while remaining_products: # run while there are remaining products
    store_coverage = (
        matched_product_ids[matched_product_ids['product_id'].isin(remaining_products)]
        .groupby('store_id')['product_id']
        .nunique()
        .sort_values(ascending=False)
    )

    # get the store with the most product coverage
    best_store = store_coverage.idxmax()
    selected_stores.add(best_store)

    # remove the covered products from the remaining list
    covered_products = set(
        matched_product_ids[matched_product_ids['store_id']==best_store]['product_id']
    )

    remaining_products -= covered_products

result = matched_product_ids[matched_product_ids['store_id'].isin(selected_stores)]
print("")
print(result)