"""
Table module
"""
import pandas as pd
import numpy as np


class Table:
    """
    Table class helps us to take csv files
    as input and perform desired operations
    """
    def __init__(self, filename):
        self.data = pd.read_csv(filename)

    def columns(self):
        """
        Get all the column names from the given
        dataframe `self.data`

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.columns()
        """
        return self.data.columns

    def total_columns(self):
        """
        Get the count of all column in the given
        dataframe `self.data`

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.total_columns()
        """
        return len(self.columns())

    def total_rows(self):
        """
        Get total count of rows from the current
        dataframe `self.data`.

        returns: dataframe

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.total_rows()
        """

    def get_categorical(self):
        """
        Gets the categorical columns from the given
        dataframe `self.data`

        returns: dataframe

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.get_categorical()
        """

    def get_numerical(self):
        """
        Gets the numerical columns from the given
        dataframe `self.data`

        returns: dataframe

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.get_numerical()
        """

    def odd_rows(self):
        """
        Get all odd indexed counted rows from the given
        dataframe `self.data`
        returns: dataframe

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.odd_rows()
        """
        return self.data.iloc[1::2]

    def even_rows(self):
        """
        Get all even indexed counted rows from the given
        dataframe `self.data`

        returns: dataframe
        """
        return self.data.iloc[:-2:2]

    def apply(self):
        """
        No description
        """
