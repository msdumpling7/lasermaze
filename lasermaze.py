class Maze:
    def __init__(self, grid_width: int, grid_height:int, start_x: int, start_y: int, mirror_list:dict, direction: str):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.start_x = start_x
        self.start_y = start_y
        self.mirror_list = mirror_list
        self.direction = direction
        self.path = set()
        self.num_squares = 0
        self.ans = None

    #define traversal function
    def laser_traverse (self, x: int, y: int, curr_direction: str):
        curr_x = x
        curr_y = y
        
        # Check if laser hits wall
        if curr_x + 1 == self.grid_width and curr_direction == "E":
            self.ans = [self.num_squares, curr_x, curr_y] 
            return
        elif curr_y + 1 == self.grid_height and curr_direction == "N":
            self.ans = [self.num_squares, curr_x, curr_y] 
            return
        elif curr_x == 0 and curr_direction == "W":
            self.ans = [self.num_squares, curr_x, curr_y] 
            return
        elif curr_y == 0 and curr_direction == "S":
            self.ans = [self.num_squares, curr_x, curr_y] 
            return

        # get new direction
        
        if curr_direction == "N":
            curr_y += 1
        elif curr_direction == "S":
            curr_y -= 1
        elif curr_direction == "E":
            curr_x += 1
        elif curr_direction == "W":
            curr_x -= 1

        #check if mirror at new location, change curr_direction if needed
        if (curr_x, curr_y) in self.mirror_list:
            if self.mirror_list[(curr_x, curr_y)] == "/":
                if (curr_x, curr_y) not in self.path:
                    self.path.add((curr_x, curr_y))
                else:
                    self.ans = [-1, None, None]
                    return
                if curr_direction == "N":               
                    curr_direction = "E"
                elif curr_direction == "S":
                    curr_direction = "W"
                elif curr_direction == "E":
                    curr_direction = "N"
                elif curr_direction == "W":
                    curr_direction = "S"
            elif self.mirror_list[(curr_x, curr_y)] == "\\":
                if (curr_x, curr_y) not in self.path:
                    self.path.add((curr_x, curr_y))
                else:
                    self.ans = [-1, None, None]
                    return
                if curr_direction == "N":               
                    curr_direction = "W"
                elif curr_direction == "S":
                    curr_direction = "E"
                elif curr_direction == "E":
                    curr_direction = "S"
                elif curr_direction == "W":
                    curr_direction = "N"

        self.num_squares += 1
        return self.laser_traverse(curr_x, curr_y, curr_direction)

    def run(self):
        self.laser_traverse(self.start_x,self.start_y,self.direction)

#write main function
if __name__=='__main__':
    array=[]
    mirror={}
    # read input file
    input_file = open("input.txt","r")
 
    for line in input_file:
        array.append(line.rstrip('\n'))
    grid = array[0].split()
    start = array[1].split()
    for l in array[2:]:
        mirror[(int(l.split()[0]),int(l.split()[1]))]=l.split()[2]
    maze1 = Maze(int(grid[0]),int(grid[1]),int(start[0]),int(start[1]),mirror,start[2])
    maze1.run()

    #write output to output file
    with open ('output.txt', 'w') as f:
        f.write (str(maze1.ans[0]))
        if maze1.ans[0] != -1:
            f.write('\n' +str(maze1.ans[1])+ " " + str(maze1.ans[2])) 
    f.close()  





