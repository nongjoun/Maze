import turtle


# กำหนดค่าคงที่แทนสัญลักษณ์ในเขาวงกต
OBSTACLE = 'X'     # สิ่งกีดขวาง
TRIED = '.'        # จุดที่ลองแล้ว
PART_OF_PATH = 'P' # เส้นทางที่ถูกต้อง
DEAD_END = 'X'     # ทางตัน




class Maze:
    def __init__(self, maze_file_name):
        self.maze_list = []
        self.start_row = 0
        self.start_col = 0

        with open(maze_file_name, 'r') as maze_file:
            for row_idx, line in enumerate(maze_file):
                row_list = list(line.strip())
                if 'S' in row_list:
                    self.start_row = row_idx
                    self.start_col = row_list.index('S')
                self.maze_list.append(row_list)

        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])


        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(- (self.columns_in_maze - 1) / 2 - .5,
                                    - (self.rows_in_maze - 1) / 2 - .5,
                                    (self.columns_in_maze - 1) / 2 + .5,
                                    (self.rows_in_maze - 1) / 2 + .5)


        
        

    def draw_maze(self):
        self.t.speed(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate, -y + self.y_translate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
            self.move_turtle(col, row)

        color_map = {
            PART_OF_PATH: 'green',
            OBSTACLE: 'red',
            TRIED: 'black',
            DEAD_END: 'red'
        }
        
        if val in color_map:
            self.drop_bread_crumb(color_map[val])

    def is_exit(self, row, col):
        return (row == 0 or row == self.rows_in_maze - 1 or 
                col == 0 or col == self.columns_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]

def search_from(maze, start_row, start_column):
    maze.update_position(start_row, start_column)

    # ฐานของการหยุดทำงาน (Base Cases)
    if maze[start_row][start_column] == OBSTACLE:
        return False

    if maze[start_row][start_column] in [TRIED, DEAD_END]:
        return False

    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True

    maze.update_position(start_row, start_column, TRIED)

    # ลองไปทุกทิศทาง (ขึ้น, ลง, ซ้าย, ขวา)
    found = (search_from(maze, start_row - 1, start_column) or
             search_from(maze, start_row + 1, start_column) or
             search_from(maze, start_row, start_column - 1) or
             search_from(maze, start_row, start_column + 1))

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)

    return found

if __name__ == "__main__":
    my_maze = Maze('mazeX.txt')
    my_maze.draw_maze()
    my_maze.update_position(my_maze.start_row, my_maze.start_col)

    search_from(my_maze, my_maze.start_row, my_maze.start_col)

    turtle.done()
