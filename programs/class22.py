


class TextFile:
    def read(self):
        print("Reading from a text file...")

class ImageFile:
    def read(self):
        print("Reading from an image file...")

# Function using Duck Typing
def read_file(file_object):
    file_object.read()

# Create file objects
text = TextFile()
image = ImageFile()

# Read files
read_file(text)
read_file(image)
