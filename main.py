import ita

def count_neighbors(data, i, j):
    """Đếm số lượng hàng xóm sống của một ô tại vị trí (i, j)."""
    neighbors = 0
    for x in range(max(0, i-1), min(len(data), i+2)):
        for y in range(max(0, j-1), min(len(data[0]), j+2)):
            if (x, y) != (i, j) and data[x][y] == 1:
                neighbors += 1
    return neighbors

def lifegame_rule(cur, neighbor):
    """Áp dụng luật của Game of Life."""
    if cur == 1:
        if neighbor < 2 or neighbor > 3:
            return 0
        else:
            return 1
    else:
        if neighbor == 3:
            return 1
        else:
            return 0

def lifegame_step(data):
    """Tính toán thế hệ tiếp theo từ thế hệ hiện tại."""
    new_data = ita.array.make2d(len(data), len(data[0]))
    for i in range(len(data)):
        for j in range(len(data[0])):
            neighbors = count_neighbors(data, i, j)
            new_data[i][j] = lifegame_rule(data[i][j], neighbors)
    return new_data

def lifegame(data, steps):
    """Tính toán các thế hệ của Game of Life và trả về một mảng 1D chứa các trạng thái."""
    results = ita.array.make1d(steps)
    results[0] = data
    for i in range(1, steps):
        results[i] = lifegame_step(results[i-1])
    return results
def draw_circle(r, center_y, center_x, color, image):
    # draw a circle with (center_x, center_y) as the center with "color" on the "image"
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            if (distance(i, j, center_y, center_x)) < r:
                image[i][j] = color
                
def distance(x1, y1, x2, y2):
    return ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5

def draw_game(state, image):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 1:  # if cell is alive
                draw_circle(0.5, i, j, [1, 1, 0], image)  # draw a yellow circle

# animation minh hoạ game of life với trạng thái khởi tạo là acorn
ani = lifegame(ita.lifegame_acorn(), 10)
ita.plot.animation_show(ani)



# vẽ ảnh minh hoạ game of life với trạng thái khởi tạo là acorn
state = ita.lifegame_acorn()
image = ita.array.make3d(len(state), len(state[0]), 3)
draw_game(state, image)
ita.plot.image_show(image)

