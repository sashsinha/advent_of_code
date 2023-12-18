import heapq
import typing
import utils


class Entry(typing.NamedTuple):
    heat_loss: int
    row: int
    col: int
    d_y: int
    d_x: int
    same_direction: int


def part_1(data: list[str]) -> int:
    grid, rows, cols = utils.read_lines_as_grid(data)
    seen = set()
    pq = [Entry(heat_loss=0, row=0, col=0, d_y=0, d_x=0, same_direction=0)]
    while pq:
        heat_loss, row, col, d_y, d_x, same_direction = heapq.heappop(pq)
        if row == rows - 1 and col == cols - 1:
            return heat_loss
        if (row, col, d_y, d_x, same_direction) in seen:
            continue
        seen.add((row, col, d_y, d_x, same_direction))
        if same_direction < 3 and (d_y, d_x) != (0, 0):
            new_row = row + d_y
            new_col = col + d_x
            if 0 <= new_row < rows and 0 <= new_col < cols:
                heapq.heappush(pq, Entry(heat_loss + grid[new_row][new_col], new_row, new_col, d_y, d_x,
                                         same_direction + 1))
        for new_d_y, new_d_x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (new_d_y, new_d_x) != (d_y, d_x) and (new_d_y, new_d_x) != (-d_y, -d_x):
                new_row = row + new_d_y
                new_col = col + new_d_x
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    heapq.heappush(pq, Entry(heat_loss + grid[new_row][new_col], new_row, new_col, new_d_y, new_d_x, 1))


def part_2(data: list[str]) -> int:
    grid, rows, cols = utils.read_lines_as_grid(data)
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]
    while pq:
        heat_loss, row, col, d_y, d_x, same_direction = heapq.heappop(pq)
        if row == rows - 1 and col == cols - 1 and same_direction >= 4:
            return heat_loss
        if (row, col, d_y, d_x, same_direction) in seen:
            continue
        seen.add((row, col, d_y, d_x, same_direction))
        if same_direction < 10 and (d_y, d_x) != (0, 0):
            new_row = row + d_y
            new_col = col + d_x
            if 0 <= new_row < rows and 0 <= new_col < cols:
                heapq.heappush(pq, Entry(heat_loss + grid[new_row][new_col], new_row, new_col, d_y, d_x,
                                         same_direction + 1))
        if same_direction >= 4 or (d_y, d_x) == (0, 0):
            for new_d_y, new_d_x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (new_d_y, new_d_x) != (d_y, d_x) and (new_d_y, new_d_x) != (-d_y, -d_x):
                    new_row = row + new_d_y
                    new_col = col + new_d_x
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        heapq.heappush(pq,
                                       Entry(heat_loss + grid[new_row][new_col], new_row, new_col, new_d_y, new_d_x, 1))


def main() -> None:
    data = utils.read_data_as_lines('day17.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=17, year=2023)
    main()
