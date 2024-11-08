import streamlit as st

from tab_text.logics import TextColumn

def display_tab_text_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_text_content (function): Function that will instantiate tab_text.logics.TextColumn class, save it into Streamlit session state and call its tab_text.logics.TextColumn.find_text_cols() method in order to find all text columns.
    Then it will display a Streamlit select box with the list of text columns found.
    Once the user select a text column from the select box, it will call the tab_text.logics.TextColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_text.logics.TextColumn.get_summary() as a Streamlit Table
    - the graph from tab_text.logics.TextColumn.histogram using Streamlit.altair_chart()
    - the results of tab_text.logics.TextColumn.frequent using Streamlit.write
 
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
    
    # Create an object of the TextColumn class and save it in the session state
    st.session_state["text_column"] = TextColumn(file_path=file_path, df=df)

    # Call the find_text_cols() to filter columns with textual data
    st.session_state.text_column.find_text_cols()

    # Set the selected text column in a variable
    option = st.selectbox("Which text column do you want to explore", st.session_state.text_column.cols_list)
    
    # Set the selected option in the session state
    try:
        st.session_state.text_column.set_data(option)
    except Exception:
        st.error("There was an error encountered while reading the file")
        exit()

    # Create an expander container to display the analysis and visualizations
    with st.expander('Text Column', expanded=True):

        # Create a table to display analysis information
        st.table(data=st.session_state.text_column.get_summary())

        # Create a bar chart showing the number of occurrence for each value
        st.subheader("Bar Chart")
        st.altair_chart(st.session_state.text_column.barchart, use_container_width=True)
        
        # Create a table listing the occurrences and percentage of the top 20 most frequent values
        st.subheader("Most Frequent Values")
        st.dataframe(st.session_state.text_column.frequent)