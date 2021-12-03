from main import part_2

def test_part_2():
    input_ = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 5
    assert part_2(input_) == expected

test_part_2()
