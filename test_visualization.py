import pandas as pd

from src.visualization import create_visualization


df = pd.DataFrame({
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04",
        "2026-01-05"
    ],
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor",
        "Keyboard"
    ],
    "Sales": [
        50000,
        30000,
        20000,
        25000,
        200000
    ],
    "Quantity": [
        5,
        10,
        8,
        7,
        50
    ]
})


# Test Central Visualization Function
fig = create_visualization(
    df,
    "bar",
    x_column="Product",
    y_column="Sales"
)

fig.show()

# Test Line Chart
line_fig = create_visualization(
    df,
    "line",
    x_column="Date",
    y_column="Sales"
)

line_fig.show()


# Test Scatter Chart
scatter_fig = create_visualization(
    df,
    "scatter",
    x_column="Quantity",
    y_column="Sales"
)

scatter_fig.show()


# Test Box Plot
box_fig = create_visualization(
    df,
    "box",
    column="Sales"
)

box_fig.show()


# Test Pie Chart
pie_fig = create_visualization(
    df,
    "pie",
    x_column="Product",
    y_column="Sales"
)

pie_fig.show()

# Test Invalid Chart Type
try:
    create_visualization(
        df,
        "histogram",
        x_column="Product",
        y_column="Sales"
    )
except ValueError as error:
    print("\nError Handling Test:")
    print(error)