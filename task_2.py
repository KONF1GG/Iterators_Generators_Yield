
import types

def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flat_gen = flat_generator(list_of_lists_1)

    for flat_gen_item, check_item in zip(flat_gen, ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_gen_item == check_item

    assert list(flat_gen) == []

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()
