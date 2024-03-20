import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

sns.set(style='dark')

def create_number_of_rental_each_month(df):
    # Extract year from the 'dteday' column
    df['yr'] = df['dteday'].dt.year

    # Resample the DataFrame based on 'month' and calculate aggregated values
    total_rental_monthly_df = df.groupby(['yr', 'month']).agg({
        "cnt": "count",                      # Count of rental records for the month
    })

    total_rental_monthly_df.reset_index(inplace=True)

    # Drop the 'yr' column
    total_rental_monthly_df.drop(columns=['yr'], inplace=True)

    # Rename the columns
    total_rental_monthly_df.rename(columns={
        "cnt": "total_rental",
    }, inplace=True)

    return total_rental_monthly_df

def create_mean_duration_of_rental_each_month(df):
    # Extract year from the 'dteday' column
    df['yr'] = df['dteday'].dt.year

    # Resample the DataFrame based on 'month' and calculate aggregated values
    mean_duration_monthly_df = df.groupby(['yr', 'month']).agg({
        "hr": "mean",                     
    })
    
    mean_duration_monthly_df.reset_index(inplace=True)

    # Drop the 'yr' column
    mean_duration_monthly_df.drop(columns=['yr'], inplace=True)

    # Rename the columns
    mean_duration_monthly_df.rename(columns={
        "hr": "mean_duration",
    }, inplace=True)

    return mean_duration_monthly_df

def create_rental_duration_each_month(df):
    # Extract year from the 'dteday' column
    df['yr'] = df['dteday'].dt.year

    # Resample the DataFrame based on 'month' and calculate aggregated values
    rental_duration_monthly_df = df.groupby(['yr', 'month']).agg({
        "rental_duration": "sum",                     
    })

    rental_duration_monthly_df.reset_index(inplace=True)

    # Drop the 'yr' column
    rental_duration_monthly_df.drop(columns=['yr'], inplace=True)

    # Rename the columns
    rental_duration_monthly_df.rename(columns={
        "rental_duration": "total_duration_of_rental",
    }, inplace=True)

    return rental_duration_monthly_df

def map_month_to_season(month):
    if month in [12, 1, 2, 3]:
        return 1  # Spring
    elif month in [3, 4, 5, 6]:
        return 2  # Summer
    elif month in [6, 7, 8, 9]:
        return 3  # Fall
    else:
        return 4  # Winter

def create_mean_temperature_each_season(df):    
    # Extract month from the 'dteday' column
    df['month'] = df['dteday'].dt.month

    # Map month to season
    df['season'] = df['month'].apply(map_month_to_season)

    # Resample the DataFrame based on 'season' and calculate aggregated values
    mean_temperature_seasonal_df = df.groupby(['yr', 'season']).agg({
        "temp": "mean",          # Mean temperature for the month
    })

    # Reset index to convert the index to columns
    mean_temperature_seasonal_df.reset_index(inplace=True)

    # Drop the 'yr' column
    mean_temperature_seasonal_df.drop(columns=['yr'], inplace=True)

    # Rename the columns
    mean_temperature_seasonal_df.rename(columns={
        "temp": "mean_temperature",
    }, inplace=True)

    return mean_temperature_seasonal_df

def create_mean_humidity_each_season(df):    
    # Extract month from the 'dteday' column
    df['month'] = df['dteday'].dt.month

    # Map month to season
    df['season'] = df['month'].apply(map_month_to_season)

    # Resample the DataFrame based on 'season' and calculate aggregated values
    mean_humidity_seasonal_df = df.groupby(['yr', 'season']).agg({
        "hum": "mean",          # Mean humidity for the month
    })

    # Reset index to convert the index to columns
    mean_humidity_seasonal_df.reset_index(inplace=True)

    # Drop the 'yr' column
    mean_humidity_seasonal_df.drop(columns=['yr'], inplace=True)

    # Rename the columns
    mean_humidity_seasonal_df.rename(columns={
        "hum": "mean_humidity",
    }, inplace=True)

    return mean_humidity_seasonal_df

def create_mean_windspeed_each_season(df):    
    # Extract month from the 'dteday' column
    df['month'] = df['dteday'].dt.month

    # Map month to season
    df['season'] = df['month'].apply(map_month_to_season)

    # Resample the DataFrame based on 'season' and calculate aggregated values
    mean_windspeed_seasonal_df = df.groupby(['yr', 'season']).agg({
        "windspeed": "mean",          # Mean windspeed for the month
    })

    # Reset index to convert the index to columns
    mean_windspeed_seasonal_df.reset_index(inplace=True)

    # Drop the 'yr' column
    mean_windspeed_seasonal_df.drop(columns=['yr'], inplace=True)

    # Rename the columns
    mean_windspeed_seasonal_df.rename(columns={
        "windspeed": "mean_windspeed",
    }, inplace=True)

    return mean_windspeed_seasonal_df

