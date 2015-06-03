#!/usr/local/bin/python
import random
import string
NUM = 10
def matrixMul(A, B):
    return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]

def autoGen(f_DM, f_A, f_B):
    length = NUM * NUM / 4
    for i in range(0, length):
        i0 = random.randint(0,50)
        i1 = random.randint(0,50)
        i2 = random.randint(0,50)
        i3 = random.randint(0,50)
        r0 = format(hex(i0).lstrip("0").strip("x"),"0>8")
        r1 = format(hex(i1).lstrip("0").strip("x"),"0>8")
        r2 = format(hex(i2).lstrip("0").strip("x"),"0>8")
        r3 = format(hex(i3).lstrip("0").strip("x"),"0>8")
        f_A.write('%d'% i0+ "\n")
        f_A.write('%d'% i1+ "\n")
        f_A.write('%d'% i2+ "\n")
        f_A.write('%d'% i3+ "\n")
        f_DM.write("32'h"+hex(i).lstrip("0").strip("x")+"0, 128'h"+r3+"_"+r2+"_"+r1+"_"+r0+"\n")
    
    for i in range(0, length):
        i0 = random.randint(0,50)
        i1 = random.randint(0,50)
        i2 = random.randint(0,50)
        i3 = random.randint(0,50)
        r0 = format(hex(i0).lstrip("0").strip("x"),"0>8")
        r1 = format(hex(i1).lstrip("0").strip("x"),"0>8")
        r2 = format(hex(i2).lstrip("0").strip("x"),"0>8")
        r3 = format(hex(i3).lstrip("0").strip("x"),"0>8")
        f_B.write('%d'% i0+ "\n")
        f_B.write('%d'% i1+ "\n")
        f_B.write('%d'% i2+ "\n")
        f_B.write('%d'% i3+ "\n")
        f_DM.write("32'h1"+format(hex(i).lstrip("0").strip("x"),"0>3")+"0, 128'h"+r3+"_"+r2+"_"+r1+"_"+r0+"\n")

def initMatrix(f_A, A):
    tmp = []
    i = 0
    count = 0
    for line in f_A:
        tmp.append(string.atoi(line.strip('\n')))
        i += 1
        count = count + 1
        if i == NUM:
            A.append(tmp)
            i = 0
            tmp = []
    if count != NUM * NUM:
        print("Error in function \"initMatrix\" [count=%d]" % count)

def writeMatrixC(f_C, C):
    for i in range(0, NUM):
        for j in range(0, NUM):
            f_C.write('%d' % C[i][j] + '\n')

def authentication(A):
    if len(A) == NUM:
        for i in range(0, NUM):
            if len(A[i]) != NUM:
                print("Error in function \"authentication\"")
    else:
        print("Error in function \"authentication\"")

def main():
    f_DM=open("DM.dat","w")
    f_A = open("A.txt","w")
    f_B = open("B.txt","w")
    autoGen(f_DM, f_A, f_B)
    f_DM.close()
    f_A.close()
    f_B.close()

    f_A = open("A.txt","r")
    f_B = open("B.txt","r")
    f_C = open("C.txt","w")
    A = []
    B = []
    C = []
    initMatrix(f_B, B)
    initMatrix(f_A, A)
    authentication(A)
    authentication(B)
    C = matrixMul(A, B)
    authentication(C)
    writeMatrixC(f_C, C)
    f_A.close()
    f_B.close()
    f_C.close()

if __name__ == "__main__":
    main()
