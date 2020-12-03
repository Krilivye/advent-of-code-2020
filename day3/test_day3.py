def test_make_a_map():
    # Arrange:
    filename = "example_map.txt"

    # Act
    map_of_the_land = make_a_map(filename)

    # Assert
    str(
        map
    ) == """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
