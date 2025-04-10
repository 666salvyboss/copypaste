from pathlib import Path
class CopyPaste:
    """A class TO SIMULATE THE CLIB BOARD FUNCTIONS AT THE CLI LEVEL"""
    def __init__(self):
        """CONSTRUCTOR TO DEFINE TEMPORARY VARIABLE FOR FUNCTION VARIABLES"""
        self.file = Path('copied_data.txt')
        self.show = None
        self.old_pin = None
        self.new_pin = None
        self.target = None

        # Ensure file exists
        if not self.file.exists():
            self.file.write_text('')  # create the file if it doesn't exist

    def copy(self, target):
        self.target = target
        try:
            f = open(self.file, 'r+')
            content = f.readlines()
            if not content:
                content = ['\n']  # placeholder for empty file

            content[0] = str(target) + '\n'  # always overwrite first line
            f.seek(0)
            f.writelines(content)
            f.truncate()
            f.close()
            print("copy successful")
        except Exception as e:
            return f"{e} - error occurred in copy"

    @staticmethod
    def paste():
        """RETURNS CONTENT FROM FILE"""
        path = Path('copied_data.txt')
        if not path.exists():
            return "copied_data.txt does not exist"
        try:
            return path.read_text()
        except Exception as e:
            return f"{e} - error occurred in paste"

    def __str__(self):
        return str(self.target)  # force string

    def pin(self, target):
        self.target = target
        with open(self.file, 'a') as f:
            f.write(str(self.target) + '\n')  # always ends with newline
        print("Pin successful")

    def unpin(self, old_pin):
        """A FUNCTION TO SIMPLY REMOVE SPECIFIC PINS"""
        self.old_pin = old_pin
        #path = Path('copied_data.txt')
        if not self.file.exists():
            return "File does not exist"
        f = self.file.open('r')
        content = f.readlines()
        f.close()
        content = [line for line in content if line.strip() != str(self.old_pin)]
        f = self.file.open('w')
        f.writelines(content)
        f.truncate()
        f.close()

    def show_pin(self, show):
        """A FUNCTION THAT REVEALS SPECIFICALLY PINNED ITEMS"""
        self.show = show
        f = open(self.file, 'r')
        content = f.readlines()
        content = [line.strip() for line in content if self.show in line]
        f.close()
        return content

if __name__ == '__main__':
    r = CopyPaste()
    r.copy('Test 1')
    print(r.paste())
    r.copy('Test 2')
    r.pin('Pin 1')
    r.unpin('Pin 1')
    r.pin('Pin 2')
    print(r.show_pin('Pin 2'))
