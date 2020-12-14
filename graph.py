import math
from terminalplot import plot
import pandas as pd
import prepareData


def draw_graph():
    courses = ["dia","cd","hoa","khtn","su","anh","van","toan","sinh","li"]
    data_2018,data_2019,data_2020 = prepareData.data_for_graph()
    x_vals, y_vals,test_vals1,test_vals2 = [],[],[],[]
    for score in data_2018:
        x_vals.append(score.index)
        y_vals.append(score.values)
        
    for i in x_vals:
        for j in i:
            test_vals1.append(j)

    for i in y_vals:
        for j in i:
            test_vals2.append(j)
    plot(test_vals1, test_vals2)
draw_graph()


