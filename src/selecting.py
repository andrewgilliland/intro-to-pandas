def main(df):
    # --- Selecting columns ---
    print("=== Salary column (Series) ===")
    print(df["salary"])

    print("\n=== Name and salary (DataFrame) ===")
    print(df[["name", "salary"]])

    # --- Filtering rows ---
    print("\n=== Salary > 80k ===")
    print(df[df["salary"] > 80000])

    print("\n=== Engineering only ===")
    print(df[df["department"] == "Engineering"])

    print("\n=== Engineering AND salary > 80k ===")
    print(df[(df["salary"] > 80000) & (df["department"] == "Engineering")])

    # --- loc ---
    print("\n=== loc: row 0 ===")
    print(df.loc[0])

    print("\n=== loc: rows 0-2, name and salary ===")
    print(df.loc[0:2, ["name", "salary"]])

    print("\n=== loc: rows where years >= 5, salary column ===")
    print(df.loc[df["years"] >= 5, "salary"])

    # --- iloc ---
    print("\n=== iloc: first row ===")
    print(df.iloc[0])

    print("\n=== iloc: first 2 rows ===")
    print(df.iloc[0:2])

    print("\n=== iloc: all rows, columns 1-2 ===")
    print(df.iloc[:, 1:3])
