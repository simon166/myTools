#!/usr/local/bin/python
import random
import string
import os
def deleteDul(file_name, file_backup_name):
    f_source = open(file_name, 'r')
    f_backup = open(file_backup_name, 'w')
    tmp = ""
    for line in f_source:
        if line != tmp:
            f_backup.write("0x" + line[25:33] + "\n")
            f_backup.write("0x" + line[17:25] + "\n")
            tmp = line
    f_source.close()
    f_backup.close()

def matrixC2hex(file_name, file_hex_name):
    fd_source = open(file_name, 'r')
    fd_hex = open(file_hex_name, 'w')
    for line in fd_source:
        fd_hex.write("0x" + format(hex(string.atoi(line.strip("\n"))).lstrip("0x"),"0>8") + '\n')
    fd_source.close()
    fd_hex.close()

def autoCmp(file1, file2):
    if os.path.isfile(file1) == False:
        print(file1 + "dose not exist!")
        return
    if os.path.isfile(file2) == False:
        print(file2 + "dose not exist!")
        return
    fd_1 = open(file1, 'r')
    fd_2 = open(file2, 'r')
    line1 = fd_1.readline()
    line2 = fd_2.readline()
    cnt = 0
    while line1 or line2:
        cnt = cnt + 1
        if line1 != line2:
            print("%30s :" % "Error")
            print("%30s : line:%d :   %s" % (file1, cnt, line1.strip("\n")))
            print("%30s : line:%d :   %s" % (file2, cnt, line2.strip("\n")))
        line1 = fd_1.readline()
        line2 = fd_2.readline()
    fd_1.close()
    fd_2.close()

def main():
    result_file = "my_wbslv_trace.dat"
    if os.path.isfile(result_file) == False:
        print(result_file + "dose not exist!")
        return
    result_file_hex = result_file + ".hex"
    deleteDul(result_file, result_file_hex)
    matrixC = "C.txt"
    if os.path.isfile(matrixC) == False:
        print(matrixC + "dose not exist!")
        return
    matrixCHex = "C.hex"
    matrixC2hex(matrixC, matrixCHex)
    autoCmp(matrixCHex, result_file_hex)

if __name__ == "__main__":
    main()
