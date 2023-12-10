import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here

    df = pd.DataFrame(df)
    # Pivot the DataFrame to create a matrix
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    # Set diagonal values to 0
    for index in car_matrix.index:
        car_matrix.at[index, index] = 0
    
    return car_matrix


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here

    df = pd.DataFrame(df)
    # Create a new column 'car_type' based on the conditions provided
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                                labels=['low', 'medium', 'high'], right=False)
    
    # Count occurrences of each car_type category
    type_counts = df['car_type'].value_counts().to_dict()
    
    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))
    
    return sorted_type_counts


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here

    # Check if 'bus' column exists in the DataFrame
    if 'bus' not in df.columns:
        raise ValueError("The DataFrame must contain a 'bus' column.")

    # Calculate the mean of the 'bus' column
    bus_mean = df['bus'].mean()

    # Filter indices where the 'bus' values are greater than twice the mean
    filtered_indices = df[df['bus'] > 2 * bus_mean].index

    # Return the sorted indices as a list
    return sorted(filtered_indices)


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    # Check if 'truck' and 'route' columns exist in the DataFrame
    if 'truck' not in df.columns or 'route' not in df.columns:
        raise ValueError("The DataFrame must contain 'truck' and 'route' columns.")

    # Group by 'route' and calculate the mean of 'truck' for each route
    route_means = df.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' is greater than 7
    filtered_routes = route_means[route_means > 7].index

    # Return the sorted list of values of the 'route' column
    return sorted(filtered_routes)



def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Create a new DataFrame to store the modified values.
    modified_df = pd.DataFrame()

    # Iterate over the rows of the input DataFrame.
    for index, row in matrix.iterrows():

        # Iterate over the columns of the input DataFrame.
        for column in matrix.columns:

            # Get the value of the current cell.
            value = row[column]

            # Multiply the value by 0.75 if it is greater than 20, and by 1.25 if it is 20 or less.
            modified_value = value * 0.75 if value > 20 else value * 1.25

            # Add the modified value to the new DataFrame.
            modified_df.loc[index, column] = modified_value

    # Return the modified DataFrame.
    return modified_df.round(1)


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
