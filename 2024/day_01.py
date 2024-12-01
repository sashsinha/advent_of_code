"""Advent of Code 2024, Day 1 Solution.

Usage:
  (advent_of_code) $ uv run -m 2024.day_01
"""

from collections import Counter

import utils


def part_1(data: list[str]) -> int:
  a, b = [], []
  for line in data:
    x, y = map(int, line.strip().split())
    a.append(x)
    b.append(y)
  return sum(abs(x - y) for x, y in zip(sorted(a), sorted(b)))


def part_2(data: list[str]) -> int:
  a, b = [], []
  for line in data:
    x, y = map(int, line.strip().split())
    a.append(x)
    b.append(y)
  b_counts = Counter(b)
  return sum(x * b_counts[x] for x in a)


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_lines('2024/day_01_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_lines('2024/day_01.txt')
  print(f'Part 2 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_lines('2024/day_01_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_lines('2024/day_01.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=1, year=2024)
  utils.download_data(day=1, year=2024)
  main()
