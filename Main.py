from Data import *

class Main:
    def useroption():
        option = input('''
Choose one of these option:
0.Exit
1. University Entrance Exam result 2018
2. University Entrance Exam result 2018
3. University Entrance Exam result 2018
input:  ''')
        if(option not in ['0','1', '2', '3']):
            print('wrong input, please try again')
            option = '-1'
        return int(option)

    if __name__ == '__main__':
        while True:
            option = useroption()
            try:
                if option == 0:
                    print("Thank you for using our app!! Hope to see you again!!")
                    exit(0)
                else:
                    b = Data(option)
                    b.search_valedictorian(1)
            except Exception:
                print("Invalid input!!! Please try to enter another option in the list!")
                  