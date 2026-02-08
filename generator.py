from random import uniform, randint, choice
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
import os
import numpy as np


def format_headers(headers: list[tuple[str, str]] | str):
    """Input a list of strings for header columns,

    Args:
        headers (list[(str, str)]): Already formatted mostly, first string in list of tuples
                                    represents header title, second reprrsents type in form 
                                    (int, float, list[str])
        headers (str): Will break string based on ,'s and create list then set columns
    """

    if type(headers) == str:
        headers_list = headers.split(',')
        l = 0
        cols = []
        while l < len(headers_list) - 1:
            # set key = to name of the column, and value = to the data type
            key, val = headers_list[l].lower().strip(), headers_list[l+1].lower().strip()
            # Verifies the type of value is acceptable
            if val == 'str' or val == 'int' or val == 'float':
                cols.append((key, val))
            # Skip to next k,v pair in the string
            l += 2
        return cols
    return tuple([(col[0].strip().lower(), col[1]) for col in headers])

def generate_row_data(headers: list[tuple[str, str]], 
                      row_data:dict[str, list[str] | tuple[int, int] | tuple[float, float]]):
    """Generate data for a single row based on the list of data provided. Can be a list of strings to
    choose from, or an int in range from min - max or a float in range min-max. Using tuple of (0, 1)

    Args:
        headers (list[tuple[str, str]]): a list of tuples displaying the column title and data type
        row_data (dict[str, list[str]  |  tuple[int, int]  |  tuple[float, float]]): 
        a dict with the key being the column title, and the value being either a list of potential
        strings, a tuple of min and max ints, or a tuple of min and max floats.

    Returns:
        new_row = {} : Creates and returns a single row when necessary
    """
    new_row = {}
    for col in headers:
        # if this column title is in the row_data's keys get random entry, else skip it
        row = row_data[col[0]] if col[0] in row_data.keys() else None
        if row:
            match col[1]:
                # If the input is an int get a random 
                case 'int':
                    try:
                        new_row[col[0]] = randint(row[0], row[1])
                    except TypeError:
                        print('Incorrect value in this row')
                    except:
                        print('Incorrect value in this row')
                # If the input is a float type get a random float from min-max
                case 'float':
                    try:
                        new_row[col[0]] = round(uniform(row[0], row[1]), 2)
                    except TypeError:
                        print('Incorrect value in this row')
                    except:
                        print('Incorrect value in this row')
                # If the input data is a string, choose a random string from options
                case 'str':
                    try:
                        new_row[col[0]] = choice(row)
                    except TypeError:
                        print('Incorrect value in this row')
                    except:
                        print('Incorrect value in this row')
    return new_row


def generate_data(headers: list[tuple[str, str]], 
                row_data:dict[str, list[str] | tuple[int, int] | tuple[float, float]],
                num_entries: int
                ):
    """
        Using numpy's own random functions work 10x faster than multi-processing
        since numpy is written in C. Using this we can generate up to 100 million
        rows in under 30 seconds.

    Args:
        headers (list[tuple[str, str]]): 
            headers to be used for entries
        row_data (dict[str, list[str]  |  tuple[int, int]  |  tuple[float, float]]): 
            a dict with the key being the column title, and the value being either a list 
            of potential strings, a tuple of min and max ints, or a tuple of min and max floats.
        num_entries (int): 
            the number of entries to add to the pd.dataframe

    Returns:
        dataframe (pd.DataFrame()): 
            returns the dataframe for all items generated in the function
    """
    data = {}
    for h in headers:
        try: 
            row = row_data[h[0]]
            match h[1]:
                # Attempts to add an int column to the df
                case 'int':
                    try:
                        data[h[0]] = np.random.randint(row[0], row[1], num_entries)
                    except TypeError:
                        print('Incorrect value in this row')
                    except:
                        print('Incorrect value in this row')
                # Attemps to add a float column to the df
                case 'float':
                    try:
                        data[h[0]] = np.random.uniform(row[0], row[1], num_entries)
                    except TypeError:
                        print('Incorrect value in this row')
                    except:
                        print('Incorrect value in this row')
                # Attempts to add a string column to the df
                case 'str':
                    try:
                        data[h[0]] = np.random.choice(row, num_entries)
                    except TypeError:
                        print('Incorrect value in this row')
                    except:
                        print('Incorrect value in this row')
        except:
            print('Something went wrong')
    df = pd.DataFrame(data)
    return df
    
