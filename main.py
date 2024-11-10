import openai
from dotenv import load_dotenv
import os
import json

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


if __name__ == "__main__":
    # Initialize the assistant and display the setup messages
    messages = initialize_assistant()
    
    # Load and display the product catalog
    product_catalog = load_product_catalog()
    print("Product Catalog:", product_catalog)

    # Test getProductInfo function
    product_name = "EcoFriendly Water Bottle"
    product_info = getProductInfo(product_name, product_catalog)
    print(f"Product Info for '{product_name}':", product_info)

    # Test checkStock function
    stock_status = checkStock(product_name, product_catalog)
    print(f"Stock Status for '{product_name}':", "In Stock" if stock_status else "Out of Stock")