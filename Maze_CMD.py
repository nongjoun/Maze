import time  # สำหรับหน่วงเวลา

def print_maze(maze, current):
    """
    แสดงเขาวงกตพร้อมตำแหน่งปัจจุบัน (S)
    
    Args:
    maze: 2D list ที่แสดงเขาวงกต
    current: ตำแหน่งปัจจุบันของ S (row, col)
    """
    for row in range(len(maze)):
        line = ""
        for col in range(len(maze[0])):
            if (row, col) == current:
                line += "S "  # ตำแหน่งปัจจุบัน
            elif maze[row][col] == "X":
                line += "X "  # กำแพง
            elif maze[row][col] == " ":
                line += ". "  # ทางเดิน
        print(line)
    print("\n")  # เพิ่มบรรทัดว่างเพื่อความสวยงาม


def solve_maze_with_visualization(maze, start, end):
    """
    แก้ปัญหาเขาวงกตพร้อมแสดงวิธีการเดินทีละขั้นตอน
    
    Args:
    maze: 2D list ที่แสดงเขาวงกต (X = กำแพง, " " = ทางเดิน)
    start: จุดเริ่มต้น (row, col)
    end: จุดเป้าหมาย (row, col)
    
    Returns:
    path: เส้นทางที่เจอเป้าหมาย หรือ None หากไม่มีทางไปถึง
    """
    rows, cols = len(maze), len(maze[0])
    stack = []  # ใช้สำหรับเก็บตำแหน่งที่ต้องสำรวจ
    visited = set()  # เก็บตำแหน่งที่เคยสำรวจแล้ว

    # ทิศทางการเคลื่อนที่ (left, down, right, up)
    directions = [ (0, -1), (1, 0), (0, 1),(-1, 0)]

    # เริ่มต้นจากจุด start
    stack.append((start, [start]))

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        row, col = current

        # แสดงเขาวงกตพร้อมตำแหน่งปัจจุบัน
        print_maze(maze, current)
        time.sleep(0.5)  # หน่วงเวลาเพื่อให้เห็นการเคลื่อนไหว

        # ตรวจสอบว่าเจอจุดเป้าหมายหรือไม่
        if current == end:
            print("Goal reached!")
            return path

        # สำรวจเส้นทางถัดไป
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)

            # ตรวจสอบว่าอยู่ในขอบเขตและไม่ใช่กำแพงหรือไม่เคยสำรวจ
            if (
                0 <= new_row < rows and
                0 <= new_col < cols and
                maze[new_row][new_col] == " " and
                new_pos not in visited
            ):
                stack.append((new_pos, path + [new_pos]))

    # หากไม่เจอเส้นทางให้คืนค่า None
    print("No path found.")
    return None


# แสดงเขาวงกตจากภาพ
maze = [
    ["X", "X", "X", "X", "X", "X", "X"],
    ["X", " ", "X", "X", " ", " ", "X"],
    ["X", " ", " ", " ", "X", " ", "X"],
    ["X", " ", "X", " ", "X", " ", "X"],
    ["X", " ", "X", " ", "X", " ", "X"],
    ["X", " ", "X", " ", " ", " ", "X"],
    ["X", " ", "X", " ", "X", "X", "X"],
    ["X", " ", "X", " ", " ", " ", "X"],
    ["X", " ", "X", "X", "X", " ", "X"],
]

start = (8, 1)  # จุดเริ่มต้น (S)
end = (8, 5)    # จุดเป้าหมาย (E)

# เรียกใช้งานฟังก์ชัน
path = solve_maze_with_visualization(maze, start, end)
