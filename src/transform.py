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
        #below is the top most popular items, chance head argument
        return filtered_data["ItemName"].value_counts().head(20)
    except KeyError:
        return "KeyError: Check if your DataFrame contains 'OrdType' and 'ItemName' columns."
    except Exception as e:
        return f"An error occurred: {e}"
    
def calculate_dine_in_percentage(data, order_type="Dine In"):
    """
    Calculates the percentage of orders that are 'Dine In' compared to total orders.

    Parameters:
        data (pd.DataFrame): The data containing order details.
        order_type (str): The type of order to filter by (default is 'Dine In').

    Returns:
        float: The percentage of 'Dine In' orders.
    """
    try:
        total_orders = len(data)
        if total_orders == 0:
            return "No orders found."

        # Filter data for Dine In orders and count them
        dine_in_orders_count = len(data[data["OrdType"] == order_type])
        
        # Calculate percentage
        dine_in_percentage = (dine_in_orders_count / total_orders) * 100
        return f"{dine_in_percentage:.2f}% of orders are {order_type}."

    except KeyError:
        return "KeyError: Check if your DataFrame contains 'OrdType' column."
    except Exception as e:
        return f"An error occurred: {e}"
