"""Advent of Code 2017, Day 1 Solution.

Usage:
  (advent_of_code) $ uv run -m 2017.day_01
"""

import utils


def part_1(data: str) -> int:
  data = data + data[0]
  total = 0
  for a, b in zip(data[:-1], data[1:]):
    if a == b:
      total += int(a)
  return total


def part_2(data: list[str]) -> int:
  n = len(data)
  look_ahead = n // 2
  data = data + data
  total = 0
  for i in range(n):
    a = data[i]
    b = data[i + look_ahead]
    if a == b:
      total += int(a)
  return total


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_line('2017/day_01_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_line('2017/day_01.txt')
  print(f'Part 1 Actual Answer: {part_1(data)}')
  # # Part 2
  example_2_data = utils.read_data_as_line('2017/day_01_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_line('2017/day_01.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=1, year=2017)
  utils.download_data(day=1, year=2017)
  main()
