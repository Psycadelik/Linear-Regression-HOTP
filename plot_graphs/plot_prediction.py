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
