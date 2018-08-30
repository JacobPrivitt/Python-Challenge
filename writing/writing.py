
class Filer():

    def openFile(self):
        with open('system_config.txt') as file_object:
            contents = file_object.read()
            print(contents)

    def openFile2(self,file):
        try:
            with open(file) as file_object:
                contents = file_object.read()
                print("Reading file ...:" + contents)
        except FileNotFoundError:
                print("\nERROR: We had trouble reading the file.")
        else:
                print("\nWe were able to access the file. Cool!")


    def writeFile(self, textfilename, textToInsert):
      try:
            with open(textfilename, 'w') as file_object:
                file_object.write(textToInsert)
                
      except FileNotFoundError:
                print("\nERROR: We had trouble writing to the file.")
      else:
                print("\nFile written to. This is what we wrote: " + textToInsert)


    def addtoFile(self, textfilename, textToInsert):
      try:
            with open(textfilename, 'a') as file_object:
                file_object.write(textToInsert)
                
      except FileNotFoundError:
                print("\nERROR: We had trouble writing to the file.")
      else:
                print("\nFile written to. This is what we wrote: " + textToInsert)




myWriter = Filer()
myWriter.writeFile('myfile.txt','Big kitty cats!')
myWriter.openFile2('myfile.txt')
myWriter.addtoFile('myfile.txt','... Love big fish!')
myWriter.openFile2('myfile.txt')
