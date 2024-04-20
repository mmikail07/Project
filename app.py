import streamlit as st
import pandas as pd

def main():
    st.title("Sensor Data Display")

    # Read data from CSV file
    sensor_data = pd.read_csv('file.csv')

    # Remove columns with Unnamed headers and N/A values
    sensor_data = sensor_data.loc[:, ~sensor_data.columns.str.contains('^Unnamed')]
    sensor_data = sensor_data.dropna(axis=1, how='all')

    # Display sensor data in a table
    st.table(sensor_data)

if __name__ == "__main__":
    main()
