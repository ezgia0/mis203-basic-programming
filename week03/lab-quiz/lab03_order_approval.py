order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
is_member = input("Is the customer a member? (yes/no): ").strip().lower() == "yes"

if requested_quantity <= 0 or requested_quantity > available_stock:
    print("Order rejected: Invalid quantity or insufficient stock.")
else:
    final_price = order_amount
    
    if is_member and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Order approved: Member discount of 10% applied.")
    else:
        print("Order approved: Standard pricing applied.")
        
    print(f"Final price: {final_price:.2f} TRY")
