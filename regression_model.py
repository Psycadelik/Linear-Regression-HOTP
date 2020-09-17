import numpy
import pandas
from ipywidgets import *
import matplotlib.pyplot as plot
from prediction_parameters import cost, hypothesis
from plot_graphs import plot_cost, plot_prediction


%matplotlib inline

dataframe = pandas.read_csv('houses_data.csv')

# plotting our training sample
plot.scatter(dataframe.area, dataframe.price)
plot.title('House Prices')
plot.xlabel('Area')
plot.ylabel('Price')
plot.show()

# Visualize cost and Hypothesis function
fig, axes = plot.subplots(nrows=1, ncols=2, figsize=(5, 5))

# Plot the graphs
plot_prediction(theta=1.0)
plot_cost(theta=1.0)
fig.tight_layout()

