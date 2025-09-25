from typing import Any
def prodotto(name:str, price: float, quantity: int) -> dict:
    prod = {"Nome": name,"Prezzo": price, "Quantità": quantity}
    
    return prod


def addProd(cart: list[dict[str, Any]], product: dict[str, Any]) -> None:
    cart.append(product)   
    


def remove_product(cart: list[dict[str, Any]], product_name: str) -> list[dict[str, Any]]:
    updated_cart: list[dict[str, Any]] = []
    for p in cart:
        if p['name'] != product_name:
            updated_cart.append(p)
    return updated_cart

def viewCart(cart: list[dict[str, Any]]) -> list[dict[str, Any]]:
    print("Il carrello contiene:")
    for prod in cart:
        print(f"{prod['Nome']}: {prod['Quantità']}, al prezzo di € {prod['Prezzo']} l'uno.")



def calculate_total(cart: list[dict[str, Any]], discount_rate: float = 0.10) -> dict[str, float]:
    subtotal: float = sum(product['price'] * product['quantity'] for product in cart)
    discount: float = discount_rate
    tax: float = 0.22 


def summary(cart: list[dict[str, Any]], sum: float) -> None:
    viewCart(cart)
    for prod in cart:
        total_price: float = prod["price"] * prod["quantity"]
    prod(f"{prod['Nome'] } - Quantity:{ prod['Quantità']}, unit price: € {prod['Prezzo']}. total: {prod['total_price']}")

    totals: dict[str, float] = calculate_total(cart)
    print("\nTotals:")
    print(f"Subtotal: €{totals['subtotal']}")
    print(f"Discount Applied: {totals['discount']}%")
    print(f"Tax: {totals['tax']}%")
    print(f"Final Total: €{round(totals['total'], 2)}")        






product1: dict[str, Any] = prodotto("Laptop", 900.0, 1)
product2: dict[str, Any] = prodotto("Mouse", 25.0, 2)
product3: dict[str, Any] = prodotto("Backpack", 50.0, 1)

# Initialize an empty shopping cart
cart: list[dict[str, Any]] = []

# Add products to the cart
addProd(cart, product1)
addProd(cart, product2)
addProd(cart, product3)

# Remove the "Mouse" product from the cart
cart = remove_product(cart, "Mouse")

# Print a full summary of the cart including totals
summary(cart)