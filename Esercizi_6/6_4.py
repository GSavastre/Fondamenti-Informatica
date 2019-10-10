from skyscraper_init import *

class Skyscraper():
    def __init__(self, matrix_path):
        self._matrix = skyscrapers(matrix_path)
        self._rows = len(self._matrix)
        self._cols = len(self._matrix[0])

    def print(self):
       for y in range(self._rows):
            for x in range(self._cols):
                print('{:4}'.format(self._matrix[y][x]), end="")
            print("")
            
    def rect(self):
        return self._rows -3, self._cols -3

    def get_max_values(self, ctr_x: int, ctr_y: int):
        max_w = max_h = -1
        for y in range(self._rows):
                if self._matrix[y][ctr_x] > max_w:
                    max_w = self._matrix[y][ctr_x]

        for x in range(self._cols):
                if self._matrix[ctr_y][x] > max_h:
                    max_h = self._matrix[ctr_y][x]

        return max_w, max_h

    def get_val(self, x: int, y: int)-> str:
        return str(self._matrix[y][x])       
                        
    def play_at(self, x: int, y: int):
        max_w, max_h = self.get_max_values(x, y)
        print(max_w, max_h)

        self._matrix[y][x] += 1

        if self._matrix[y][x] > max_w or self._matrix[y][x] > max_h:
            self._matrix[y][x] = 0
        

def main():
    
    file = "6_5_text.csv"
    play_area = Skyscraper(file)
    coord = [-1]*2
    
    print("Le coordinate vanno da:\n0(zero) a ",play_area.rect()[0],"per le righe\n0(zero) a ",play_area.rect()[1],"per le colonne")
    str_coord = input("Scegli le coordinate x,y (separate da uno spazio) digita -1 per terminare: ")
    
    coord[0] = int(str_coord.split(" ")[0])
    coord[1] = int(str_coord.split(" ")[1])

    while(0 <= coord[0] <= play_area.rect()[1] and 0 <= coord[1] <= play_area.rect()[0]):
        play_area.play_at(coord[0] + 1, coord[1] + 1)
        print(play_area.get_val(coord[0] + 1, coord[1] + 1))
        
        str_coord = input("Scegli le coordinate(separate da uno spazio) digita -1 per terminare: ")
        coord[0] = int(str_coord.split(" ")[0])
        coord[1] = int(str_coord.split(" ")[1])
        

    play_area.print()
    
if __name__ == "__main__":
    main()
