Collaborative Development of Data Explorer Web App

Authors

Group 27:

- Aditya Kulkarni (25410263)
- Archit Pradip Murgudkar (14190286)
- Rohan Rocky Britto (24610990)
- Vishal Kandikattu (25413586)

Description

The CSV Explorer web application allows users to conduct exploratory data analysis (EDA) on uploaded CSV files. Developed using Streamlit, this application provides various interactive tools for analyzing different types of data, including numeric, text, and date columns. Users can quickly understand the dataset structure, identify data quality issues, and visualize distributions and statistics to derive insights effectively.

Some of the challenges faced during development included designing an intuitive user interface, managing coordination and version control across multiple team members, and handling complex data types efficiently. The project also involved overcoming obstacles related to integrating various types of data visualizations and ensuring performance with larger datasets.

Future features to implement include additional analysis tools, integration with databases for more dynamic data access, machine learning capabilities for automatic insights, and improved performance handling for very large datasets.

How to Setup

Ensure Python 3.9+ is installed on your system.

Clone the project repository from GitHub: git clone https://github.com/rohanbrit/dsp_at3_group27

Navigate to the project directory: cd dsp_at3_group27

Install the required dependencies: pip install -r requirements.txt


How to Run the Program

To start the web application, navigate to the app's directory and run the command:

streamlit run .\app\streamlit_app.py

Once the application is running, access it by opening the URL http://localhost:8501 in your web browser.
From there, upload a CSV file, and use the various tabs to explore and analyze the dataset.


Project Structure

app/: Contains the main Streamlit application.

streamlit_app.py: Entry point for the application.

tab_df/: Handles functionality for DataFrame analysis.

display.py: Contains the code for rendering the DataFrame tab in the UI.

logics.py: Contains logic for processing and summarizing data, including dataset statistics and handling.

tab_num/: Handles numeric column analysis.

display.py: Handles UI display for numeric analysis.

logics.py: Contains numeric data processing logic.

tab_text/: Handles text column analysis.

display.py: Handles UI display for text analysis.

logics.py: Contains text processing logic, including frequency analysis.

tab_date/: Handles date column analysis.

display.py: Handles UI display for date analysis.

logics.py: Contains logic for managing and visualizing date column data.

requirements.txt: Lists all the required Python packages and their versions for running the application.

README.md: Documentation for the project, setup, and running instructions.


Citations

Kabir, M. (n.d.). Collaborative Development of Data Explorer Web App. Retrieved October 25, 2024, from UTS Canvas

Streamlit documentation: https://docs.streamlit.io/

Altair documentation: https://altair-viz.github.io/

