def main():
    with open("input", "r") as input_file:
        input_list = input_file.readlines()
        tree_grid = [[int(t) for t in l.strip()] for l in input_list]
    print(count_visible_trees(tree_grid))


def count_visible_trees(tree_grid):
    num_visible = (len(tree_grid) - 1) * 2 + (len(tree_grid[0]) - 1) * 2
    for r in range(len(tree_grid)):
        for c in range(len(tree_grid[0])):
            if r != 0 and r != len(tree_grid) - 1 and c != 0 and c != len(tree_grid[0]) - 1:
                if check_visible(tree_grid, r, c):
                    num_visible += 1
    return num_visible


def check_visible(tree_grid, r, c):
    height = tree_grid[r][c]
    sides_invisible = 0
    # check left
    for i in tree_grid[r][:c]:
        if i >= height:
            sides_invisible += 1
            break
    # check right
    for i in tree_grid[r][c+1:]:
        if i >= height:
            sides_invisible += 1
            break
    # check up
    for i in range(r):
        if tree_grid[i][c] >= height:
            sides_invisible += 1
            break
    # check down
    for i in range(r+1, len(tree_grid)):
        if tree_grid[i][c] >= height:
            sides_invisible += 1
            break
    return sides_invisible != 4


if __name__ == "__main__":
    main()
