# intro-to-pandas

A practical introduction to [pandas](https://pandas.pydata.org/), Python's library for working with tabular data.

Companion code for the article [Getting Started with Pandas for Data Science](https://github.com/andrewgilliland/intro-to-pandas).

## Project Structure

```
main.py           # entry point — calls each module in order
data/
  employees.csv   # sample data with intentional missing values
  employees.json  # same data in JSON format
  output.csv      # written by exporting.py
  output.json     # written by exporting.py
src/
  dataframes.py   # creating DataFrames and Series
  read_data.py    # loading data from CSV and JSON
  selecting.py    # filtering rows, .loc and .iloc
  transforming.py # adding columns, .apply(), .str methods
  grouping.py     # groupby() and aggregation
  exporting.py    # to_csv() and to_json()
```

## What It Covers

- Creating DataFrames from Python dicts
- Inspecting data with `shape`, `dtypes`, `describe`, and `head`
- Loading data from CSV and JSON with `read_csv` and `read_json`
- Handling missing values with `isnull`, `dropna`, and `fillna`
- Selecting columns as a Series or DataFrame
- Filtering rows with boolean conditions
- Label-based and position-based selection with `.loc` and `.iloc`
- Adding and transforming columns with `.apply()` and `.str` accessor methods
- Grouping and aggregating data with `groupby()`
- Exporting results to CSV and JSON

## Requirements

- Python >= 3.14
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
git clone https://github.com/andrewgilliland/intro-to-pandas
cd intro-to-pandas
uv sync
```

## Run

```bash
uv run main.py
```

Outputs a summary of each operation to the terminal and writes `data/output.csv` and `data/output.json`.
