from generator import format_headers, generate_row_data

def test_new_row():
    """
        Generate a random row with all values present

        Expected Outcome:
            a full new_row with values for name, age, and money
    """
    headers = [('name', 'str'), ('age', 'int'), ('money', 'float')]
    available_names = [
        'Will',
        'Sean',
        'Syl'
    ]
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
    headers = [('name', 'str'), ('age', 'int'), ('money', 'float')]
    available_names = [
        'Will',
        'Sean',
        'Syl'
    ]
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
    headers = [('name', 'str'), ('age', 'int'), ('money', 'float')]
    available_names = [
        'Will',
        'Sean',
        'Syl'
    ]
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
