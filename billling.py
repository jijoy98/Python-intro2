def read_products(filename):
    products = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                product_id, name, price = line.strip().split(',')
                products.append({
                    'id': product_id,
                    'name': name,
                    'price': float(price)
                })
            except ValueError:
                print(f"Error processing line: {line}. Skipping invalid product.")
                continue
    return products

def select_products(products):
    selected_products = []
    while True:
        product_id = input("Enter the ProductID to add to the cart (or 'done' to finish): ")
        if product_id.lower() == 'done':
            break
        try:
            quantity = int(input("Enter the quantity: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        for product in products:
            if product['id'] == product_id:
                # Check if product already in cart
                for selected_product in selected_products:
                    if selected_product['id'] == product_id:
                        selected_product['quantity'] += quantity
                        break
                else:
                    selected_products.append({
                        'id': product['id'],
                        'name': product['name'],
                        'price': product['price'],
                        'quantity': quantity
                    })
                break
        else:
            print("Invalid ProductID")
    return selected_products

def calculate_total(selected_products):
    total = 0
    for product in selected_products:
        total += product['price'] * product['quantity']
    return total

def write_transaction(filename, selected_products, total):
    with open(filename, 'a') as file:
        file.write("Transaction:\n")
        for product in selected_products:
            file.write("{:<10} {:<15} ${:<10.2f} x {}\n".format(product['id'], product['name'], product['price'], product['quantity']))
        file.write("Total: ${:.2f}\n".format(total))
        file.write("\n")

def display_confirmation(selected_products, total):
    print("\nYour Cart:")
    print("{:<10} {:<15} {:<10} {:<10}".format('ProductID', 'ProductName', 'Price', 'Quantity'))
    for product in selected_products:
        print("{:<10} {:<15} ${:<10.2f} {:<10}".format(product['id'], product['name'], product['price'], product['quantity']))
    print(f"Total: ${total:.2f}")
    confirm = input("Do you want to proceed with the transaction? (yes/no): ").lower()
    return confirm == 'yes'

def main():
    products = read_products('products.txt')
    selected_products = select_products(products)
    total = calculate_total(selected_products)

    if display_confirmation(selected_products, total):
        write_transaction('transactions.txt', selected_products, total)
        print("Transaction details have been saved to 'transactions.txt'.")
    else:
        print("Transaction has been cancelled.")

if __name__ == "__main__":
    main()
