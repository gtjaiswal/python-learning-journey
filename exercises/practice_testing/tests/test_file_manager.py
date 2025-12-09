import unittest
# from file_manager import FileManager  # Not needed - FileManager is defined below

#
# class MyTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.file_manager = FileManager("/Users/garimajaiswal/Learning/Python/python-learning-journey/basics/data/day1_task_word_frequency_input.txt")
#
#     def test_write(self):
#         self.assertEqual(self.file_manager.write("ABC"),self.file_manager.read())
#         self.assertEqual(self.file_manager.write(""), None)
#

import unittest
import os


class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def write(self, content):
        with open(self.filename, 'w') as f:
            f.write(content)

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()


class TestFileManager(unittest.TestCase):

    def setUp(self):
        """
        Runs before EACH test method.
        Creates a test file that will be used by FileManager.
        """
        self.test_filename = "test_file.txt"
        self.file_manager = FileManager(self.test_filename)
        # Note: We don't create the file here, FileManager.write() will create it
        # But we could pre-create it if needed: open(self.test_filename, 'w').close()

    def tearDown(self):
        """
        Runs after EACH test method, even if the test fails.
        Ensures cleanup happens no matter what.
        """
        # Check if file exists before trying to delete
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_write_creates_file_with_content(self):
        """Test that write() creates file and stores content."""
        content = "Hello, World!"
        self.file_manager.write(content)

        # Verify file was created
        self.assertTrue(os.path.exists(self.test_filename))

        # Verify content was written
        with open(self.test_filename, 'r') as f:
            actual_content = f.read()
        self.assertEqual(actual_content, content)

    def test_read_returns_file_content(self):
        """Test that read() returns the correct content."""
        content = "Test content"
        self.file_manager.write(content)

        result = self.file_manager.read()
        self.assertEqual(result, content)

    def test_write_overwrites_existing_content(self):
        """Test that write() overwrites previous content."""
        self.file_manager.write("First content")
        self.file_manager.write("Second content")

        result = self.file_manager.read()
        self.assertEqual(result, "Second content")

    def test_read_empty_file(self):
        """Test reading an empty file."""
        self.file_manager.write("")

        result = self.file_manager.read()
        self.assertEqual(result, "")

    def test_cleanup_happens_even_if_test_fails(self):
        """
        Test that demonstrates tearDown runs even if test fails.
        This test will fail intentionally, but file should still be deleted.
        Comment out the assertion to see tearDown working.
        """
        self.file_manager.write("Some content")

        # This assertion will fail, but tearDown should still run
        # Uncomment to see the failure:
        # self.assertEqual(1, 2, "Intentional failure")

        # For demo purposes, we'll pass this test
        self.assertTrue(os.path.exists(self.test_filename))


if __name__ == '__main__':
    unittest.main()
