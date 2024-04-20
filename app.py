import streamlit as st
import pandas as pd

def main():
    st.title("Sensor Data Display")

    # Read data from CSV file
    sensor_data = pd.read_csv('file.csv')

    # Display sensor data in a table
    st.table(sensor_data)

if __name__ == "__main__":
    main()
