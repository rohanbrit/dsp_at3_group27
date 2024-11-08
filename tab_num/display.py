# tab_numeric/display.py
import streamlit as st
import altair as alt
import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from tab_numeric.logics import NumericColumn

def display_tab_num_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_num_content (function): Function that will instantiate tab_num.logics.NumericColumn class, save it into Streamlit session state, and call its methods to find all numeric columns.
    Then it displays various analyses such as histograms, box plots, and scatter plots.

    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded DataFrame (optional)

    --------------------
    Returns
    --------------------
    -> None
    """
    # Instantiate the NumericColumn class
    num_col_analyzer = NumericColumn(file_path=file_path, df=df)

    # Load and identify numeric columns
    num_col_analyzer.find_num_cols()
    numeric_columns = num_col_analyzer.cols_list

    if not numeric_columns:
        st.warning("No numeric columns found in the dataset.")
        return

    # Display a select box for numeric column selection
    selected_column = st.selectbox(
        "Select a numeric column for analysis:",
        numeric_columns,
        key="numeric_column_select"
    )

    # Set data for the selected column and compute stats
    num_col_analyzer.set_data(selected_column)

    # Display statistics summary
    st.subheader(f"Statistics Summary for {selected_column}")
    summary_df = num_col_analyzer.get_summary()
    st.table(summary_df)

    # Display histogram
    st.subheader("Histogram")
    st.altair_chart(num_col_analyzer.histogram, use_container_width=True)

    # Display box plot
    st.subheader("Interactive Box Plot")
    box_plot = num_col_analyzer.set_boxplot()
    if box_plot:
        st.altair_chart(box_plot, use_container_width=True)

    # Display scatter plot (with user selection for second column)
    st.subheader("Interactive Scatter Plot")
    other_column = st.selectbox("Select another numeric column for scatter plot:", [col for col in numeric_columns if col != selected_column])
    scatter_plot = num_col_analyzer.set_scatterplot(other_column)
    if scatter_plot:
        st.altair_chart(scatter_plot, use_container_width=True)