def create_total_rental_each_season(df):    
    # Extract month from the 'dteday' column
    df['month'] = df['dteday'].dt.month

    # Map month to season
    df['season'] = df['month'].apply(map_month_to_season)

    # Resample the DataFrame based on 'season' and calculate aggregated values
    total_rental_seasonal_df = df.groupby(['yr', 'season']).agg({
        "cnt": "count",
    })

    # Reset index to convert the index to columns
    total_rental_seasonal_df.reset_index(inplace=True)

    # Drop the 'yr' column
    total_rental_seasonal_df.drop(columns=['yr'], inplace=True)

    # Rename the columns
    total_rental_seasonal_df.rename(columns={
        "cnt": "total_rental",
    }, inplace=True)

    return total_rental_seasonal_df

def create_workingday(df):
    by_workingday_df = df.groupby(by="workingday").instant.nunique().reset_index()

    # # Drop the 'yr' column
    # by_workingday_df.drop(columns=['instant'], inplace=True)
    
    return by_workingday_df

def create_workingday_hour(df):
    by_workingday_hour_df = df.groupby(by=["workingday", "hr"]).instant.nunique().reset_index()

    # # Drop the 'yr' column
    # by_workingday_hour_df.drop(columns=['instant'], inplace=True)

    return by_workingday_hour_df

all_df = pd.read_csv("dashboard/main_data.csv")

# Convert 'dteday' column to datetime
all_df['dteday'] = pd.to_datetime(all_df['dteday'])

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("outfushion.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

total_rental_monthly_df = create_number_of_rental_each_month(main_df)
mean_duration_monthly_df = create_mean_duration_of_rental_each_month(main_df)
rental_duration_monthly_df = create_rental_duration_each_month(main_df)
mean_temperature_seasonal_df = create_mean_temperature_each_season(main_df)
mean_humidity_seasonal_df = create_mean_humidity_each_season(main_df)
mean_windspeed_seasonal_df = create_mean_windspeed_each_season(main_df)
total_rental_seasonal_df = create_total_rental_each_season(main_df)
by_workingday_df = create_workingday(main_df)
by_workingday_hour_df = create_workingday_hour(main_df)

st.header('Bike Sharing🚲')

# Plot Total Rental, Mean Duration, and Total Rental Duration in a 1x3 matrix layout
st.subheader('Rental Metrics for each Month')

# Create a row layout with 3 columns
col1, col2, col3 = st.columns(3)

# Plot Total Rental in the first column
with col1:
    st.text('Total Rental')
    st.line_chart(total_rental_monthly_df)

# Plot Mean Duration in the second column
with col2:
    st.text('Mean Duration')
    st.line_chart(mean_duration_monthly_df)

# Plot Total Rental Duration in the third column
with col3:
    st.text('Total Rental Duration')
    st.line_chart(rental_duration_monthly_df)

# Plot Total Rental
st.subheader('Total Rental for each Season')
st.line_chart(total_rental_seasonal_df)

st.subheader('Environmental Metrics')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.subheader('Mean Temperature for each Season')
    st.line_chart(mean_temperature_seasonal_df)

with tab2:
    st.subheader('Mean Humidity for each Season')
    st.line_chart(mean_humidity_seasonal_df)

with tab3:
    st.subheader('Mean Windspeed for each Season')
    st.line_chart(mean_windspeed_seasonal_df)

st.subheader("Number of Order during Working Day")
 
col1, col2 = st.columns(2)

with col1:
    chart1 = alt.Chart(by_workingday_df.sort_values(by="instant", ascending=False)).mark_bar().encode(
        x='workingday',
        y='instant',
        tooltip=['workingday', 'instant']
    ).properties(
        title="Working Day to Rental",
        width=500,
        height=300
    )
    st.altair_chart(chart1, use_container_width=True)

with col2:
    chart2 = alt.Chart(by_workingday_hour_df).mark_bar().encode(
        x=alt.X('hr:O', title='Hour'),
        y=alt.Y('instant:Q', title='Rental Counts'),
        color='workingday:N',
        tooltip=['hr', 'instant', 'workingday']
    ).properties(
        title="Hourly Rental Counts by Working Day",
        width=500,
        height=300
    )
    st.altair_chart(chart2, use_container_width=True)

st.caption('Copyright (c) Farrel Jonathan Vickeldo 2024')