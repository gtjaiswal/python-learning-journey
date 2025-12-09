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

# file_manager = FileManager("/Users/garimajaiswal/Learning/Python/python-learning-journey/basics/data/day1_task_word_frequency_input.txt")
# print(file_manager.write("ABS"))
