
import pandas as pd



class ManipulateDF:

    def remove_nr_from_column(self, df : pd.DataFrame, column_name : str):

        """
        remove integers nr from a string

        Parameters:
            dataframe = df, column_name = string

        Returns:
            WebDriver: An instance of WebDriver to control the browser.
        """

        df[column_name] = df[column_name].str.replace(r'\d+', '', regex=True)
        return df