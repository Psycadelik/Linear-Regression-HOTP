import numpy as np
import matplotlib.pyplot as plot
import pandas
from prediction_parameters.cost import cost_function
from prediction_parameters.hypothesis import hypothesis

dataframe = pandas.read_csv('houses_data.csv')

# function to plot cost
def plot_cost(theta):
    x2 = np.linspace(-0.5, 2.5)
    y2 = [cost_function(x, training_data=dataframe) for x in x2]

    axes[1].set_ylim(0, 3.5)
    axes[1].set_xlim(-0.5, 2.5)

    axes[1].set_title('Cost Function')
    axes[1].set_xlabel(r'$\theta$')
    axes[1].set_ylabel(r'$J(\theta)$')

    axes[1].scatter(theta, cost_function(theta, dataframe), label='cost')
    axes[1].legend(loc='upper left')
    axes[1].plot(x2, y2)

# function to plot prediction
def plot_prediction(theta):
    x1 = np.linspace(0.0, 5.0)
    y1 = np. linspace(0.0, 5.0)

    axes[0].set_ylim(0, 5.0)

    axes[0].set_title('House Prices')
    axes[0].set_xlabel('Area(feet$^2$)')
    axes[0].set_ylabel('Price')

    axes[0].scatter(dataframe.area, dataframe.price)
    axes[0].plot(dataframe.area, theta * dataframe.price, color='red', label='prediction')
    axes[0].legend(loc='upper left')


# Visualize cost and hypothesis functions
fig, axes = plot.subplots(nrows=1, ncols=2, figsize=(5,5))

# Plot the graphs
plot_prediction(theta=1.0)
plot_cost(theta=1.0)
fig.tight_layout()

def update(theta = 1.0):
    axes[0].clear()
    axes[1].clear()

    plot_prediction(theta)
    plot_cost(theta)

interact(update)
