# intro-to-pandas

A practical introduction to [pandas](https://pandas.pydata.org/), Python's library for working with tabular data.

## What It Covers

- Creating DataFrames from Python dicts
- Inspecting data with `shape`, `dtypes`, `describe`, and `info`
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
uv sync
```

## Run

```bash
uv run main.py
```

Outputs a summary of each operation to the terminal and exports `output.csv` and `output.json`.
