def main(df):
    # --- Average salary by department ---
    print("=== Avg salary by department ===")
    print(df.groupby("department")["salary"].mean())

    # --- Multiple aggregations ---
    print("\n=== Multi-aggregation ===")
    summary = df.groupby("department").agg(
        avg_salary=("salary", "mean"),
        max_salary=("salary", "max"),
        headcount=("name", "count"),
    )
    print(summary)

    # --- Sort results ---
    print("\n=== Sorted by avg salary ===")
    sorted_summary = df.groupby("department")["salary"].mean().reset_index()
    sorted_summary = sorted_summary.sort_values("salary", ascending=False)
    print(sorted_summary)
