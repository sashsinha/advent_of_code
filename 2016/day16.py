import utils


def dragon_curve_step(s: str) -> str:
    a = s
    b = a
    b = ''.join(reversed(b))
    mapping_table = str.maketrans("01", "10")
    b = b.translate(mapping_table)
    return f'{a}0{b}'


def checksum_step(s: str) -> str:
    new_checksum = []
    for a, b in zip(s[0::2], s[1::2]):
        if a == b:
            new_checksum.append('1')
        else:
            new_checksum.append('0')
    return ''.join(new_checksum)


def part_1(data: str) -> str:
    disk_size = 272
    while len(data) < disk_size:
        data = dragon_curve_step(data)
    checksum = checksum_step(data[:disk_size])
    while len(checksum) % 2 != 1:
        checksum = checksum_step(checksum)
    return checksum


def part_2(data: str) -> str:
    disk_size = 35651584
    while len(data) < disk_size:
        data = dragon_curve_step(data)
    checksum = checksum_step(data[:disk_size])
    while len(checksum) % 2 != 1:
        checksum = checksum_step(checksum)
    return checksum


def main() -> None:
    data = utils.read_data_as_line('day16.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=16, year=2016)
    main()
