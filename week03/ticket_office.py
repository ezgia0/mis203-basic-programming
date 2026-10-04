total_tickets = 0
total_revenue = 0.0
free_tickets = 0

while True:
    name = input("Customer name (or q to quit): ")
    if name.lower() == "q":
        break
        
    age = int(input("Age: "))
    
    if age < 0 or age > 120:
        print("Invalid age.")
        continue
        
    day = input("Day (weekday/weekend): ").lower()
    if day != "weekday" and day != "weekend":
        print("Invalid day.")
        continue
        
    is_student = input("Student (yes/no): ").lower()
    if is_student != "yes" and is_student != "no":
        print("Please answer yes or no.")
        continue
        
    if day == "weekday":
        base_price = 200
    else:
        base_price = 250
        
    if age < 6:
        final_price = 0
        ticket_type = "Free"
        free_tickets += 1 
    elif age >= 65:
        final_price = base_price * 0.50
        ticket_type = "Senior"
    elif age >= 6 and age <= 12:
        final_price = base_price * 0.60
        ticket_type = "Child"
    elif is_student == "yes" and age <= 25:
        final_price = base_price * 0.70
        ticket_type = "Student"
    else:
        final_price = base_price
        ticket_type = "Standard"
        
    print(f"{name}: {final_price:.2f} TRY ({ticket_type})")
    
    total_tickets += 1
    total_revenue += final_price

if total_tickets == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / total_tickets
    print(f"Tickets sold: {total_tickets}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
