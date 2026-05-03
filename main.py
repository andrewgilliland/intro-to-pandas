import pandas as pd


def main():
    # --- Creating a DataFrame ---
    data = {
        "name": ["Alice", "Bob", "Carol", "Dave"],
        "department": ["Engineering", "Marketing", "Engineering", "Sales"],
        "salary": [95000, 72000, 105000, 68000],
        "years": [3, 5, 7, 2],
    }
    df = pd.DataFrame(data)
    print("=== DataFrame ===")
    print(df)

    # --- Basic properties ---
    print("\n=== Shape, dtypes, describe ===")
    print("Shape:", df.shape)
    print(df.dtypes)
    print(df.describe())

    # --- Selecting columns ---
    print("\n=== Salary column (Series) ===")
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

    # --- loc and iloc ---
    print("\n=== loc: rows where years >= 5, salary column ===")
    print(df.loc[df["years"] >= 5, "salary"])

    print("\n=== iloc: first 2 rows ===")
    print(df.iloc[0:2])

    # --- Adding and transforming columns ---
    df["bonus"] = df["salary"] * 0.10
    df["total_comp"] = df["salary"] + df["bonus"]

    def seniority(years):
        if years < 2:
            return "Junior"
        elif years < 5:
            return "Mid"
        else:
            return "Senior"

    df["level"] = df["years"].apply(seniority)
    df["salary_k"] = df["salary"].apply(lambda x: f"${x // 1000}k")
    df["name_upper"] = df["name"].str.upper()

    print("\n=== After transformations ===")
    print(df[["name", "name_upper", "salary_k", "level", "total_comp"]])

    # --- Groupby and aggregation ---
    print("\n=== Avg salary by department ===")
    print(df.groupby("department")["salary"].mean())

    print("\n=== Multi-aggregation ===")
    summary = df.groupby("department").agg(
        avg_salary=("salary", "mean"),
        max_salary=("salary", "max"),
        headcount=("name", "count"),
    )
    print(summary)

    print("\n=== Sorted by avg salary ===")
    sorted_summary = df.groupby("department")["salary"].mean().reset_index()
    sorted_summary = sorted_summary.sort_values("salary", ascending=False)
    print(sorted_summary)

    # --- Exporting ---
    df.to_csv("output.csv", index=False)
    df.to_json("output.json", orient="records", indent=2)
    print("\nExported to output.csv and output.json")


if __name__ == "__main__":
    main()
