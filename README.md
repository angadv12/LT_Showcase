# Exact Change Calculator

This repository contains three files that together implement a program for calculating exact change in US currency. The program is composed of:

1. `greedy_coin_algorithm.py`: Contains the greedy algorithm to calculate the minimum number of bills and coins for any amount.
2. `coin_tkinter_app.py`: Implements a GUI using Tkinter to allow users to interact with the calculator.
3. `greedy_test.py`: Contains automated tests to verify that the greedy algorithm works correctly.

## Setup and Running the Application

### Prerequisites

- Python 3.x installed on your system.

### Step-by-Step Instructions

1. **Clone the Repository**

   Clone this repository to your local machine using:

   ```sh
   git clone https://github.com/angadv12/LT_Showcase
   ```

2. **Running the Application**

   To run the GUI application:

   ```sh
   python coin_tkinter_app.py
   ```

   This will open a window where you can enter an amount in dollars, and click "Calculate Change" to see the breakdown of bills and coins needed to make the amount.

3. **Running the Tests**

   To run the automated tests to verify the algorithm:

   ```sh
   python -m unittest greedy_test.py
   ```
   This command will run all the test cases in `greedy_test.py` and provide output about whether they passed or failed.

## File Overview

### `greedy_coin_algorithm.py`
This file contains the `get_exact_change` function, which uses a greedy algorithm to determine the optimal combination of bills and coins to represent a given amount in US currency.

### `coin_tkinter_app.py`
This file provides a simple graphical user interface (GUI) using Tkinter to interact with the `get_exact_change` function. Users can enter an amount and see the exact change displayed in the GUI window.

### `greedy_test.py`
This file contains test cases for the `get_exact_change` function. The tests include a range of typical, edge, and boundary cases to ensure the algorithm works as expected.

## Note
- The skeleton for this README was generated by GPT-4o by feeding in the 3 files I made and then edited by me.