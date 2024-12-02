"""Advent of Code 2022, Day 1 Solution.

Usage:
  (advent_of_code) $ uv run -m 2022.day_01
"""

import heapq

import utils


def part_1(data: str) -> int:
  elf_backpacks = [
    utils.ints_from_line(line, '\n') for line in data.split('\n\n')
  ]
  elf_totals = [sum(elf_backpack) for elf_backpack in elf_backpacks]
  return max(elf_totals)


def part_2(data: str) -> int:
  elf_backpacks = [
    utils.ints_from_line(line, '\n') for line in data.split('\n\n')
  ]
  elf_totals = [sum(elf_backpack) for elf_backpack in elf_backpacks]
  top3_totals = heapq.nlargest(3, elf_totals)
  return sum(top3_totals)


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_line('2022/day_01_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_line('2022/day_01.txt')
  print(f'Part 1 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_line('2022/day_01_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_line('2022/day_01.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=1, year=2022)
  utils.download_data(day=1, year=2022)
  main()
