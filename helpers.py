import pandas as pd


def clean(str):
    return str.replace('\\', '').replace('\"', '')


def capitalize(str):
    return str.capitalize()


def lower(str):
    return str.lower()


def split_string(str):
    if '_' in str:
        parts = str.split('_')
    elif '-' in str:
        parts = str.split('-')
    elif ' ' in str:
        parts = str.split(' ')
    else:
        return str

    res = ''
    for part in parts:
        res = res + part.capitalize() + ' '

    return res.strip(' ')


def transform_gender(column):
    return column.astype(str).str.lower().replace({
        "1": "Male",
        "m": "Male",
        "boolean_1": "Male",
        "string_m": "Male",
        "character_m": "Male",
        "male": "Male",
        "0": "Female",
        "f": "Female",
        "boolean_0": "Female",
        "string_f": "Female",
        "character_f": "Female",
        "female": "Female",
    })


def remove_prefix(x):
    if pd.notnull(x):
        if x.startswith('string_'):
            return x.split('string_')[1]
        if x.startswith('integer_'):
            return x.split('integer_')[1]
        if x.startswith('boolean_'):
            return x.split('boolean_')[1]
        else:
            return x
    else:
        return x
