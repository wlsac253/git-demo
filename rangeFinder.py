from pathlib import Path
import numpy as np


path=Path("/home/chensgroup/Desktop/irregularmodel/_2D_model/result_regular/real")

def max_min_value(m):
    files_set=[["m2n2","m2n3","m2n4"],["m3n3","m3n4","m3n5","m3n6"],["m4n4","m4n5","m4n6","m4n7","m4n8"]]
    data_set=files_set[m-1]

    file01=open(path/data_set[0],"r")
    line01=file01.readline()
    count=0
    while line01:
        count+=1
        line01=file01.readline()
    num_datapoint=count

    min_y=0
    max_y=0
    for file_name in data_set:
        file=open(path/file_name,"r")
        line=file.readline()
        while line:
            y=float(line)
            if (y<=min_y):
                min_y=y
            if(y>=max_y):
                max_y=y
            line=file.readline()
    return [[min_y],[max_y]]


def max_min_file():
    file=open(path/"max_min_list","w")
    for m in range(1,4):
        min_max=max_min_value(m)
        file.write(str(min_max[0][0])+"\n")
        file.write(str(min_max[1][0])+"\n")
    file.close()




vector=max_min_value(1)
print("min/max vector is: ",vector,"value: ",vector[0][0],vector[1][0])
vector=max_min_value(2)
print("min/max vector is: ",vector,"value: ",vector[0][0],vector[1][0])
vector=max_min_value(3)
print("min/max vector is: ",vector,"value: ",vector[0][0],vector[1][0])

max_min_file()
