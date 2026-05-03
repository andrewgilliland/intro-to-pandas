import pandas as pd


def make_dataframe():
    data = {
        "name": ["Alice", "Bob", "Carol", "Dave"],
        "department": ["Engineering", "Marketing", "Engineering", "Sales"],
        "salary": [95000, 72000, 105000, 68000],
        "years": [3, 5, 7, 2],
    }
    return pd.DataFrame(data)


def main():
    df = make_dataframe()

    print("=== DataFrame ===")
    print(df)

    print("\n=== Salary column (Series) ===")
    print(df["salary"])

    print("\n=== Shape, dtypes, describe ===")
    print("Shape:", df.shape)
    print(df.dtypes)
    print(df.describe())

    return df
