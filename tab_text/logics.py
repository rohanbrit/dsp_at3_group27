import pandas as pd
import altair as alt

class TextColumn:
    """
    --------------------
    Description
    --------------------
    -> TextColumn (class): Class that manages a column from a dataframe of text data type

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (optional)
    -> df (pd.Dataframe): Pandas dataframe (optional)
    -> cols_list (list): List of columns names of dataset that are text type (default set to empty list)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (default set to None)
    -> n_unique (int): Number of unique value of a serie (default set to None)
    -> n_missing (int): Number of missing values of a serie (default set to None)
    -> n_empty (int): Number of times a serie has empty value (default set to None)
    -> n_mode (int): Mode value of a serie (default set to None)
    -> n_space (int): Number of times a serie has only space characters (default set to None)
    -> n_lower (int): Number of times a serie has only lowercase characters (default set to None)
    -> n_upper (int): Number of times a serie has only uppercase characters (default set to None)
    -> n_alpha (int): Number of times a serie has only alphabetical characters (default set to None)
    -> n_digit (int): Number of times a serie has only digit characters (default set to None)
    -> barchart (alt.Chart): Altair barchart displaying the count for each value of a serie (default set to empty)
    -> frequent (pd.DataFrame): Datframe containing the most frequest value of a serie (default set to empty)

    """
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = df
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.n_empty  = None
        self.n_mode = None
        self.n_space = None
        self.n_lower = None
        self.n_upper = None
        self.n_alpha = None
        self.n_digit = None
        self.barchart = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])
    
    def find_text_cols(self):
        """
        --------------------
        Description
        --------------------
        -> find_text_cols (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.
        Then it will find all columns of text data type and store the results in the relevant attribute (self.cols_list).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """

        # If dataframe is not passed, read it from the file path
        if self.df is None:
    
            self.df = pd.read_csv(self.file_path)
        
        # Filter all the text columns from the dataframe
        self.cols_list = self.df.select_dtypes(include="object").columns.tolist()
        

    def set_data(self, col_name):
        """
        --------------------
        Description
        --------------------
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that sets the self.serie attribute with the relevant column from the dataframe and then computes all requested information from self.serie to be displayed in the Text section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> col_name (str): Name of the text column to be analysed

        --------------------
        Returns
        --------------------
        -> None
        """

        # Save the column values to a class variable 'serie'
        self.serie = self.df[col_name]

        # If column has values, convert it to string type and compute and set all values to be displayed into class variables
        if not self.is_serie_none():
            self.convert_serie_to_text()
        
            self.set_unique()
            self.set_missing()
            self.set_empty()
            self.set_whitespace()
            self.set_lowercase()
            self.set_uppercase()
            self.set_alphabet()
            self.set_digit()
            self.set_mode()

            # Set the barchart class variable as the altair chart object
            self.set_barchart()

            # Set the values, occurrence and percentages in the frequent class variable
            self.set_frequent()
        

    def convert_serie_to_text(self):
        """
        --------------------
        Description
        --------------------
        -> convert_serie_to_text (method): Class method that convert a Pandas Series to text data type and store the results in the relevant attribute (self.serie).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        
        self.serie = self.serie.astype(str)

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if the serie is empty or not

        """

        return self.serie is None
        

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie and store the results in the relevant attribute(self.n_unique).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """

        self.n_unique = self.serie.nunique()
        

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie and store the results in the relevant attribute(self.n_missing).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        
        self.n_missing = self.serie.isna().sum()

    def set_empty(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty (method): Class method that computes the number of times a serie has empty value and store the results in the relevant attribute(self.n_empty).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_empty = self.serie.eq("").sum()
        

    def set_mode(self):
        """
        --------------------
        Description
        --------------------
        -> set_mode (method): Class method that computes the mode value of a serie and store the results in the relevant attribute(self.n_mode).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_mode = self.serie.mode()[0]

    def set_whitespace(self):
        """
        --------------------
        Description
        --------------------
        -> set_whitespace (method): Class method that computes the number of times a serie has only space characters and store the results in the relevant attribute(self.n_space).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_space = self.serie.str.isspace().sum()

    def set_lowercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_lowercase (method): Class method that computes the number of times a serie has only lowercase characters and store the results in the relevant attribute(self.n_lower).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_lower = self.serie.str.islower().sum()
        

    def set_uppercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_uppercase (method): Class method that computes the number of times a serie has only uppercase characters and store the results in the relevant attribute(self.n_upper).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_upper = self.serie.str.isupper().sum()
        
    
    def set_alphabet(self):
        """
        --------------------
        Description
        --------------------
        -> set_alphabet (method): Class method that computes the number of times a serie has only alphabetical characters and store the results in the relevant attribute(self.n_alpha).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_alpha = self.serie.str.isalpha().sum()
        

    def set_digit(self):
        """
        --------------------
        Description
        --------------------
        -> set_digit (method): Class method that computes the number of times a serie has only digit characters and store the results in the relevant attribute(self.n_digit).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_digit = self.serie.str.isdigit().sum()

    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie and store the results in the relevant attribute(self.barchart).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        # Get the number of times each unique value occurs in the column
        df_value_counts = self.serie.value_counts().reset_index()

        self.barchart = (
            alt.Chart(df_value_counts)
            .mark_bar()
            .encode(x=alt.X(df_value_counts.columns[0], sort='-y'), y=df_value_counts.columns[1])
        )
        
      
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie and store the results in the relevant attribute(self.frequent).

        --------------------
        Parameters
        --------------------
        -> end (int):
            Parameter indicating the maximum number of values to be displayed

        --------------------
        Returns
        --------------------
        -> None

        """

        self.frequent['value'] = self.serie.value_counts(normalize=False, sort=True, ascending=False).index
        self.frequent['occurrence'] = self.serie.value_counts(normalize=False, sort=True, ascending=False).values
        self.frequent['percentage'] = self.serie.value_counts(normalize=True, sort=True, ascending=False).values

        self.frequent = self.frequent.head(end)
        

    def get_summary(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """

        # Create a summary dataframe with the values to be displayed
        description = [
            "Number of Unique Values",
            "Number of Rows with Missing Values",
            "Number of Empty Rows",
            "Number of Rows with Only Whitespace",
            "Number of Rows with Only Lowercases",
            "Number of Rows with Only Uppercases",
            "Number of Rows with Only Alphabet",
            "Number of Rows with Only Digits",
            "Mode Value"
        ]

        value = [
            self.n_unique,
            self.n_missing,
            self.n_empty,
            self.n_space,
            self.n_lower,
            self.n_upper,
            self.n_alpha,
            self.n_digit,
            self.n_mode
        ]
        
        summary_df = pd.DataFrame({"Description": description, "Value": value}, dtype="string")

        return summary_df