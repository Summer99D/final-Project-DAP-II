from shiny import App, render, ui, reactive
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Define the UI
app_ui = ui.page_fluid(
    ui.h2("Correlation between temperature and crimes recorded in Chicago", 
          style="text-align: center; padding: 20px; background-color: #f8f9fa;"),
    ui.input_slider(
        id='temp_slider',
        label='Select Temperature (°F):',
        min=10,
        max=100,
        value=50,
        step=1,
        animate=True
    ),
    ui.output_plot('crime_heatmap')
)

def server(input, output, session):
    @reactive.Calc
    def process_data():
        # Load data
        df = pd.read_csv('/Users/samarnegahdar/Desktop/Final_project/final-Project-DAP-II/Datasets/merged_data.csv')
        
        # Step 1: Calculate total crimes per day per zipcode for each temperature
        daily_crimes = df.groupby(['DATE', 'ZIP_CODE', 'TAVG'])['Crime Count'].sum().reset_index()
        
        # Step 2: Filter for selected temperature
        temp_data = daily_crimes[daily_crimes['TAVG'] == input.temp_slider()]
        
        # Step 3: Calculate average crimes for this temperature in each ZIP code
        avg_crimes = temp_data.groupby('ZIP_CODE')['Crime Count'].mean().reset_index()
        
        # Convert ZIP codes to string for merging
        avg_crimes['ZIP_CODE'] = avg_crimes['ZIP_CODE'].astype(str).str.zfill(5)
        
        return avg_crimes

    @render.plot
    def crime_heatmap():
        avg_crimes = process_data()

        # Load Chicago ZIP code shapefile
        url = "https://data.cityofchicago.org/api/geospatial/unjd-c2ca?method=export&format=GeoJSON"
        chicago_gdf = gpd.read_file(url)
        
        # Convert zip codes to string for merging
        chicago_gdf['zip'] = chicago_gdf['zip'].astype(str).str.zfill(5)

        # Merge crime data with geodataframe
        merged_gdf = chicago_gdf.merge(avg_crimes, left_on='zip', right_on='ZIP_CODE', how='left')
        merged_gdf['Crime Count'] = merged_gdf['Crime Count'].fillna(0)

        # Create the plot
        fig, ax = plt.subplots(figsize=(12, 8))
        merged_gdf.plot(
            column='Crime Count',
            ax=ax,
            legend=True,
            cmap='YlOrRd',
            missing_kwds={'color': 'lightgrey'},
            legend_kwds={'label': 'Average Crime count'},
            edgecolor='black',
            linewidth=0.5
        )

        plt.title(f"Average Crime Count at {input.temp_slider()}°F")
        plt.axis('off')
        return fig

# Create and run the app
app = App(app_ui, server)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001)