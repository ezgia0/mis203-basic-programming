room_types = {
    "1": {"name": "Economy Room", "min_cap": 1, "max_cap": 2, "price_per_person": 1500.00},
    "2": {"name": "Superior Room", "min_cap": 2, "max_cap": 3, "price_per_person": 2500.00},
    "3": {"name": "Family Room", "min_cap": 2, "max_cap": 5, "price_per_person": 2000.00},
    "4": {"name": "King Suite", "min_cap": 1, "max_cap": 4, "price_per_person": 5000.00}
}

print("=== HOTEL RESERVATION SYSTEM ===")
print("Available Room Types:")
print("1. Economy Room (1-2 Guests) - 1500.00 TRY per person/night")
print("2. Superior Room (2-3 Guests) - 2500.00 TRY per person/night")
print("3. Family Room (2-5 Guests) - 2000.00 TRY per person/night")
print("4. King Suite (1-4 Guests) - 5000.00 TRY per person/night")

room_choice = input("Select a room type (1-4): ").strip()

while room_choice not in room_types:
    room_choice = input("Invalid selection! Please enter a number between 1 and 4: ").strip()

selected_room = room_types[room_choice]

while True:
    total_guests = int(input(f"Enter number of guests ({selected_room['min_cap']}-{selected_room['max_cap']}): "))
    if selected_room["min_cap"] <= total_guests <= selected_room["max_cap"]:
        break
    print(f"Error: {selected_room['name']} capacity must be between {selected_room['min_cap']} and {selected_room['max_cap']} guests.")

nights = int(input("Enter number of nights to stay: "))
while nights <= 0:
    nights = int(input("Invalid duration! Please enter at least 1 night: "))

guests = []
total_amount_per_night = 0.0

for i in range(1, total_guests + 1):
    print(f"\n--- Guest {i} ---")
    full_name = input(f"Enter full name for Guest {i}: ").strip()
    is_child = input("Is this guest a child? (yes/no): ").strip().lower() == "yes"
    
    age = 0
    discount_rate = 0.0
    
    if is_child:
        age = int(input("Enter child's age: "))
        if 0 <= age <= 6:
            discount_rate = 1.00
        elif 6 < age <= 10:
            discount_rate = 0.40
        else:
            discount_rate = 0.00
            
    base_price = selected_room["price_per_person"]
    guest_price = base_price * (1.0 - discount_rate)
    total_amount_per_night += guest_price
    
    guests.append({
        "name": full_name,
        "is_child": is_child,
        "age": age if is_child else None,
        "nightly_price": guest_price
    })

total_stay_cost = total_amount_per_night * nights

print("\n" + "=" * 50)
print("RESERVATION SUMMARY")
print("=" * 50)
print(f"Room Type: {selected_room['name']}")
print(f"Total Guests: {total_guests}")
print(f"Duration of Stay: {nights} night(s)")
print("-" * 50)

for idx, g in enumerate(guests, 1):
    guest_type = f"Child ({g['age']} yrs)" if g['is_child'] else "Adult"
    print(f"Guest {idx}: {g['name']} - {guest_type} - Nightly Rate: {g['nightly_price']:.2f} TRY")

print("-" * 50)
print(f"Nightly Subtotal: {total_amount_per_night:.2f} TRY")
print(f"TOTAL AMOUNT DUE: {total_stay_cost:.2f} TRY")
print("=" * 50)
