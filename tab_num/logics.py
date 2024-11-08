# tab_numeric/logics.py
import pandas as pd
import altair as alt

#class to look after numeric data types
class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column of numeric data type

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (optional)
    -> df (pd.DataFrame): Pandas dataframe (optional)
    -> cols_list (list): List of columns names of dataset that are numeric type (default set to empty list)
    -> serie (pd.Series): Pandas series where the content of a column has been loaded (default set to None)
    -> n_unique (int): Number of unique values of a series (default set to None)
    -> n_missing (int): Number of missing values of a series (default set to None)
    -> col_mean (int): Average value of a series (default set to None)
    -> col_std (int): Standard deviation value of a series (default set to None)
    -> col_min (int): Minimum value of a series (default set to None)
    -> col_max (int): Maximum value of a series (default set to None)
    -> col_median (int): Median value of a series (default set to None)
    -> n_zeros (int): Number of times a series has values equal to 0 (default set to None)
    -> n_negatives (int): Number of times a series has negative values (default set to None)
    -> histogram (alt.Chart): Altair histogram displaying the count for each bin value of a series (default set to empty)
    -> frequent (pd.DataFrame): Dataframe containing the most frequent values of a series (default set to empty)
    """
    def __init__(self, file_path=None, df=None):
        """
        --------------------
        Description
        --------------------
        -> __init__ (method): Class constructor that initializes the attributes of the NumericColumn class.

        --------------------
        Parameters
        --------------------
        -> file_path (str): Path to the CSV file to load (optional)
        -> df (pd.DataFrame): Preloaded Pandas DataFrame (optional)

        --------------------
        Returns
        --------------------
        -> None
        """
        self.file_path = file_path
        self.df = df if df is not None else pd.read_csv(file_path) if file_path else pd.DataFrame()
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.col_mean = None
        self.col_std = None
        self.col_min = None
        self.col_max = None
        self.col_median = None
        self.n_zeros = None
        self.n_negatives = None
        self.histogram = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])

    #function to find numeric columns
    def find_num_cols(self):
        """
        --------------------
        Description
        --------------------
        -> find_num_cols (method): Class method that finds and sets all numeric columns in the DataFrame to self.cols_list.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.df.empty:
            self.cols_list = self.df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    def set_data(self, col_name):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that sets the self.serie attribute with the specified column and computes all requested statistics.

        --------------------
        Parameters
        --------------------
        -> col_name (str): Name of the numeric column to be analyzed

        --------------------
        Returns
        --------------------
        -> None
        """
        if col_name in self.df.columns:
            self.serie = self.df[col_name]
            self.convert_serie_to_num()
            self.set_unique()
            self.set_missing()
            self.set_zeros()
            self.set_negatives()
            self.set_mean()
            self.set_std()
            self.set_min()
            self.set_max()
            self.set_median()
            self.set_histogram()
            self.set_frequent()

    #typecasting function
    def convert_serie_to_num(self):
        """
        --------------------
        Description
        --------------------
        -> convert_serie_to_num (method): Class method that converts self.serie to a numeric type.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if self.serie is not None:
            self.serie = pd.to_numeric(self.serie, errors='coerce')

    #function to check empty:
    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or None.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): True if self.serie is empty or None, False otherwise
        """
        return self.serie is None or self.serie.empty

    #unique value function
    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that calculates the number of unique values in self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.n_unique = self.serie.nunique()

    #missing value function
    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that calculates the number of missing values in self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.n_missing = self.serie.isna().sum()

    #zero value function
    def set_zeros(self):
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that counts the number of zero values in self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.n_zeros = (self.serie == 0).sum()

    #negatives function
    def set_negatives(self):
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that counts the number of negative values in self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.n_negatives = (self.serie < 0).sum()

    #mean function
    def set_mean(self):
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that calculates the mean of self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.col_mean = round(self.serie.mean(), 2)

    #std deviation function
    def set_std(self):
        """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that calculates the standard deviation of self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.col_std = round(self.serie.std(), 2)

    #min function
    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that finds the minimum value of self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.col_min = self.serie.min()

    #max_function
    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that finds the maximum value of self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.col_max = self.serie.max()

    #mediam function
    def set_median(self):
        """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that calculates the median value of self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.col_median = self.serie.median()

    #histogram function
    def set_histogram(self):
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that generates an Altair histogram of self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            self.histogram = alt.Chart(self.df).mark_bar().encode(
                alt.X(self.serie.name, bin=True),
                y='count()'
            ).properties(
                title=f'Histogram of {self.serie.name}'
            )

    #boxplot function
    def set_boxplot(self):
        """
        --------------------
        Description
        --------------------
        -> set_boxplot (method): Class method that generates an Altair box plot for the current self.serie.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (alt.Chart): Box plot for the selected numeric column.
        """
        if not self.is_serie_none():
            boxplot = alt.Chart(self.df).mark_boxplot().encode(
                y=alt.Y(self.serie.name, title=self.serie.name)
            ).properties(
                title=f'Box Plot for {self.serie.name}',
                width=600,
                height=400
            )
            return boxplot
    
    #scatterplot function
    def set_scatterplot(self, other_column):
        """
        --------------------
        Description
        --------------------
        -> set_scatterplot (method): Class method that generates an Altair scatter plot between self.serie and another numeric column.

        --------------------
        Parameters
        --------------------
        -> other_column (str): Name of the other numeric column to compare against.

        --------------------
        Returns
        --------------------
        -> (alt.Chart): Scatter plot between the selected columns.
        """
        if not self.is_serie_none() and other_column in self.df.columns:
            scatterplot = alt.Chart(self.df).mark_circle(size=60).encode(
                x=alt.X(self.serie.name, title=self.serie.name),
                y=alt.Y(other_column, title=other_column),
                tooltip=[self.serie.name, other_column]
            ).properties(
                title=f'Scatter Plot: {self.serie.name} vs {other_column}',
                width=700,
                height=500
            ).interactive()
            return scatterplot

    #frequency function
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the DataFrame containing the most frequent values of a series.

        --------------------
        Parameters
        --------------------
        -> end (int): The maximum number of top values to be displayed.

        --------------------
        Returns
        --------------------
        -> None
        """
        if not self.is_serie_none():
            value_counts = self.serie.value_counts().head(end).reset_index()
            value_counts.columns = ['value', 'occurrence']
            value_counts['percentage'] = (value_counts['occurrence'] / len(self.serie) * 100).round(2)
            self.frequent = value_counts
    
    #summary function:
    def get_summary(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary (method): Class method that formats and returns all computed statistics as a Pandas DataFrame.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted DataFrame containing metrics and their respective values.
        """
        if not self.is_serie_none():
            summary = {
                'Unique Values': self.n_unique,
                'Missing Values': self.n_missing,
                'Zero Values': self.n_zeros,
                'Negative Values': self.n_negatives,
                'Average': self.col_mean,
                'Standard Deviation': self.col_std,
                'Minimum': self.col_min,
                'Maximum': self.col_max,
                'Median': self.col_median
            }
            return pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
        return pd.DataFrame(columns=['Metric', 'Value'])
