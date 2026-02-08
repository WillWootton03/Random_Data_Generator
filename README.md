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
The code below displays the method for generate millions of rows in minimal time. Utilizing numpy's random functions I make use of numpy's optimized C code which runs worlds faster than a traditional python for loop. After testing between running multi-processed python and numpy's functionality numpy is up to 10x faster so it works better for data processing. This produces a fully usable dataframe as the return value.\
The code snippet is a small snippet showing our data dictionary, and the for loop iterates through all possible headers, it then checks whatever was pushed into row_data to set all columns. This is just the case for int values, there are similair match cases for float and str variables.\
Example output:
&nbsp;&nbsp;&nbsp;&nbsp;pd.df(size)
```python 
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
```
The code below is a simple save to csv, which has a defualt file name. The function prevents data files from overriding by incrementing the number extension on the end of the file. Besides the normal os.path, and df.to_csv this is the main file saving algorithm.\
Example File name:
&nbsp;&nbsp;&nbsp;&nbsp;'data_file_102.csv'
```python
# If it is a default file_name
if file_name == 'data_file_':
    # gets only the data file number for all files in the data dir
    def_files = [int(file[10:-4]) for file in os.listdir(output_dir) if file.startswith('data_file_')]
    # if there are any default file name styled files
    if def_files:
        # gets the largest data file extension number and increments it so no overriding files
        num = str(max(def_files) + 1)
        file_name += num + ext
    else: 
        # create the first default file name file
        file_name = 'data_file_1.csv'
```