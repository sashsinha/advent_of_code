"""Advent of Code 2024, Day 2 Solution.

Usage:
  (advent_of_code) $ uv run -m 2024.day_02
"""

import utils


def are_levels_safe(levels: list[int]) -> bool:
  is_safe = True
  is_decreasing = False
  is_increasing = False
  for a, b in zip(levels[1:], levels[:-1]):
    if a < b:
      if is_decreasing:
        is_safe = False
        break
      is_increasing = True
    elif a > b:
      if is_increasing:
        is_safe = False
        break
      is_decreasing = True
    else:
      is_safe = False
      break
    if abs(a - b) > 3:
      is_safe = False
      break
  return is_safe


def part_1(data: list[str]) -> int:
  safe = 0
  for report in data:
    levels = list(map(int, report.split()))
    if are_levels_safe(levels):
      safe += 1
  return safe


def part_2(data: list[str]) -> int:
  safe = 0
  for report in data:
    levels = list(map(int, report.split()))
    if are_levels_safe(levels):
      safe += 1
    else:
      for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1 :]
        if are_levels_safe(new_levels):
          safe += 1
          break
  return safe


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_lines('2024/day_02_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_lines('2024/day_02.txt')
  print(f'Part 1 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_lines('2024/day_02_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_lines('2024/day_02.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=2, year=2024)
  utils.download_data(day=2, year=2024)
  main()
