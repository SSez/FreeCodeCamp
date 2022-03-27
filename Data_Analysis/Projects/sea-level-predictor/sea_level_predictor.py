import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    line = linregress(x, y)
    years = pd.Series([i for i in range(df['Year'][0], 2050 + 1)])
    y_prediction = line.slope * years + line.intercept
    plt.plot(years, y_prediction, color='red')

    # Create second line of best fit
    df_new = df.loc[df['Year'] >= 2000]
    new_x = df_new["Year"]
    new_y = df_new["CSIRO Adjusted Sea Level"]
    second_line = linregress(new_x, new_y)
    s_years = pd.Series([i for i in range(2000, 2050 + 1)])
    ys_prediction = second_line.slope * s_years + second_line.intercept
    plt.plot(s_years, ys_prediction, color='black')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
