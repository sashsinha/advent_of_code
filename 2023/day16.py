import collections
import dataclasses
import utils


@dataclasses.dataclass(frozen=True)
class Entry:
    y: int
    x: int
    d_y: int
    d_x: int


def get_energized(grid: list[list[int]], rows: int, cols: int, start_cell: Entry) -> int:
    queue = collections.deque([start_cell])
    seen = set()
    while queue:
        y, x, d_y, d_x = dataclasses.astuple(queue.pop())
        y += d_y
        x += d_x
        if y < 0 or y >= rows or x < 0 or x >= cols:
            continue
        ch = grid[y][x]
        if ch == '.' or (ch == '-' and d_y == 0) or (ch == '|' and d_x == 0):
            entry = Entry(y, x, d_y, d_x)
            if entry not in seen:
                seen.add(entry)
                queue.appendleft(entry)
        elif ch == "/":
            # if d_y == 0 and d_x == 1:  # right
            #     d_y, d_x = -1, 0  # up
            # elif d_y == 0 and d_x == -1:  # left
            #     d_y, d_x = 1, 0  # down
            # elif d_y == -1 and d_x == 0:  # up
            #     d_y, d_x = 0, 1  # right
            # elif d_y == 1 and d_x == 0:  # down
            #     d_y, d_x = 0, -1  # left
            d_y, d_x = -d_x, -d_y
            entry = Entry(y, x, d_y, d_x)
            if entry not in seen:
                seen.add(entry)
                queue.appendleft(entry)
        elif ch == '\\':
            # if d_y == 0 and d_x == 1:  # right
            #     d_y, d_x = 1, 0  # down
            # elif d_y == 0 and d_x == -1:  # left
            #     d_y, d_x = -1, 0  # up
            # elif d_y == -1 and d_x == 0:  # up
            #     d_y, d_x = 0, -1  # left
            # elif d_y == 1 and d_x == 0:  # down
            #     d_y, d_x = 0, 1  # right
            d_y, d_x = d_x, d_y
            entry = Entry(y, x, d_y, d_x)
            if entry not in seen:
                seen.add(entry)
                queue.appendleft(entry)
        elif ch == '-' and d_y != 0:
            for entry in [Entry(y, x, 0, 1), Entry(y, x, 0, -1)]:
                if entry not in seen:
                    seen.add(entry)
                    queue.appendleft(entry)
        elif ch == '|' and d_x != 0:
            for entry in [Entry(y, x, 1, 0), Entry(y, x, -1, 0)]:
                if entry not in seen:
                    seen.add(entry)
                    queue.appendleft(entry)
    return len({(e.y, e.x) for e in seen})


def part_1(data: list[str]) -> int:
    grid = [list(line.strip()) for line in data]
    rows, cols = len(grid), len(grid[0])
    return get_energized(grid, rows, cols, Entry(y=0, x=-1, d_y=0, d_x=1))


def part_2(data: list[str]) -> int:
    grid = [list(line.strip()) for line in data]
    rows, cols = len(grid), len(grid[0])
    left_edge_starts = [Entry(y=r, x=-1, d_y=0, d_x=1) for r in range(rows)]
    top_edge_starts = [Entry(y=-1, x=c, d_y=1, d_x=0) for c in range(cols)]
    right_edge_starts = [Entry(y=r, x=cols, d_y=0, d_x=-1) for r in range(rows)]
    bottom_edge_starts = [Entry(y=rows, x=c, d_y=-1, d_x=0) for c in range(cols)]
    all_edge_starts = left_edge_starts + top_edge_starts + right_edge_starts + bottom_edge_starts
    return max(get_energized(grid, rows, cols, e) for e in all_edge_starts)


def main() -> None:
    data = utils.read_data_as_lines('day16.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=16, year=2023)
    main()
