def main(df):
    # --- Export to CSV ---
    df.to_csv("data/output.csv", index=False)
    print("=== Exported to data/output.csv ===")

    # --- Export to JSON ---
    df.to_json("data/output.json", orient="records", indent=2)
    print("=== Exported to data/output.json ===")
