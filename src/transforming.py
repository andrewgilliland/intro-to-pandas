def main(df):
    df = df.copy()

    # --- New columns from arithmetic ---
    df["bonus"] = df["salary"] * 0.10
    df["total_comp"] = df["salary"] + df["bonus"]

    # --- apply() with a function ---
    def seniority(years):
        if years < 2:
            return "Junior"
        elif years < 5:
            return "Mid"
        else:
            return "Senior"

    df["level"] = df["years"].apply(seniority)

    # --- apply() with a lambda ---
    df["salary_k"] = df["salary"].apply(lambda x: f"${x // 1000}k")

    # --- .str accessor methods ---
    df["name_upper"] = df["name"].str.upper()
    df["dept_short"] = df["department"].str[:3]
    df["is_eng"] = df["department"].str.contains("Engineering")

    print("=== After transformations ===")
    print(
        df[
            [
                "name",
                "name_upper",
                "dept_short",
                "salary_k",
                "level",
                "total_comp",
                "is_eng",
            ]
        ]
    )

    # --- drop and rename ---
    df = df.drop(columns=["bonus"])
    df = df.rename(columns={"salary_k": "salary_display"})

    print("\n=== After drop and rename ===")
    print(df[["name", "salary_display", "level"]])

    return df
