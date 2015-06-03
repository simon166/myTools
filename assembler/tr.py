import binascii
import sys
import os

sourceFile = sys.argv[1]#raw_input("Input assembly source file name: ")
#sourceFile = raw_input("Input assembly source file name: ")
if os.path.isfile(sourceFile) == False:
    print(sourceFile + " doesn't exist!")
    os._exit(0)

if os.path.isfile("as-new") == False:
    print(sourceFile + " doesn't exist!")
    os._exit(0)

if os.path.isfile("ld-new") == False:
    print(sourceFile + " doesn't exist!")
    os._exit(0)

if os.path.isfile("objcopy") == False:
    print(sourceFile + " doesn't exist!")
    os._exit(0)

objectFile = sourceFile[:-2] + ".o"
outFile = sourceFile[:-2] + ".out"
datFileSim = sourceFile[:-2]
datFileRtl = sourceFile[:-2] + ".dat"
os.system("./as-new " + sourceFile + " -g --gdwarf-2 -o " + objectFile)
os.system("./ld-new " + objectFile + " -o " + outFile)
os.system("./objcopy -O binary "+ outFile + " " + datFileSim)
if os.path.isfile(datFileSim) == False:
    print "Doesn't create "+datFileSim
    os._exit(0)
fb_s = open(datFileSim,'rb')
fb_d = open(datFileRtl,'w')


for i in range(0,65535):
    insnPack = fb_s.read(16)
    if(len(insnPack) != 16):
        break
    insnPack = binascii.b2a_hex(insnPack)
    insn0 = insnPack[0:8]
    insn1 = insnPack[8:16]
    insn2 = insnPack[16:24]
    insn3 = insnPack[24:32]
    insn0 = insn0[6:8]+insn0[4:6]+insn0[2:4]+insn0[0:2] + '_'
    insn1 = insn1[6:8]+insn1[4:6]+insn1[2:4]+insn1[0:2] + '_'
    insn2 = insn2[6:8]+insn2[4:6]+insn2[2:4]+insn2[0:2] + '_'
    insn3 = insn3[6:8]+insn3[4:6]+insn3[2:4]+insn3[0:2] + '\n'
    addr =  '{0:0>4}'.format(hex(i).replace("0x",''))
    #i#fb_d.write(addr + '\n')
    fb_d.write("32'h001" + addr + '0,\t' + "128'h" + insn0 + insn1 + insn2 + insn3)
   
#insn = fb_s.read(4)
#insnString = binascii.b2a_hex(insn)
#print insnString[6:8]+insnString[4:6]+insnString[2:4]+insnString[0:2]

#insn = fb_s.read(4)
#insnString = binascii.b2a_hex(insn)
#print insnString[6:8]+insnString[4:6]+insnString[2:4]+insnString[0:2]


fb_s.close()
fb_d.close()
