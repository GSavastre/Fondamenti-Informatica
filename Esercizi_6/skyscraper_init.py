def import_csv(file_name: str):

    imported_matrix = []

    values = []
    
    with open(file_name, "r") as f3:
        for line in f3:
            #imported_matrix.append(map(float,line.split(',')))

            values = list(map(float, line.split(',')))
            imported_matrix.append(values)
    
    return imported_matrix

def skyscrapers(mat_text: str):

    matrix = import_csv(mat_text)

    cont_matrix = [[ 0 for x in range(len(matrix[0])+2)]for y in range(len(matrix) + 2)]

    rows = len(matrix)

    cols = len(matrix[0])

    for y in range(rows):
        for x in range(cols):
            cont_matrix[y+1][x+1] = int(matrix[y][x])

    for y in range(rows):
        
        max_sx = matrix[y][0]
        max_dx = matrix[y][len(matrix[0])-1]
        
        for x in range(cols):
            if matrix[y][x] > max_sx:
                max_sx = matrix[y][x]
                cont_matrix[y+1][0] += 1 
                
            if matrix[y][len(matrix[0])- x - 1] > max_dx:
                max_dx = matrix[y][len(matrix[0])-x]
                cont_matrix[y+1][len(matrix[0])+1] += 1


    for x in range(cols):
        max_up = matrix[0][x]
        max_dwn = matrix[len(matrix)-1][x]

        for y in range(rows):
            if matrix[y][x] > max_up:
                max_up = matrix[y][x]
                cont_matrix[0][x+1] += 1

            if matrix[len(matrix)- y - 1][x] > max_dwn:
                max_dwn = matrix[len(matrix)-y -1][x]
                cont_matrix[len(matrix)+1][x+1] += 1

    return cont_matrix

def main():
    matrix = skyscrapers("6_5_text.csv")


    for n in range(len(matrix)):
            print(matrix[n], end="\n")
            
if __name__ == "__main__":
    main()
