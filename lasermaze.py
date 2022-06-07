class Maze():
    def __init__(self, grid_width: int, grid_height: int, start_x: int, start_y: int, direction: str, mirror_list: dict):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.start_x = start_x
        self.start_y = start_y
        self.direction = direction
        self.mirror_list = mirror_list
        self.path = set()
        self.ans = None
        self.squares = 0

    def get_ans(self):
        return self.ans

    def check_wall(self, x: int, y: int, direction: str):
        if x + 1 == self.grid_width and direction == 'E':
            return True
        elif x == 0 and direction == 'W':
            return True
        elif y + 1 == self.grid_height and direction == 'N':
            return True
        elif y == 0 and direction == 'S':
            return True
        return False

    def laser_traverse(self, x: int, y: int, curr_direction: str):
        # check wall
        curr_x = x
        curr_y = y
        if self.check_wall(curr_x, curr_y, curr_direction) == True:
            self.ans = [self.squares, curr_x, curr_y]
            return

        # get new location
        if curr_direction == 'E':
            curr_x += 1
        elif curr_direction == 'W':
            curr_x -= 1
        elif curr_direction == 'N':
            curr_y += 1
        elif curr_direction == 'S':
            curr_y -= 1

        # check mirror, and change direction if needed
        # check if inifinite loop
        if (curr_x, curr_y) in self.mirror_list:
            if (curr_x, curr_y) in self.path:
                self.ans = [-1, None, None]
                return
            else:
                self.path.add((curr_x, curr_y))

            if self.mirror_list[(curr_x, curr_y)] == '/':
                if curr_direction == "N":
                    curr_direction = "E"
                elif curr_direction == "S":
                    curr_direction = "W"
                elif curr_direction == "E":
                    curr_direction = "N"
                elif curr_direction == "W":
                    curr_direction = "S"
            elif self.mirror_list[(curr_x, curr_y)] == '\\':
                if curr_direction == "N":
                    curr_direction = "W"
                elif curr_direction == "S":
                    curr_direction = "E"
                elif curr_direction == "E":
                    curr_direction = "S"
                elif curr_direction == "W":
                    curr_direction = "N"
        self.squares += 1
        return self.laser_traverse(curr_x, curr_y, curr_direction)

    def run(self):
        self.laser_traverse(self.start_x, self.start_y, self.direction)


# write main function
if __name__ == '__main__':
    array = []
    mirror = {}
    # read input file
    input_file = open("input.txt", "r")

    for line in input_file:
        array.append(line.rstrip('\n'))
    grid = array[0].split()
    start = array[1].split()
    for l in array[2:]:
        mirror[(int(l.split()[0]), int(l.split()[1]))] = l.split()[2]
    maze1 = Maze(int(grid[0]), int(grid[1]), int(
        start[0]), int(start[1]), start[2], mirror)
    maze1.run()
    ans = maze1.get_ans()

    # write output to output file
    with open('output.txt', 'w') as f:
        f.write(str(ans[0]))
        if ans[0] != -1:
            f.write('\n' + str(ans[1]) + " " + str(ans[2]))
    f.close()
