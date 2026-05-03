import pandas as pd


def main():
    # --- Load from CSV ---
    df = pd.read_csv("data/employees.csv")
    print("=== Loaded from CSV ===")
    print(df)

    # --- Always inspect after loading ---
    print("\n=== head ===")
    print(df.head(3))

    print("\n=== dtypes ===")
    print(df.dtypes)

    print("\n=== shape ===")
    print(df.shape)

    # --- Load with options: select columns, force type, treat missing values ---
    df = pd.read_csv(
        "data/employees.csv",
        usecols=["name", "salary", "department"],  # load only these columns
        dtype={"salary": float},  # force salary to float
        na_values=["N/A", "none", ""],  # treat these as NaN
    )
    print("\n=== Loaded with options ===")
    print(df)

    # --- Inspect missing values ---
    print("\n=== Null counts per column ===")
    print(df.isnull().sum())

    # --- Drop rows with any null ---
    print("\n=== After dropna ===")
    print(df.dropna())

    # --- Fill nulls with a default value ---
    print("\n=== After fillna(0) ===")
    print(df.fillna(0))

    # --- Load from JSON ---
    df_json = pd.read_json("data/employees.json")
    print("\n=== Loaded from JSON ===")
    print(df_json)
    print("\ndtypes:", df_json.dtypes.to_dict())

    return df
