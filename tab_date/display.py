import streamlit as st

from tab_date.logics import DateColumn

def display_tab_date_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_date_content (function): Function that will instantiate tab_date.logics.DateColumn class, save it into Streamlit session state and call its tab_date.logics.DateColumn.find_date_cols() method in order to find all datetime columns.
    Then it will display a Streamlit select box with the list of datetime columns found.
    Once the user select a datetime column from the select box, it will call the tab_date.logics.DateColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_date.logics.DateColumn.get_summary() as a Streamlit Table
    - the graph from tab_date.logics.DateColumn.histogram using Streamlit.altair_chart()
    - the results of tab_date.logics.DateColumn.frequent using Streamlit.write
 
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
        date_col = DateColumn(file_path=file_path)
    elif df is not None:
        date_col = DateColumn(df=df)
    else:
        st.warning("Please provide either a file path or a dataframe to analyze date columns.")
        return
    
    st.session_state["date_colum"] = date_col
    date_col.find_date_cols()
  
#   Check for empty list if not then proceed
    if len(date_col.cols_list) !=0 :
        selected_col = st.selectbox("Which date column do you want to explore", date_col.cols_list, key="date_col_selector")
        date_col.set_data(selected_col)
   
        with st.expander("Date Column", expanded=True):
            summary_df = date_col.get_summary()
            st.table(summary_df)


            st.subheader("BarChart")
            st.altair_chart(date_col.barchart, use_container_width=True)

            st.subheader("Most Frequent Values:")
            st.write(date_col.frequent)
    else:
        st.write('No date Column Found')