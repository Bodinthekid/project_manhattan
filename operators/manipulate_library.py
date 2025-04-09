
import pandas as pd



class ManipulateDF:

    def remove_nr_from_column(self, df : pd.DataFrame, column_name : str):

        """
            remove integers nr from a string

        Parameters:
            dataframe = df, column_name = string

        Returns:
            df
        """

        df[column_name] = df[column_name].str.replace(r'\d+', '', regex=True)
        return df
    

    def change_column_name(self, df : pd.DataFrame, new_columns : dict):

        """
            change column names from df using dict

        Parameters:
            dataframe = df, new_columns = dict

        Returns:
            df
        """

        df = df.rename(columns=new_columns)

        return df