import unittest
from image_processing.filters import apply_blur

class TestFilters(unittest.TestCase):
    def test_apply_blur(self):
        result = apply_blur('test_image.jpg', 'blurred_image.jpg')
        self.assertTrue(result.endswith('blurred_image.jpg'))

if __name__ == '__main__':
    unittest.main()
