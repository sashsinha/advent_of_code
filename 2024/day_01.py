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
  data = utils.read_data_as_lines('2024/day_01.txt')
  print(part_1(data))
  print(part_2(data))


if __name__ == '__main__':
  utils.download_data(day=1, year=2024)
  main()
