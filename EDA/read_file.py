import pandas as pd
from os import listdir, path
from . import generate_html
def read_file():
    file = ""
    files_list =dict(enumerate([i for i in listdir() if path.splitext(i)[1] in ['.csv', '.xlsx']]))
    print(pd.DataFrame(files_list,index=range(1)).T)
    while True:
        try:
            file_number = int(input('Type the number of the file :'))
            if file_number > len(files_list) -1 or file_number < 0:
                print("You enterd number is out ranged")
            else:
                break
        except ValueError:
            print("Please Enter a Vaild Number Not a String")


    filename = files_list[file_number]

    if path.splitext(filename)[1] == ".csv":
        file = pd.read_csv(filename)
    elif path.splitext(filename)[1] == ".xlsx":
        file = pd.read_excel(filename)


    generate_html.generate_html(file, path.splitext(filename)[0])