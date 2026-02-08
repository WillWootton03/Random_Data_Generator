from generator import format_headers, generate_row_data

headers = [
    ('name', 'str'), 
    ('age', 'int'), 
    ('money', 'float')
]

available_names = [
    'Will',
    'Sean',
    'Syl'
]

def test_new_row():
    """
        Generate a random row with all values present

        Expected Outcome:
            a full new_row with values for name, age, and money
    """
    add_row = {
        'name' : available_names,
        'age' : [18, 80],
        'money' : [0, 100000]
    }
    formatted_headers = format_headers(headers)
    new_row = generate_row_data(formatted_headers, add_row)

    print(new_row)
    assert new_row['name']
    assert new_row['age']
    assert new_row['money']

def test_missing_row():
    """
        Generates a new random row without an entry to a column

        Expected Outcome:
            new_row with a value for name, and age and missing a money value
    """
    add_row = {
        'name' : available_names,
        'age' : [18, 80],
    }

    formatted_headers = format_headers(headers)
    new_row = generate_row_data(formatted_headers, add_row)

    print(new_row)
    assert new_row['name']
    assert new_row['age']

def test_invalid_data_type():
    """
        Generates a random row, but there is a value error in age.

        Expected Outcome:
            new row with only name and money values
    """
    add_row = {
        'name' : available_names,
        'age' : available_names,
        'money' : [0, 100000]
    }
    formatted_headers = format_headers(headers)
    new_row = generate_row_data(formatted_headers, add_row)

    print(new_row)
    assert new_row['name']
    assert new_row['money']

def test_correct_string_headers():
    """
        Tests to see how the format_headers function acts when given a correctly formatted string 
        of headers and types
    """
    formatted_headers = format_headers('name, str, age, int, money, float')
    print(formatted_headers)

    add_row = {
        'name' : available_names,
        'age' : [18, 100],
        'money' : [0, 100000]
    }
    new_row = generate_row_data(formatted_headers, add_row)
    print(new_row)
    assert new_row['name']
    assert new_row['age']
    assert new_row['money']

def test_incorrect_string_headers():
    """
        Tests to see how format_headers handles incorrect formatting for some of the strings header input.
        Creates a new_row to verify correct and incorrect input data
    """
    formatted_headers = format_headers('name, str, age, int, money, f, int, lol')
    print(formatted_headers)

    add_row = {
        'name' : available_names,
        'age' : [18, 100],
        'money' : [0, 100000]
    }
    new_row = generate_row_data(formatted_headers, add_row)
    print(new_row)

    assert new_row['name']
    assert new_row['age']