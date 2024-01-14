import pandas as pd
import numpy as np
from io import StringIO
from helpers import clean
from helpers import capitalize
from helpers import transform_gender
from helpers import split_string
from helpers import remove_prefix


def my_m_and_a(content_database_1, content_database_2, content_database_3):
    df_1 = pd.read_csv(content_database_1, sep=",")
    df_2 = pd.read_csv(content_database_2, sep=";", header=None)
    df_3 = pd.read_csv(content_database_3, sep="\t|,", engine="python")

    df1 = transform_db_1(df_1)
    df2 = transform_db_2(df_2)
    df3 = transform_db_3(df_3)

    df = pd.concat([df1, df2, df3])

    df = df[['Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country', 'Created_at', 'Referral']]

    return df


def transform_db_1(df):
    df = df.rename(columns={"username": "Referral"})
    df["Created_at"] = np.nan
    df["Age"] = df["Age"].astype(str)

    df["Gender"] = transform_gender(df["Gender"])

    df["LastName"] = df["LastName"].astype(str).map(clean).map(capitalize)
    df["FirstName"] = df["FirstName"].astype(str).map(clean).map(capitalize)
    df["Email"] = df["Email"].astype(str).map(clean).str.lower()
    df["City"] = df["City"].astype(str).map(capitalize).map(split_string)
    df["Country"] = "USA"

    return df


def transform_db_2(df):
    df.columns = ["Age", "City", "Gender", "Name", "Email"]

    df["Gender"] = transform_gender(df["Gender"])
    df["Age"] = df["Age"].astype(str).str.extract('(\d+)').astype(str)

    df[["FirstName", "LastName"]] = df["Name"].astype(str).str.split(" ", n=1, expand=True)

    df["FirstName"] = df["FirstName"].astype(str).map(clean).map(capitalize)
    df["LastName"] = df["LastName"].astype(str).map(clean).map(capitalize)
    df["Email"] = df["Email"].astype(str).map(clean).str.lower()
    df["City"] = df["City"].astype(str).map(capitalize).map(split_string)
    df["Country"] = "USA"

    df["Referral"] = np.nan
    df["Created_at"] = np.nan

    return df


def transform_db_3(df):
    df = df.applymap(remove_prefix)

    df["Gender"] = transform_gender(df["Gender"])
    df["Age"] = df["Age"].str.extract('(\d+)').astype(str)

    split_names = df["Name"].astype(str).str.split(" ", n=1, expand=True)
    df["FirstName"] = split_names[0]
    if 1 in split_names.columns:
        df["LastName"] = split_names[1].fillna('')
    else:
        df["LastName"] = ''

    df["FirstName"] = df["FirstName"].astype(str).map(clean).map(capitalize)
    df["LastName"] = df["LastName"].astype(str).map(clean).map(capitalize)
    df["Country"] = "USA"
    df["Email"] = df["Email"].astype(str).map(clean).str.lower()
    df["City"] = df["City"].astype(str).map(capitalize).map(split_string)

    df["Referral"] = np.nan
    df["Created_at"] = np.nan

    return df
