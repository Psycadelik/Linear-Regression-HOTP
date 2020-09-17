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
    
