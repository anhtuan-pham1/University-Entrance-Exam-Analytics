from Data import Data
import pandas as pd
import math 
from termcolor import colored

class Graph:
    def __init__(self,option):
        self.data = Data(option).get_graph_data()
        self.courses = ["dia","cd","hoa","khtn","su","anh","van","toan","sinh","li"]

    #round of 500
    def print_graph(self, stat: int):
        graph_bar = ""
        for i in range (1,stat,500):
            graph_bar = graph_bar + "|"
        return graph_bar
    
    def graph_ratio(self):
        course_counter = 0
        for grade in self.data:
            total = grade.sum()
            print(self.courses[course_counter])
            serie_index = 0
            for i in grade:
                percentage = (int(i)*100)/total
                round_stat = math.ceil(i / 500.0) * 500.0
                graph_bar = self.print_graph(int (round_stat))
                print(colored('{message: <{width}}'.format(message=str(round(grade.index[serie_index],2)), width=4),'blue') + " :"+ graph_bar + "  " + colored(str(i),'yellow'))
                serie_index += 1
            print("--------------------------------------------------------------------------------------------------------------")
            course_counter += 1
