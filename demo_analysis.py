"""
demo_analysis.py

Builds a small fake sales dataset, computes the average sale amount,
and saves a bar chart of sales by product as a PNG.

Run with:
    python demo_analysis.py
"""

import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_PATH = "sales_by_product.png"


def build_sales_data() -> pd.DataFrame:
    """Return a small DataFrame of 10 fake sales records."""
    data = {
        "order_id": range(1, 11),
        "product": [
            "Widget", "Gadget", "Widget", "Gizmo", "Gadget",
            "Widget", "Gizmo", "Gadget", "Widget", "Gizmo",
        ],
        "amount": [25.50, 40.00, 22.75, 15.20, 38.90,
                   28.00, 17.65, 41.30, 24.10, 19.95],
    }
    return pd.DataFrame(data)


def main():
    df = build_sales_data()
    print(df)

    average = df["amount"].mean()
    print(f"\nAverage sale amount: ${average:.2f}")

    sales_by_product = df.groupby("product")["amount"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(6, 4))
    sales_by_product.plot(kind="bar", ax=ax, color="#4C72B0")
    ax.set_title("Total Sales by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Total Sales ($)")
    ax.axhline(average, color="gray", linestyle="--", linewidth=1)
    plt.xticks(rotation=0)
    plt.tight_layout()

    fig.savefig(OUTPUT_PATH, dpi=150)
    print(f"Saved chart to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
