import csv

def get_file(f):

    reader = csv.reader(f)
    cells = list()
    for line in reader:
        if(line[0] != ""):
            cells.append(line)

    return cells
