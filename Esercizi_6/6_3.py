def sum_near(values_list, index: int, cols: int) -> (float,int):
    cont = 1
    total_sum = values_list[index]

    if (index % cols) == 0:
        left = -1
    else:
        left = index - 1

    if ((index + 1)%cols) == 0:
        right = -1
    else:
        right = index + 1

    if left >= 0:
        total_sum += values_list[left]
        cont += 1

    if right < cols and right != -1:
        total_sum += values_list[right]
        cont += 1

    return total_sum, cont


def smooth(values_list, rows, cols):
    new_values_list = [0.0 for n in range(len(values_list))]
    values_summed = 0
    cont = 0

    for n in range(len(values_list)):
        result = sum_near(values_list, n, cols)
        
        values_summed += result[0]
        cont += result[1]

        if 0 <= n - cols:
            result = sum_near(values_list, n - cols, cols)
        
            values_summed += result[0]
            cont += result[1]

        if n + cols < len(values_list):
            result = sum_near(values_list, n + cols, cols)
        
            values_summed += result[0]
            cont += result[1]

        
        new_values_list[n] = values_summed / cont
        values_summed = cont = 0

    return new_values_list

def main():
    matrix = [2.0, 4.0, 3.0, 8.0,
              9.0, 3.0, 2.0, 7.0,
              5.0, 6.0, 9.0, 1.0]

    new_matrix = [0.0 for n in range(len(matrix))]

    rows = 3

    cols = len(matrix) // rows
    
    new_matrix = smooth(matrix, rows, cols)

    for n in range(len(new_matrix)):
            print('{:03.2f}'.format(new_matrix[n]),end=" ")
            if ((n + 1) % cols) == 0:
                print("")

if __name__ == "__main__":
    main()
