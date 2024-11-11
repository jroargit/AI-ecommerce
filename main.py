import openai
from dotenv import load_dotenv
import os
import json
import re

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to initialize and set up the assistant
def initialize_assistant():
    # Define the initial system message to instruct the assistant
    messages = [
        {"role": "system", "content": "You are ShopBot, an AI assistant for an e-commerce platform. You help users with product information queries."}
    ]
    return messages


# Function to load product catalog from JSON file
def load_product_catalog():
    try:
        with open("products.json", "r") as file:
            products = json.load(file)
        print("Product catalog loaded successfully.")
        return products
    except FileNotFoundError:
        print("Error: Product catalog file not found.")
        return []
    

# Function to get product information by name
def getProductInfo(product_name, catalog):
    """
    Retrieve product information by name.
    :param product_name: Name of the product to search.
    :param catalog: List of products.
    :return: Dictionary with product details or None if not found.
    """
    for product in catalog:
        if product["name"].lower() == product_name.lower():
            return {
                "id": product["id"],
                "name": product["name"],
                "description": product["description"],
                "price": product["price"],
                "stock": product["stock"]
            }
    return None

# Function to check if a product is in stock
def checkStock(product_name, catalog):
    """
    Check stock availability for a given product.
    :param product_name: Name of the product to check.
    :param catalog: List of products.
    :return: Boolean indicating stock availability, or None if not found.
    """
    product_info = getProductInfo(product_name, catalog)
    if product_info:
        return product_info["stock"]
    return None


# Function to process user query and get response from ShopBot
# Global variable to remember the last product queried
last_queried_product = None

def ask_shopbot(query, catalog):
    """
    Process user query through ShopBot and return response.
    :param query: User query string.
    :param catalog: List of products.
    :return: ShopBot response string.
    """
    global last_queried_product  # Access the global variable
    messages = initialize_assistant()
    messages.append({"role": "user", "content": query})

    # Search for the product name directly in the catalog
    found_product = None
    for product in catalog:
        if product["name"].lower() in query.lower():
            found_product = product
            last_queried_product = product  # Update last queried product
            break

    if found_product:
        # Determine if the query is about product details or stock
        if "tell me about" in query.lower():
            response = (
                f"Product Name: {found_product['name']}\n"
                f"Description: {found_product['description']}\n"
                f"Price: ${found_product['price']}\n"
                f"Available: {'Yes' if found_product['stock'] else 'No'}"
            )
        elif "is it available" in query.lower():
            response = f"Yes, '{found_product['name']}' is in stock." if found_product["stock"] else f"No, '{found_product['name']}' is out of stock."
        else:
            response = "I'm here to help you with product information or stock availability. Please ask me about a product."
    elif "is it available" in query.lower() and last_queried_product:
        # Use the last queried product if it exists
        stock_status = last_queried_product["stock"]
        response = f"Yes, '{last_queried_product['name']}' is in stock." if stock_status else f"No, '{last_queried_product['name']}' is out of stock."
    else:
        response = "Sorry, I couldn't find any information on the specified product."

    return response




if __name__ == "__main__":
    # Initialize the assistant and display the setup messages
    messages = initialize_assistant()
    
    # Load and display the product catalog
    product_catalog = load_product_catalog()
    print("Product Catalog:", product_catalog)

    # Sample queries to test the assistant
    user_query_1 = "Tell me about the EcoFriendly Water Bottle."
    print("User:", user_query_1)
    print("ShopBot:", ask_shopbot(user_query_1, product_catalog))

    user_query_2 = "Is it available?"
    print("\nUser:", user_query_2)
    print("ShopBot:", ask_shopbot(user_query_2, product_catalog))