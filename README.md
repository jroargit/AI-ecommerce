# AI E-Commerce Assistant (ShopBot)

This project implements an AI e-commerce assistant called **ShopBot** using OpenAI’s GPT-4o API. ShopBot can respond to questions about products in a catalog, provide product details, and check stock availability.

## Project Structure

```
AI-ecommerce/
├── main.py               # Main file to run the project
├── assistant.py          # Core assistant logic and `ask_shopbot` function
├── product_catalog.py    # Functions to load and handle the product catalog
├── products.json         # Product catalog in JSON format
├── .env                  # Environment file (stores the API key)
└── .gitignore            # Lists files ignored by Git (includes .env)
```

### Key Files
- **`products.json`**: Contains the product catalog.
- **`product_catalog.py`**: Manages loading and querying the product catalog.
- **`assistant.py`**: Contains the assistant logic to handle user queries.
- **`main.py`**: Runs the project and simulates user interactions.

## Prerequisites

1. **Python** installed on your system (recommended: Python 3.7 or above).
2. **OpenAI API Key** to use the GPT-4o model.

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/jroargit/AI-ecommerce.git
   cd AI-ecommerce
   ```

2. **Install dependencies**:
   ```bash
   pip install openai python-dotenv
   ```

3. **Set up your OpenAI API Key**:
   - Create a `.env` file in the root of the project.
   - Add your API key in the `.env` file as follows:
     ```plaintext
     OPENAI_API_KEY=sk-<your_api_key_here>
     ```

4. **Create or check the product catalog**:
   - Ensure the `products.json` file is in the project root and contains the product catalog in JSON format.

## Running the Project

To run the project and test the assistant, use the following command:

```bash
python main.py
```

This will simulate a conversation between the user and ShopBot in the console. You’ll see how ShopBot responds to queries, such as fetching product details or checking stock availability.

### Example Output

```plaintext
User: Tell me about the EcoFriendly Water Bottle.
ShopBot: 
Product Name: EcoFriendly Water Bottle
Description: A reusable water bottle made from eco-friendly materials.
Price: $15.99
Available: Yes

User: Is it available?
ShopBot: Yes, 'EcoFriendly Water Bottle' is in stock.
```

## Code Explanation

1. **`product_catalog.py`**: Loads the catalog from `products.json` and provides functions to:
   - `getProductInfo(product_name)`: Returns product details.
   - `checkStock(product_name)`: Checks stock availability.

2. **`assistant.py`**: Contains `ask_shopbot`, which parses user queries and responds using the product catalog.
   - Uses a global variable `last_queried_product` to remember the last product queried.

3. **`main.py`**: Runs the assistant and simulates user queries.

## Additional Notes

- **Expanding the Catalog**: You can add more products to `products.json`, ensuring each product has an ID, name, description, price, and stock status (`true` or `false`).
- **Environment Configuration**: Don’t forget to include `.env` in `.gitignore` to keep your API key secure.

---
