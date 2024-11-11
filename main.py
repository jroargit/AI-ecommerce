import openai
from dotenv import load_dotenv
import os
from product_catalog import load_product_catalog
from assistant import ask_shopbot, initialize_assistant

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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