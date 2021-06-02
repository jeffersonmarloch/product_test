from pathlib import Path
import io



class File:
    @staticmethod
    def create(name_file):
        if not Path(name_file).exists():
            Path(name_file)


    @staticmethod
    def count_line(name_file):
        try:
            file = open(name_file, 'r')
            quantity_line = len(file.readlines())
            file.close()

            return quantity_line
        except FileNotFoundError:
            return 0


    @staticmethod
    def write(name_file, line):
        '''
        >>> name = "test"
        >>> write(name)
        '''

        quantity_actualy_line = File.count_line(name_file)
        file = open(name_file, 'a')
        try:
            file.write(str(quantity_actualy_line) + ', ' + line + '\n')

            return file 

        except io.UnsupportedOperation:
            file.write("0, " + line + '\n')

            return file 

        finally:
            file.close()



    @staticmethod
    def read(name_file):
        '''
        >>> name = "test"
        >>> write(name, "test")
        >>> read(name)
        test
        '''
        file = Path(name_file)
        return file.read_text()

    
    @staticmethod
    def delete():
        return 0    