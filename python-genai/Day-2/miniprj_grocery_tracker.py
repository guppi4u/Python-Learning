# Program for grocery tracker


def grocery_tracker():

        welcome_msg = """

            ╔══════════════════════════════════════╗
            ║   Grocery Price Tracker              ║ 
            ╚══════════════════════════════════════╝

                Menu:
                1. Add item
                2. View all items
                3. Calculate total
                4. Filter by category
                5. Find most/least expensive
                6. Remove item
                7. Exit
            """
        print(welcome_msg)

    # to list items
        items = []
    # to store items
    # store_item={"user_item":" ","user_price":0,"user_quantity":0,"category":" "}

        while True:
            user_input = int(
                input("Hi Welcome , please enter your choice form the menu(1-7) :")
            )
            if user_input == 1:
                # Create a NEW dictionary for each item
                store_item = {
                    "user_item": input("Enter your item: "),
                    "user_price": float(input("Enter product price: ")),
                    "user_quantity": int(input("Enter item quantity: ")),
                    "category": input("Enter item category: "),
                }
                items.append(store_item)
                print("Item added successfully!!!")

            # print(f'{store_item}')

            elif user_input == 2:
            # ✅ FIXED - Loop through ALL items in the list
                if len(items) == 0:
                    print("No items as added yet")

                else:
                    print("""
                    
                    ═══════════════════════════════════════
                            All Grocery Items:
                    ═══════════════════════════════════════""")

                # iterating through entire dictionary
                for index, item in enumerate(items, 1):
                    total_value = item["user_price"] * item["user_quantity"]

                    print(
                        f"""
                            {index}.{item['user_item']}
                            Price : ${item['user_price']} x {item['user_quantity']} = ${total_value}
                            Category: {item["category"]}  
                            """)
                print(
                """    
                            ========================""")
            # Calculating user total
            elif user_input == 3:
                if len(items) == 0:
                    print("No items as added yet")

                else:
                    total = sum(item['user_price'] * item['user_quantity'] for item in items)
                    print(f"\n╔═══════════════════════════════════════╗")
                    print(f"║ Total Value of All Items: ${total:.2f}")
                    print(f"╚═══════════════════════════════════════╝\n")

            # Filter by category 
            elif user_input == 4:
                if len(items) == 0:
                    print("No items as added yet!\n")

                else: 
                    category_search = input("Enter category to filter: ").lower()
                    filtered_items = [item for item in items if item["category"].lower() == category_search]
                     
                     #checking if filtered items are 0 or not 
                    if len(filtered_items) == 0:
                        print(f"No items found in category '{category_search}'\n")
                    else:
                        print(f"\n═══════════════════════════════════════")
                        print(f"Items in '{category_search}' category:")
                        print(f"═══════════════════════════════════════")
                        for index, item in enumerate(filtered_items, 1):
                            total_value =item['user_price'] * item['user_quantity']
                            print(f'''
                                    {index}. {item["user_item"]}
                                    Price: ${item["user_price"]} × {item["user_quantity"]} = ${total_value}''')
                    print(f"═══════════════════════════════════════\n")
            
            # Find most/least expensive
            elif user_input == 5:
                if len(items) == 0:
                    print("No items added yet!\n")
                else:
                    most_expensive = max(items, key=lambda x: x["user_price"])
                    least_expensive = min(items, key=lambda x: x["user_price"])
                
                    print(f'''
                    ╔═══════════════════════════════════════╗
                    ║ Most Expensive Item:
                    ║ {most_expensive["user_item"]} - ${most_expensive["user_price"]}
                    ╠═══════════════════════════════════════╣
                    ║ Least Expensive Item:
                    ║ {least_expensive["user_item"]} - ${least_expensive["user_price"]}
                    ╚═══════════════════════════════════════╝
                                                                    ''')
                    
            elif user_input == 6:
            # Remove item
                if len(items) == 0:
                    print("No items to remove!\n")
                else:
                    print("\nItems available:")
                    for index, item in enumerate(items, 1):
                        print(f"{index}. {item['user_item']}")
                
                try:
                    item_index = int(input("Enter item number to remove: ")) - 1
                    if 0 <= item_index < len(items):
                        removed_item = items.pop(item_index)
                        print(f"✓ '{removed_item['user_item']}' removed successfully!\n")
                    else:
                        print("Invalid item number!\n")
                except ValueError:
                    print("Please enter a valid number!\n")
            
            elif user_input == 7:
                print("\nThank you for using Grocery Tracker!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-7.\n")
                

grocery_tracker()
