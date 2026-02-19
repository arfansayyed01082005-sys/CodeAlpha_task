📈 Task 2: Stock Portfolio Tracker

📌 Overview

This project is a console-based Stock Portfolio Management program created using Python.
It helps users calculate the total value of their stock investments by entering stock symbols and the number of shares they own.

The program uses predefined stock prices and performs calculations automatically. It also gives the option to store the results in a file for future reference.

This task is helpful for beginners who want to understand how Python can be used for basic financial calculations and data handling.

🎯 Goal

The main objective of this task is to create a simple system that:

Accepts stock names from the user

Accepts the number of shares purchased

Uses fixed prices stored inside the program

Calculates the total investment value

The focus is on building logical thinking and improving understanding of Python fundamentals.

🛠 Features

Stores stock prices inside the program

Allows the user to enter multiple stocks

Calculates the value of each stock separately

Displays the overall portfolio value

Option to export results into a file

Handles incorrect stock names safely

Easy-to-read console output

📚 Concepts Used 

Dictionary Data Structure:
Used to store stock symbols and their prices in key-value format (Example: "AAPL": 180).

User Interaction (input/output):
Takes information from the user using input() and shows results using print().

Loops:
Used to allow the user to enter more than one stock.

Decision Making (if-else):
Checks whether the entered stock name exists in the price list.

Mathematical Calculations:
Multiplies price × quantity to find total value.

File Writing (Optional):
Saves portfolio details into .txt or .csv files for record keeping.

🧾 Example Stock Prices (Hardcoded in Program)

{
 "AAPL": 180,
 "TSLA": 250,
 "GOOGL": 140,
 "MSFT": 330,
 "AMZN": 135
}

▶️ How to Run

Make sure Python 3 is installed on your computer.

Save the file with the name:

CodeAlpha_stock_portfolio_tracker.py

Open Command Prompt or Terminal in the file location.

Run the program using:

CodeAlpha_stock_portfolio_tracker.py

Follow the instructions shown on the screen to enter stock details.

💾 Output Files

If the save option is selected, the program can create:

portfolio.txt → A simple readable summary file

portfolio.csv → A file that can be opened in Excel

These files store the total investment details entered by the user.