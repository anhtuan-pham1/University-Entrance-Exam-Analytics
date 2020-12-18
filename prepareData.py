import pandas as pd

def open_csv():
    diem_thi_2018 = pd.read_csv("diemthi/2018.csv")
    diem_thi_2019 = pd.read_csv("diemthi/2019.csv")
    diem_thi_2020 = pd.read_csv("diemthi/2020.csv")

    return diem_thi_2018,diem_thi_2019,diem_thi_2020

def remove_unnecessary_column():
    diem_thi_2018,diem_thi_2019,diem_thi_2020 = open_csv()

    diem_thi_2018 =  diem_thi_2018.apply (pd.to_numeric, errors='coerce')
    del diem_thi_2018["Unnamed: 0"]

    diem_thi_2019 =  diem_thi_2019.apply (pd.to_numeric, errors='coerce')
    del diem_thi_2019["Unnamed: 0"]

    diem_thi_2020 =  diem_thi_2020.apply (pd.to_numeric, errors='coerce')
    del diem_thi_2020["Unnamed: 0"]

    return diem_thi_2018,diem_thi_2019,diem_thi_2020

def average_mon():
    diem_2018,diem_2019,diem_2020 = remove_unnecessary_column()
    courses = ["dia","cd","hoa","khtn","su","anh","van","toan","sinh","li"]
    dict_2018 = dict.fromkeys(courses, None)
    dict_2019 = dict.fromkeys(courses, None)
    dict_2020 = dict.fromkeys(courses, None)

    for course in courses:
        average = diem_2018[course].mean(skipna= True).round(decimals=2)
        dict_2018[course] = average

    for course in courses:
        average = diem_2020[course].mean(skipna= True).round(decimals=2)
        dict_2020[course] = average
    
    for course in courses:
        average = diem_2019[course].mean(skipna= True).round(decimals=2)
        dict_2019[course] = average

    return dict_2018,dict_2019,dict_2020

def data_for_graph():
    diem_2018,diem_2019,diem_2020 = remove_unnecessary_column()
    courses = ["dia","cd","hoa","khtn","su","anh","van","toan","sinh","li"]
    data_2018 = []
    data_2019 = []
    data_2020 = []

    for course in courses:
        unique_score = diem_2018[course].value_counts()
        unique_score.sort_index(inplace = True)
        data_2018.append(unique_score)
        print(data_2018)

    for course in courses:
        unique_score = diem_2019[course].value_counts()
        unique_score.sort_index(inplace = True)
        data_2019.append(unique_score)

    for course in courses:
        unique_score = diem_2020[course].value_counts()
        unique_score.sort_index(inplace = True)
        data_2020.append(unique_score)
        
    return data_2018,data_2019,data_2020

def course_combination():
    course_comb={'A':["toan","li","hoa"],'B':["toan","hoa","sinh"],'C':["van","su","dia"],'D':["toan","van","anh"]}
    diem_thi_2018,diem_thi_2019,diem_thi_2020 = remove_unnecessary_column()
    diem_thi_to_hop_2018 = []
    diem_thi_to_hop_2019 = []
    diem_thi_to_hop_2020 = []
    for key in course_comb:
        diem_thi_to_hop_2018.append(diem_thi_2018[course_comb[key]])
        diem_thi_to_hop_2019.append(diem_thi_2019[course_comb[key]])
        diem_thi_to_hop_2020.append(diem_thi_2020[course_comb[key]])
    return diem_thi_to_hop_2018,diem_thi_to_hop_2019,diem_thi_to_hop_2020



