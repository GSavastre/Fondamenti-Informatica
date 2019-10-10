def smooth(mat):
    rows = len(mat)
    cols = len(mat[0])

    new_matrix = [[ 0.0 for x in range(cols)]for y in range(rows)]

    cont = 1

    delta = [-1, 0 , 1]

    dx = delta[0]

    dy = delta[1]

    scroll_delta = -1

    index_delta = 0

    for y in range(rows):
        for x in range(cols):
            new_matrix[y][x] = mat[y][x]
            for n in range(4):
                if 0 <= x + dx < cols and 0 <= y + dy < rows:
                    #print("sono in: ",mat[y][x],"ho: ",new_matrix[y][x]," prendo:",mat[y+dy][x+dx])
                    new_matrix[y][x] += mat[y+dy][x+dx]
                    #print("adesso ho", new_matrix[y][x])
                    cont += 1
                    #print("Il divisore è ",cont)
                    
                dy = dx

                if dx == delta[0] or dx == delta[2]:
                    scroll_delta *= -1

                index_delta += scroll_delta 
                
                dx = delta[index_delta]
                

            new_matrix[y][x] /= cont
            #print("Che fa: ",new_matrix[y][x])
            #print("----------nuovo-elemento----------")
            cont = 1
            

    return new_matrix

def main():
    matrix = [[2.0, 4.0, 3.0, 8.0],
          [9.0, 3.0, 2.0, 7.0],
          [5.0, 6.0, 9.0, 1.0]]
    

    matrix = smooth(matrix)
    
    for n in range(len(matrix)):
        print(matrix[n], end="\n")
    

if __name__ == "__main__":
    main()
