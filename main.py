import openai
from dotenv import load_dotenv
import os

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


if __name__ == "__main__":
    # Initialize the assistant and display the setup messages
    messages = initialize_assistant()
    print("Assistant initialized with messages:", messages)
