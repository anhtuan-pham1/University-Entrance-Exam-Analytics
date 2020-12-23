from Data import Data
from Graph import Graph

def year_option():
    option = input('''
Choose one of these option:
0.Exit
1. University Entrance Exam result 2018
2. University Entrance Exam result 2019
3. University Entrance Exam result 2020
option:  ''')
    if(option not in ['0','1', '2', '3']):
        print('wrong input, please try again')
    return int(option)

def user_option():
    option = input('''
Choose one of these option:
0. Exit
1. Return to choose year option
2. Search for your grade
3. Search for valedictorian of each combination
4. Display visualized graph of each subject
option:  ''')
    if(option not in ['0','1', '2', '3','4']):
        print('wrong input, please try again')
        option = '-1'
    return int(option)

if __name__ == '__main__':
    while True:
        option = year_option()
        try:
            if option == 0:
                print("Thank you for using our app!! Hope to see you again!!")
                exit(0)
            data = Data(option)
            while True:
                user = user_option()
                if user == 0:
                    exit(0)
                elif user == 1:
                    break
                elif user == 2:
                    ID = input("Enter your ID: ")
                    data.search_grades(ID)
                elif user == 3:
                    data.search_valedictorian()
                elif user == 4:
                    graph = Graph(option).graph_ratio()
    
        except Exception:
            print("Invalid input!!! Please try to enter another option in the list!")