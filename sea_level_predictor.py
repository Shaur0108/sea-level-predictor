import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all data)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # From 1880 to 2050 (we want to predict until 2050)
    plt.plot(years_extended, [slope1 * year + intercept1 for year in years_extended], label='Best Fit Line (All Data)', color='blue')

    # Create second line of best fit (using data from year 2000 onward)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Only predict from year 2000 onwards
    years_recent_extended = range(2000, 2051)
    plt.plot(years_recent_extended, [slope2 * year + intercept2 for year in years_recent_extended], label='Best Fit Line (2000-Present)', color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add a legend
    plt.legend()

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
