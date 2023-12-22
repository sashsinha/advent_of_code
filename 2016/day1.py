import utils


def part_1(data: str) -> int:
    curr_pos = (0, 0)
    curr_dir = utils.Direction.NORTH
    for move in data.split(', '):
        d, steps = move[0], int(move[1:])
        if d == 'R':
            curr_dir = utils.Direction(utils.rotate_right(curr_dir.value))
        elif d == 'L':
            curr_dir = utils.Direction(utils.rotate_left(curr_dir.value))
        curr_pos = utils.move(curr_pos, curr_dir, steps)
    return utils.manhattan_distance((0, 0), curr_pos)


def part_2(data: str) -> int:
    curr_pos = (0, 0)
    seen_pos = {curr_pos}
    curr_dir = utils.Direction.NORTH
    for move in data.split(', '):
        d, steps = move[0], int(move[1:])
        if d == 'R':
            curr_dir = utils.Direction(utils.rotate_right(curr_dir.value))
        elif d == 'L':
            curr_dir = utils.Direction(utils.rotate_left(curr_dir.value))
        for _ in range(steps):
            curr_pos = utils.move(curr_pos, curr_dir, 1)
            if curr_pos in seen_pos:
                return utils.manhattan_distance((0, 0), curr_pos)
            seen_pos.add(curr_pos)
    return -1


def main() -> None:
    data = utils.read_data_as_line('day1.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=1, year=2016)
    main()
