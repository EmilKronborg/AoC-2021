from main import part_1

def test_part_1():
    input_ = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 7
    assert part_1(input_) == expected

test_part_1()
