import os.path
from os import path

def main():

    dir_name = input("Enter the name directory in which they want to save a file: ")

    if os.path.exists(dir_name):
        print("Directory exists:" + str(path.exists('hi.txt')))

    else:
        os.mkdir(dir_name)

        file_name = input('Enter the name of file that you want to save in the directory: ')
        f = open(dir_name + '/' + file_name, 'w')
        name, address, phone = input('Enter Name, Address, and Phone number separated by comma: ').split(',')
        n = f.write('name.strip()' + ',' + 'address.strip()' + ',' + 'phone.strip()')
        # f = open('dir_name' + '/' + 'file_name', 'r')
        # data = f.read().split(',')
        # print(f)
        print('Output of files: ')
        print('Name: ', name)
        print('Address: ', address)
        print('Phone: ', phone)
        f.close()


if __name__== "__main__":
    main()

