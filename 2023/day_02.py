"""Advent of Code 2023, Day 2 Solution.

Usage:
  (advent_of_code) $ uv run -m 2023.day_02
"""

import utils


def part_1(data: list[str]) -> int:
  possible_game_ids = 0
  for g, game_info in enumerate(data, start=1):
    unused_game_id, cube_sets = game_info.split(': ')
    is_possible = True
    for cube_set in cube_sets.split('; '):
      cubes = cube_set.split(', ')
      for cube in cubes:
        count, color = cube.split(' ')
        count = int(count)
        if color == 'red' and count > 12:
          is_possible = False
          break
        elif color == 'green' and count > 13:
          is_possible = False
          break
        elif color == 'blue' and count > 14:
          is_possible = False
          break
    if is_possible:
      possible_game_ids += g
  return possible_game_ids


def part_2(data: list[str]) -> int:
  total_power = 0
  for game_info in data:
    unused_game_id, cube_sets = game_info.split(': ')
    max_red = 0
    max_green = 0
    max_blue = 0
    for cube_set in cube_sets.split('; '):
      cubes = cube_set.split(', ')
      for cube in cubes:
        count, color = cube.split(' ')
        count = int(count)
        if color == 'red':
          max_red = max(max_red, count)
        elif color == 'green':
          max_green = max(max_green, count)
        elif color == 'blue':
          max_blue = max(max_blue, count)
    total_power += max_red * max_green * max_blue
  return total_power


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_lines('2023/day_02_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_lines('2023/day_02.txt')
  print(f'Part 1 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_lines('2023/day_02_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_lines('2023/day_02.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=2, year=2023)
  utils.download_data(day=2, year=2023)
  main()
