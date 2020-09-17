# Cost function
def cost_function(theta, training_data):
    result = 0
    for index, training_set in training_data.iterrows():
        predicted = hypothesis(theta, training_set['area'])
        square_diff = (predicted - training_set['price']) ** 2
        result = square_diff / (2 * len(training_data.index))
    return result
