# Random Data Generator
## Project Details
This is a project I designed as a step up from my past random-xcel-generator module. This project will serve to be valuable in my study of ML and ML models and allow me to quickly generate constant random data to test with models. Feel free to try it out and maybe use it in your own projects, anything from generating a 100,000 entry table with missing data requiring you to use data-analysis and understand what data or rows to drop entirely. Use it for an easy ML dataset with or without missing data. 
******
### Code Examples
The following code will be used as the basis for all following functions unless stated otherwise
```python
    headers = [
        ('name', 'str'), 
        ('age', 'int'), (
            'money', 'float')
    ]
    available_names = [
        'Will',
        'Sean',
        'Syl'
    ]
```
The code below displays a simple use of the generate_row_data and format_headers functions. This asserts that all data is added properly to the new row dict which is returned and set as new_row.\
Example Output:\
&nbsp;&nbsp;&nbsp;&nbsp;{'name': 'Will', 'age': 75, 'money': 75673.91}
```python
    add_row = {
        'name' : available_names,
        'age' : [18, 80],
        'money' : [0, 100000]
    }

    formatted_headers = format_headers(headers)
    new_row = generate_row_data(formatted_headers, add_row)
```
The code below instead adds only 2 rows, instead of the full 3, this can be paired with pd function setting a fill_index=0 value when reindexing a row.\
Example Output:\
&nbsp;&nbsp;&nbsp;&nbsp;{'name': 'Sean', 'age': 57}
```python
    add_row = {
        'name' : available_names,
        'age' : [18, 80],
    }

    formatted_headers = format_headers(headers)
    new_row = generate_row_data(formatted_headers, add_row)
```
The code below tests to see what happens when an incorrect data type match occurs between headers value and value given for a row. Output should skip the age entry and add both name and money no age.\
Example Output:\
&nbsp;&nbsp;&nbsp;&nbsp;{'name': 'Sean', 'money': 77481.01}
```python
    add_row = {
        'name' : available_names,
        'age' : available_names,
        'money' : [0, 100000]
    }
    formatted_headers = format_headers(headers)
    new_row = generate_row_data(formatted_headers, add_row)
```
The code below is similair to the first example where all data is passed to correct keys and the correct data type, however we are testing to see how the string formatting works for format_headers. In order to pass a string to format headers it must follow the following rules, 'title', 'data_type'. The accepted data types are str, int, float; this supports a choice of strings, an int in range k-n inclusive (which also works for bool if you set 0, 1 as the min and max), and a float range k-n inclusive.\
Example Output:\
&nbsp;&nbsp;&nbsp;&nbsp;[('name', 'str'), ('age', 'int'), ('money', 'float')]\
&nbsp;&nbsp;&nbsp;&nbsp;{'name': 'Sean', 'age': 71, 'money': 46383.99}
```python
   formatted_headers = format_headers('name, str, age, int, money, float')
    print(formatted_headers)

    add_row = {
        'name' : available_names,
        'age' : [18, 100],
        'money' : [0, 100000]
    }
```
The code below tests what occurs when a partially correct input is set for format_headers string. In this example name and age are valid, but all other keys won't work since their values arent str, int, or float. The desired outcome for this is a new_row with name and age set properly.\
Example Output:\
&nbsp;&nbsp;&nbsp;&nbsp;[('name', 'str'), ('age', 'int'), ('money', 'f'), ('int', 'lol')]\
&nbsp;&nbsp;&nbsp;&nbsp;{'name': 'Sean', 'age': 74}
```python
    formatted_headers = format_headers('name, str, age, int, money, f, int, lol')
    print(formatted_headers)

    add_row = {
        'name' : available_names,
        'age' : [18, 100],
        'money' : [0, 100000]
    }
    new_row = generate_row_data(formatted_headers, add_row)
    print(new_row)
```