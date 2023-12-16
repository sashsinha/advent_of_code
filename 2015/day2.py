import utils


def get_wrapping_paper(l: int, w: int, h: int) -> int:
    smallest_side, second_smallest_side = sorted([l, w, h])[:2]
    return 2 * l * w + 2 * w * h + 2 * h * l + smallest_side * second_smallest_side


def part_1(data: list[str]) -> int:
    total_wrapping_paper = 0
    for line in data:
        l, w, h = utils.ints_from_line(line, 'x')
        total_wrapping_paper += get_wrapping_paper(l, w, h)
    return total_wrapping_paper


def get_ribbon(l: int, w: int, h: int) -> int:
    smallest_side, second_smallest_side = sorted([l, w, h])[:2]
    smallest_perimeter = 2 * smallest_side + 2 * second_smallest_side
    return smallest_perimeter + l * w * h


def part_2(data: list[str]) -> int:
    total_ribbon = 0
    for line in data:
        l, w, h = utils.ints_from_line(line, 'x')
        total_ribbon += get_ribbon(l, w, h)
    return total_ribbon


def main() -> None:
    data = utils.read_data_as_lines('day2.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=2, year=2015)
    main()
