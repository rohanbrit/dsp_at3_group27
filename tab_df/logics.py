import pandas as pd
class Dataset:
    """
    --------------------
    Description
    --------------------
    -> Dataset (class): Class that manages a dataset loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (mandatory)
    -> df (pd.Dataframe): Pandas dataframe (default set to None)
    -> cols_list (list): List of columns names of dataset (default set to empty list)
    -> n_rows (int): Number of rows of dataset (default set to 0)
    -> n_cols (int): Number of columns of dataset (default set to 0)
    -> n_duplicates (int): Number of duplicated rows of dataset (default set to 0)
    -> n_missing (int): Number of missing values of dataset (default set to 0)
    -> n_num_cols (int): Number of columns that are numeric type (default set to 0)
    -> n_text_cols (int): Number of columns that are text type (default set to 0)
    -> table (pd.DataFrame): Pandas DataFrame containing the list of columns, their data types and memory usage from dataframe (default set to None)
    """
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = df
        if self.file_path is not None:
            self.set_df()
        self.cols_list = []
        self.n_rows = 0
        self.n_cols = 0
        self.n_duplicates = 0
        self.n_missing = 0
        self.n_num_cols = 0
        self.n_text_cols = 0
        self.table = None

    def set_data(self):
        if not self.is_df_none():
            self.set_columns()
            self.set_dimensions()
            self.set_duplicates()
            self.set_missing()
            self.set_numeric()
            self.set_text()
            self.set_table()

    def set_df(self):
        if self.df is None and self.file_path is not None:
            try:
                self.df = pd.read_csv(self.file_path, on_bad_lines='skip')
            except pd.errors.ParserError:
                st.error("There was an error reading the CSV file. Please check the file format.")
                self.df = None

    def is_df_none(self):
        return self.df is None or self.df.empty

    def set_columns(self):
        if not self.is_df_none():
            self.cols_list = list(self.df.columns)

    def set_dimensions(self):
        if not self.is_df_none():
            self.n_rows, self.n_cols = self.df.shape

    def set_duplicates(self):
        if not self.is_df_none():
            self.n_duplicates = self.df.duplicated().sum()

    def set_missing(self):
        if not self.is_df_none():
            self.n_missing = self.df.isna().sum().sum()

    def set_numeric(self):
        if not self.is_df_none():
            self.n_num_cols = len(self.df.select_dtypes(include=['number']).columns)

    def set_text(self):
        if not self.is_df_none():
            self.n_text_cols = len(self.df.select_dtypes(include=['object']).columns)

    def get_head(self, n=5):
        if not self.is_df_none():
            return self.df.head(n)

    def get_tail(self, n=5):
        if not self.is_df_none():
            return self.df.tail(n)

    def get_sample(self, n=5):
        if not self.is_df_none():
            return self.df.sample(n)

    def set_table(self):
        if not self.is_df_none():
            memory_usage = self.df.memory_usage(deep=True).values
            if len(memory_usage) == len(self.df.columns) + 1:
                memory_usage = memory_usage[1:]
            if len(memory_usage) == len(self.df.columns):
                self.table = pd.DataFrame({
                    'Column': self.df.columns,
                    'Data Type': self.df.dtypes.astype(str),
                    'Memory Usage': memory_usage
                })
            else:
                st.warning("Memory usage calculation failed due to inconsistent lengths. Please check your dataframe.")

    def get_summary(self):
        if not self.is_df_none():
            return pd.DataFrame({
                'Description': [
                    'Number of Rows',
                    'Number of Columns',
                    'Number of Duplicates',
                    'Number of Missing Values',
                    'Number of Numeric Columns',
                    'Number of Text Columns'
                ],
                'Value': [
                    self.n_rows,
                    self.n_cols,
                    self.n_duplicates,
                    self.n_missing,
                    self.n_num_cols,
                    self.n_text_cols
                ]
            })
        return None
