import aocd
import os


def download_data(day: int, year: int) -> None:
    data_file_name = f'{year}/day{day}.txt'
    owd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    if not os.path.isfile(data_file_name):
        with open(data_file_name, 'w') as data_input_file:
            data_input_file.write(aocd.get_data(day=day, year=year))
    os.chdir(owd)


def read_data_as_line(file_name: str) -> str:
    with open(file_name) as input_file:
        return input_file.read()


def read_data_as_lines(file_name: str) -> list[str]:
    with open(file_name) as input_file:
        return input_file.readlines()


def ints_from_line(line: str, delimiter: str) -> list[int]:
    return list(map(int, line.split(delimiter)))
