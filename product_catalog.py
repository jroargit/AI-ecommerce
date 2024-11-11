import json

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