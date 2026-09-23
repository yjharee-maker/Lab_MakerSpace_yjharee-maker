# Makerspace Equipment Checkout System

## Overview

A Python terminal application for managing makerspace members, equipment, and equipment loans.

The application uses **Python, OOP, and SQLite**.

## Run the Application

```
python3 main.py

```

## Classes

### Member

Manages makerspace members.

* Register
* List
* Update
* Delete
* Search

### Equipment

Manages makerspace equipment.

* Register
* List
* Update
* Delete
* Search
* Track availability

### Loan

Manages equipment checkouts and returns.

* Create loans
* Return equipment
* Search loans
* View loan history
* View current loans

## Database Tables

The SQLite database contains three main tables:

* `members` — stores member information
* `equipment` — stores equipment and availability
* `loans` — stores checkout and return information

## Reports

The application generates:

* Current loan reports
* Member loan history
* Equipment loan history

Reports are exported as `.txt` files in the `reports/` directory.

## AI Disclosure

AI tools were used during development to assist with:

* Understanding programming concepts
* Debugging
* Code review

