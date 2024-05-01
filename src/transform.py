import pandas as pd

def filter_and_find_popular_item(data, order_type='Dine In'):
    # Filter data for Dine In orders
    filtered_data = data[data['OrdType'] == order_type]
    popular_item = filtered_data['SizeName'].mode()[0] #mode() returns most frequent value
    return popular_item