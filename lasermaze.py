class Maze:
    def __init__(self, grid_width: int, grid_height:int, start_x: int, start_y: int, mirror_list:dict, direction: str):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.start_x = start_x
        self.start_y =  start_y
        self.mirror_list = mirror_list
        self.direction = direction
        self.path = set()
        self.num_squares = 0

    #define traversal function
    def laser_traverse (self, x: int, y: int, curr_direction: str):
        curr_x = x
        curr_y = y
        
        # Check if laser hits wall
        if curr_x +1 == self.grid_width or curr_y +1 == self.grid_height:
            return [num_square, curr_x, curr_y] 

        
        # get new direction
        else:
            if curr_direction == "N":
                curr_y += 1
            elif curr_direction == "S":
                curr_y -= 1
            elif curr_direction == "E":
                curr_x+= 1
            elif curr_direction == "W"
                curr_x-=1

            #check if have mirror at new location, change curr_direction if needed
            if self.mirror_list[(curr_x, curr_y)] == "/":
                if (curr_x, curr_y) not in self.path:
                    self.path.add((curr_x, curr_y))
                else:
                    return [-1, None, None]
                if curr_direction == "N":               
                    curr_direction = "E"
                elif curr_direction == "S":
                    curr_direction = "w"
                elif curr_direction ="E":
                    curr_direction = "N"
                elif curr_direction == "w":
                    curr_direction == "S"
            if self.mirror_list[(curr_x, curr_y)] == "\":
                if (curr_x, curr_y) not in self.path:
                    self.path.add((curr_x, curr_y))
                else:
                    return [-1, None, None]
                if curr_direction == "N":               
                    curr_direction = "w"
                elif curr_direction == "S":
                    curr_direction = "E"
                elif curr_direction ="E":
                    curr_direction = "S"
                elif curr_direction == "w":
                    curr_direction == "N"

            self.num_squares += 1
            return self.laser_traverse(curr_x, curr_y, curr_direction)
        

#write main function
if '__name__'=='__main__':
    array=[]
    mirror={}
    #parse input file from indir

    #read input file by line
    for line in input_file:
        array.append(line.rstrip('\n'))
    grid = map(int, array[0].split())
    start = array[1].split()
    for array in array[2:]:
        mirror[(array.split()[0],array.split()[1])]=array.split()[2]
    maze_parameter = maze(grid[0],grid[1],int(start[0]),int(start[1]),mirror,start[2])
    count, x, y = laser_traverse (int(start[0]),int(start[1]),start[2])

    #write output to outdir
        





