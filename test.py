import unittest
from word_count import count_words, find_most_common_word

#! Answer for Q4
class TestCountWords(unittest.TestCase):

    def test_count_words_with_filepath(self):
        # create a sample file for testing
        with open('test_sample.txt', 'w') as file:
            file.write('this is a test\nthis is only a test\n')

        # test the count_words function
        result = count_words('test_sample.txt')
        expected = {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
        self.assertEqual(result, expected)

        # delete the sample file after testing
        import os
        os.remove('test_sample.txt')

    def test_max_common(self):

        input = {'this': 3, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
        expected = ('this', 3)
        result = find_most_common_word(input)
        self.assertEqual(result, expected)

    def test_null_input(self):
        self.assertEqual(count_words(None), {})

    def test_empty_input(self):
        self.assertEqual(count_words(""), {})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_words(123)

    def test_valid_input(self):
        input_text = "This is a sample sentence. It contains words."
        expected_output = {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'sentence': 1, 'it': 1, 'contains': 1, 'words': 1}
        self.assertEqual(count_words(input_text), expected_output)



if __name__ == '__main__':
    unittest.main()
