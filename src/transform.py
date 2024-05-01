import pandas as pd


def filter_and_find_popular_item(data, order_type="Dine In"):
    # Filter data for Dine In orders
    filtered_data = data[data["OrdType"] == order_type]
    popular_item = filtered_data["SizeName"].mode()[
        0
    ]  # mode() returns most frequent value
    return popular_item


def find_top_three_items(data, order_type="Dine In"):
    try:
        filtered_data = data[data["OrdType"] == order_type]
        if filtered_data.empty:
            return "No orders found for type '{}'.".format(order_type)
        return filtered_data["ItemName"].value_counts().head(3)
    except KeyError:
        return "KeyError: Check if your DataFrame contains 'OrdType' and 'ItemName' columns."
    except Exception as e:
        return f"An error occurred: {e}"
