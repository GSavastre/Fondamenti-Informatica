from es52 import smooth

def import_csv(file_name: str):

    imported_matrix = []

    values = []
    
    with open(file_name, "r") as f3:
        for line in f3:
            #imported_matrix.append(map(float,line.split(',')))

            values = list(map(float, line.split(',')))
            imported_matrix.append(values)
    
    return imported_matrix        
                    


def main():
    matrix = import_csv("5_3_text.csv")
    
    matrix = smooth(matrix)

    for n in range(len(matrix)):
        print(matrix[n], end="\n")

if __name__ == "__main__":
    main()
