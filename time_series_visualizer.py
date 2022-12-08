import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'], index_col = 'date')

# Clean data
df = df.query('value > value.quantile(0.025) & value < value.quantile(0.975)')


def draw_line_plot():
    # Draw line plot
    import matplotlib.dates as mdates
    fig, ax = plt.subplots(figsize = (25, 10))
    ax.plot(df, color = 'red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth = [1, 7]))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month_name()
    df_bar['year'] = df_bar.index.year

    # Draw bar plot
    fig, ax = plt.subplots(figsize = (15, 10))
    sns.barplot(x = 'year', y = 'value', data = df_bar,
                  hue = 'month', hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                  palette = 'tab10', ci = None)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title = "Months", loc = 'upper left')
 
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize = (25, 10), dpi = 100)
    sns.boxplot(data = df_box, x = 'year', y = 'value', palette = "tab10", ax = ax[0]).set(title = "Year-wise Box Plot (Trend)", xlabel = "Year", ylabel = "Page Views")
    sns.boxplot(data = df_box, x = 'month', y = 'value', palette = "tab10", order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax = ax[1]).set(title = "Month-wise Box Plot (Seasonality)", xlabel = "Month", ylabel = "Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
