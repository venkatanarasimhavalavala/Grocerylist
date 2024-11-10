# Grocerylist
Here’s a suggested README.md content for your grocery list project:

---

# Grocery List Manager 🛒

This is a simple Python program that allows users to manage their grocery list. The program helps users add, remove, and view items in a grocery list while ensuring no duplicate items are added.

## Features

- **Add Items**: Add grocery items to the list.
- **Remove Items**: Remove specific items from the list.
- **View List**: View all items currently in the grocery list.
- **Avoid Duplicates**: Automatically prevents duplicate items from being added.
- **Exit**: Close the program when you're done.

## How It Works

1. **User Input**: The user is prompted to choose from the available options.
2. **Operations**:
   - Add an item: Adds a new item to the grocery list.
   - Remove an item: Removes a specified item from the list.
   - View the list: Displays all items currently in the grocery list.
   - Exit: Exits the program.

## Code Explanation

- **Set for Groceries (`GL`)**: The program uses a Python set to store grocery items, ensuring that no duplicates are added.
- **Functions**:
  - `adding()`: Adds an item to the list.
  - `removing()`: Removes an item if it exists in the list.
  - `viewing()`: Displays the current list of grocery items.
  - `quit()`: Exits the program.

## Usage

1. Clone or download the repository.
2. Run the script in your Python environment:
   ```bash
   python groceries_list.py
   ```
3. Follow the prompts to manage your grocery list.

## Sample Output

```plaintext
Groceries list

Select the options you want
1. Add an item
2. Remove an item
3. View the list
4. Exit
Enter your choice: 1
Enter the item you want to add: apple
apple, has been added to the list

Select the options you want
1. Add an item
2. Remove an item
3. View the list
4. Exit
Enter your choice: 3
Your list is:
apple
```

## Requirements

- Python 3.x


---

Feel free to modify the content as per your preference or additional features!