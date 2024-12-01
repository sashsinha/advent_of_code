import enum
import math
import os

import aocd


def download_data(day: int, year: int) -> None:
  data_file_name = f'{year}/day_{day:0>2}.txt'
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
    return list(map(str.strip, input_file.readlines()))


def read_data_as_int_lines(file_name: str) -> list[int]:
  with open(file_name) as input_file:
    return list(map(int, input_file.readlines()))


def ints_from_line(line: str, delimiter: str) -> list[int]:
  return list(map(int, line.split(delimiter)))


def read_lines_as_dict(lines: list[str]) -> dict[str, int]:
  d = {}
  for line in lines:
    k, v = line.split(':')
    d[k.strip()] = int(v)
  return d


def read_lines_as_grid(lines: list[str]) -> tuple[list[list[int]], int, int]:
  grid = [[int(ch) for ch in line.strip()] for line in lines]
  return grid, len(grid), len(grid[0])


class Direction(enum.Enum):
  NORTH = (0, -1)
  NORTHEAST = (1, -1)
  EAST = (1, 0)
  SOUTHEAST = (1, 1)
  SOUTH = (0, 1)
  SOUTHWEST = (-1, 1)
  WEST = (-1, 0)
  NORTHWEST = (-1, -1)


def rotate_left(direction: tuple[int, int]) -> tuple[int, int]:
  dx, dy = direction
  return -dy, dx


def rotate_right(direction: tuple[int, int]) -> tuple[int, int]:
  dx, dy = direction
  return dy, -dx


def move(
  position: tuple[int, int], direction: Direction, steps: int = 1
) -> tuple[int, int]:
  x, y = position
  dx, dy = direction.value
  return x + dx * steps, y + dy * steps


def manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
  x1, y1 = point1
  x2, y2 = point2
  return abs(x1 - x2) + abs(y1 - y2)


def euclidean_distance(
  point1: tuple[int, int], point2: tuple[int, int]
) -> float:
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
