import streamlit as st
import pandas as pd
from tab_df.logics import Dataset

def display_tab_df_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_df_content (function): Function that will instantiate tab_df.logics.Dataset class, save it into Streamlit session state and call its tab_df.logics.Dataset.set_data() method in order to compute all information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    1. the results of tab_df.logics.Dataset.get_summary() as a Streamlit Table
    2. the results of tab_df.logics.Dataset.table using Streamlit.write()
    Finally it will display a second Streamlit Expander container with a slider to select the number of rows to be displayed and a radio button to select the method (head, tail, sample).
    According to the values selected on the slider and radio button, display the subset of the dataframe accordingly using Streamlit.dataframe
    
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """
    if file_path is not None:
        dataset = Dataset(file_path)
    elif df is not None:
        dataset = Dataset(df=df)
    else:
        st.warning("Please provide either a file path or a dataframe to analyze.")
        return

    st.session_state["dataset"] = dataset
    dataset.set_data()

    with st.expander("Dataset Overview", expanded=True):
        summary = dataset.get_summary()
        if summary is not None:
            st.table(summary)
        if dataset.table is not None:
            st.write(dataset.table)

    with st.expander("View Data", expanded=True):
        n_rows = st.slider("Select number of rows to display", min_value=1, max_value=100, value=5)
        method = st.radio("Select method to view data", options=["Head", "Tail", "Sample"])

        if method == "Head":
            st.dataframe(dataset.get_head(n=n_rows))
        elif method == "Tail":
            st.dataframe(dataset.get_tail(n=n_rows))
        elif method == "Sample":
            st.dataframe(dataset.get_sample(n=n_rows))