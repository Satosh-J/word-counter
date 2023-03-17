import unittest
from word_count import count_words, find_most_common_word

#! Answer for Q4
class TestCountWords(unittest.TestCase):


    def test_count_words_with_string_input(self):
        input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        expected_output = {'lorem': 1, 'ipsum': 1, 'dolor': 1, 'sit': 1, 'amet': 1, 'consectetur': 1, 'adipiscing': 1, 'elit': 1}
        self.assertEqual(count_words(input_text), expected_output)

    def test_count_words_with_filepath(self):
        # create a sample file for testing
        with open('test_sample.txt', 'w') as file:
            file.write('Quis istum dolorem timet? \Quis dolorem dolorem?')

        # test the count_words function
        result = count_words('test_sample.txt')
        expected = {'quis': 2, 'istum': 1, 'dolorem': 3, 'timet': 1}
        self.assertEqual(result, expected)

        # delete the sample file after testing
        import os
        os.remove('test_sample.txt')

    def test_null_input(self):
        self.assertEqual(count_words(None), {})

    def test_empty_input(self):
        self.assertEqual(count_words(""), {})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_words(123)

    def test_max_common(self):
        input = {'tenueris': 3, 'est': 2, 'a': 2, 'ipsum': 2, 'bona': 1}
        expected = ('tenueris', 3)
        result = find_most_common_word(input)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
