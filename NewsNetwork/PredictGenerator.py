import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.metrics import median_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2
from sklearn.metrics import accuracy_score as acc
import math

'''
This module includes functions related to making and evaluat-
ing predictions on data based on a given model
'''
def unnormalize(price,max_price,min_price):
    '''Revert values to their unnormalized amounts'''
    price = price*(max_price-min_price)+min_price
    return(price)

    
# Analyzes the predictions to see how accurate they are
def model_show_predictions(predictions, y, deeper, wider, dropout, learning_rate,
    max_price=0, min_price=0):
    print('Predictions with PARAMS deeper={}_wider={}_dropout={}_lr={}'
        .format(deeper, wider, dropout, learning_rate))

    unnorm_predictions = []
    for pred in predictions:
        unnorm_predictions.append(pred)

    unnorm_y = []
    for y_pt in y:
        unnorm_y.append(y_pt)



    # print("Summary of actual opening price changes")
    # print(pd.DataFrame(unnorm_y, columns=[""]).describe())
    # print()
    # print("Summary of predicted opening price changes")
    # print(pd.DataFrame(unnorm_predictions, columns=[""]).describe())

    # # Plot the predicted (blue) and actual (green) values
    # plt.figure(figsize=(12,4))
    # plt.plot(unnorm_predictions)
    # plt.plot(unnorm_y)
    # plt.title("Predicted (blue) vs Actual (green) Opening Price Changes with params deeper={}_wider={}_dropout={}_lr={}".
    #     format(deeper,wider,learning_rate,dropout))
    # plt.xlabel("Testing instances")
    # plt.ylabel("Change in Opening Price")

    # Create lists to measure if opening price increased or decreased
    direction_pred = []
    for pred in unnorm_predictions:
        if pred >= 0.5:
            direction_pred.append(1)
        else:
            direction_pred.append(0)
    direction_test = []
    for value in unnorm_y:
        if value >= 0.5:
            direction_test.append(1)
        else:
            direction_test.append(0)

    # # Calculate errors
    # _mae = mae(unnorm_y, unnorm_predictions) #median absolute error
    # _rmse = np.sqrt(mse(y, predictions)) # root mean squared error
    # _r2 = r2(unnorm_y, unnorm_predictions) #R squared error

    # print("Median absolute error: {}".format(_mae))
    # print("Root mean suqared error: {}".format(_rmse))
    # print("R squared error: {}".format(_r2))

    # Calculate if the predicted direction matched the actual direction
    direction = acc(direction_test, direction_pred)
    print('len of direction_test: ' + str(len(direction_test)))
    print('len of direction_pred: ' + str(len(direction_pred)))
    print('direction: ' + str(direction))
    direction = round(direction,4)*100
    print("Predicted values matched the actual direction {}% of the time.".format(direction))
    print('y head: \n' + str(y[0:10]))
    print('predictions head \n' + str(predictions[0:10]))

   # plt.show()

    plt.savefig('./RESULTS_deeper={}_wider={}_dropout={}_lr={}.png'.
        format(deeper, wider, dropout, learning_rate))


