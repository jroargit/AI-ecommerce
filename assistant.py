import re
from product_catalog import load_product_catalog, getProductInfo, checkStock


# Function to initialize and set up the assistant
def initialize_assistant():
    # Define the initial system message to instruct the assistant
    messages = [
        {"role": "system", "content": "You are ShopBot, an AI assistant for an e-commerce platform. You help users with product information queries."}
    ]
    return messages

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