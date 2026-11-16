# Data Processing Lab — Object-Oriented Programming

## 1. Lab Overview

This project demonstrates how to refactor a Python data-processing program from procedural code to object-oriented programming (OOP).

The program loads CSV datasets, performs data-processing operations, and manages multiple tables using a simple in-memory database.

In Commit 4, a `DB` class is introduced to store and search tables. A `join()` method is also added to the `Table` class to combine information from two tables using a common key.

The project uses two datasets:

- **Cities.csv** — Contains city names, countries, latitude, longitude, and temperature.
- **Countries.csv** — Contains country information, including population, EU membership, and coastline availability.

## 2. Project Structure

```text
data-processing-lab/
│
├── Cities.csv
├── Countries.csv
├── data_processing.py
├── refactoring.py
├── OOP_cty.py
└── README.md
```

**File Descriptions:**

- `Cities.csv`: Dataset containing city information.
- `Countries.csv`: Dataset containing country information.
- `data_processing.py`: Commit 1 — Procedural data processing.
- `refactoring.py`: Commit 2 — Refactoring using reusable functions.
- `OOP_cty.py`: Commits 3–4 — Object-oriented implementation with database and table operations.
- `README.md`: Project documentation.

## 3. Design Overview

### DataLoader Class

The `DataLoader` class is responsible for reading CSV files and converting their contents into lists of dictionaries.

**Attributes:**

- `base_path`: Stores the directory containing the CSV files.

**Methods:**

- `__init__(base_path=None)`: Initializes the file path using `pathlib.Path`.
- `load_csv(filename)`: Reads a CSV file using `csv.DictReader` and returns a list of dictionaries.

### DB Class

The `DB` class represents a simple in-memory database that manages multiple tables.

**Attributes:**

- `tables`: A list containing Table objects.

**Methods:**

- `__init__()`: Initializes an empty database.
- `insert(table)`: Inserts a Table object into the database.
- `search(table_name)`: Searches for a table by name and returns the matching Table object, or `None` if not found.

### Table Class

The `Table` class represents tabular data and provides operations for filtering, aggregation, and joining.

**Attributes:**

- `table_name`: Stores the table name.
- `table`: Stores data as a list of dictionaries.

**Methods:**

- `__init__(table_name, table)`: Initializes a Table object.
- `filter(condition)`: Returns a new Table containing rows that satisfy a condition.
- `aggregate(aggregation_function, aggregation_key)`: Applies an aggregation function to values from a specified column.
- `join(other_table, key)`: Combines matching rows from two tables using a common key.
- `__str__()`: Returns a string representation of the table.

### Table Join Operation

The `join()` method performs an inner join between two tables using a shared key.

In this project, the Cities and Countries tables are joined using the `country` key.

The resulting table contains both city information and corresponding country information.

Only records with matching values in both tables are included.

## 4. How to Test and Run

### Requirements

- Python 3
- No additional third-party libraries required

### Running the Program

1. Download or clone the repository.
2. Make sure `OOP_cty.py`, `Cities.csv`, and `Countries.csv` are in the same directory.
3. Open a terminal in the project directory.
4. Run:

```bash
python OOP_cty.py
```

The test code at the bottom of `OOP_cty.py` runs automatically when the script executes.

### Expected Operations

The program performs the following operations:

1. Lists all cities in Italy.
2. Calculates the average temperature of cities in Italy.
3. Lists all non-EU countries.
4. Counts the number of countries with coastlines.
5. Joins Cities and Countries tables using `country`.
6. Lists cities with temperatures below 5°C in non-EU countries.
7. Finds the minimum and maximum temperatures in EU countries without coastlines.

### Expected Results

Using the provided datasets:

- Average temperature in Italy: `13.474666666666668`
- Number of countries with coastlines: `29`
- Minimum temperature in EU countries without coastlines: `4.54`
- Maximum temperature in EU countries without coastlines: `10.34`

## 5. Conclusion

This lab demonstrates how Object-Oriented Programming improves code organization and reusability.

The `DataLoader` class handles file loading, the `DB` class manages multiple tables, and the `Table` class provides filtering, aggregation, and joining operations.

These concepts provide a foundation for more advanced data processing and database management.