import file_tools as ft

if __name__ == '__main__':

    ft.write_file("./data/test.txt", "国庆复习\n")
    ft.write_file("./data/test.txt", "Python文件操作\n")
    ft.read_file("./data/test.txt")