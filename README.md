# Shopping Cart Project

This is an app designed to accept cashier inputs at checkout. This app is designed to have adjustable tax rates for various regional grocery stores, as well as the option to send e-mail receipts. 

## Prerequisites
  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Navigate to the app's folder from the command line.:

```sh
cd shopping_cart_exercise
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n shopping-env python=3.8
conda activate shopping-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In in the root directory of your local repository, create a new file called ".env" by using the command:

```sh
cd touch .env
```
Update the contents of the ".env" file to specify your tax rate, Sendgrid API Key, and comapny e-mail address for e-mail receipts:

```sh
TAX_RATE = "ENTER TAX RATE"

SENDGRID_API = "ENTER API KEY"

SENDGRID_EMAIL = "ENTER COMPANY EMAIL"
```

## Usage

Run the app:

```py
shopping_cart.py
```
When prompted with inputs, the user shall input the id number of the item the customer is buying. Once all items have been entered, the user must enter "done" to show the final cost.

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.
