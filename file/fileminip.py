class Filer():

    def openFile(self):
        with open('system_config.txt') as file_object:
            contents = file_object.read()
            print(contents)

    def openFile2(self, file):
        try:
            with open(file) as file_object:
                contents = file_object.read()
                print(contents)
        except FileNotFoundError:
            print("\nERROR: We couldn't read the file.")
        else:
            print("\nWe got the file.")
my_file = Filer()
my_file.openFile2('people.txt')
