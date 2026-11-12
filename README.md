# Expense Tracker

A command-line expense tracker written in Python. You can add, view, total, and delete expenses from a simple menu.

## Features

- Add an expense with an amount, category, and short note
- View all expenses in a numbered list
- Show the total amount spent
- Delete an expense by its number

## How to run

1. Install Python 3.
2. Download or clone this repository.
3. In a terminal, run:

```
python main.py
```

## Example menu

```
Welcome to the expense tracker!
1. Add expense
2. View expenses
3. Total expenses
4. Delete expense
5. Exit
```

## How it works

Each expense is stored as a dictionary (`amount`, `category`, `note`), and all expenses are kept in a list. Each menu option calls its own function.

## Current limitations

- Expenses are not saved, so they disappear when you close the program.
- Typing a letter where a number is expected will crash the program.

## Planned improvements

- Save expenses to a file
- Store data in SQLite
- Handle invalid input
- Add tests with pytest
- Turn it into a Flask web app

## Author

Pudeep Orsu, Computer Science student at Wichita State University
