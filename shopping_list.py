# -*- coding: utf-8 -*-
import json  # Importing the JSON module for handling JSON data
import os  # Importing the OS module for system-related operations
import time  # Importing the Time module for time-related operations


def add_item(shopping_list, item, quantity):
    """Add an item with its quantity to the shopping list."""
    shopping_list[item] = quantity

def remove_item(shopping_list, item):
    """Remove an item from the shopping list if it exists."""
    if item in shopping_list:
        del shopping_list[item]

def view_shopping_list(shopping_list):
    """Display the shopping list with items and their quantities."""
    for item, quantity in shopping_list.items():
        print(f"{item}: {quantity}")
    print()
    print("Press enter to continue")
    input()

def save_shopping_list(shopping_list, file_name):
    """Save the shopping list to a JSON file."""
    with open(file_name, "w") as file:
        json.dump(shopping_list, file)

def load_shopping_list(file_name):
    """Load the shopping list from a JSON file."""
    with open(file_name, "r") as file:
        return json.load(file)

def manage_shopping_list(shopping_list, file_name=None):
    """Manage the shopping list (add, remove, view, save, or exit)."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console screen

        print("""
        1. Add item
        2. Remove item
        3. View list
        4. Save and exit
        5. Exit without saving""")

        choice = input("Choose an option: ")

        match choice:
          case "1":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            add_item(shopping_list, item, quantity)
          case "2":
            item = input("Enter the item name: ")
            remove_item(shopping_list, item)
          case "3":
            view_shopping_list(shopping_list)
            choice = 3
          case "4":
            if file_name is None:
                file_name = input("Enter the file name to save: ")
            if not file_name.endswith(".json"):
                file_name += ".json"
            save_shopping_list(shopping_list, file_name)
            break
          case "5":
            break
          case _:
              print("Invalid option")
              time.sleep(1)

def menu_inicial():

    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console screen

        print(f"""
        Shopping List Manager
        =====================
        1. Create a new shopping list
        2. Load an existing list
        3. Exit
        """)

        choice = input("Choose an option: ")

        match choice:
          case "1":
              shopping_list = {}
              manage_shopping_list(shopping_list)
          case "2":
              print("Available lists:")
              files = [file for file in os.listdir() if file.endswith(".json")]
              if not files:
                  print("No lists found")
                  time.sleep(2)
                  continue
              for i, file in enumerate(files, 1):
                  print(f"{i}. {file}")
              choice = int(input("Choose a list to load (0 if none): "))
              if choice == 0:
                  continue
              if choice < 0 or choice > len(files):
                  print("Invalid option")
                  time.sleep(1)
                  continue
              file_name = files[choice - 1]
              shopping_list = load_shopping_list(file_name)
              manage_shopping_list(shopping_list, file_name)
          case "3":
              break
          case _:
              print("Invalid option")
              time.sleep(1)

opcao = menu_inicial()

def main():
        menu_inicial

if __name__ == "__main__":
    main()