.global start                
_begin:
start:
.text
.ent main

.exptable:
jmp  exp_lable0|||         #bus error 0
nop|||
nop|||
nop|||

jmp  exp_lable1|||         #bus error 1        
nop|||
nop|||
nop|||

jmp  exp_lable2|||         #bus error 2
nop|||
nop|||
nop|||

jmp  exp_lable3|||         #bus error 3
nop|||
nop|||
nop|||

jmp  exp_lable4|||         #exception illegale instruction 
nop|||
nop|||
nop|||

jmp  exp_lable5|||         #exception overflow
nop|||
nop|||
nop|||

jmp  exp_lable6|||         # exception illegale address
nop|||
nop|||
nop|||

jmp  exp_lable7|||          # exception 3
nop|||
nop|||
nop|||

jmp  exp_lable8|||          #unavoided pic 0
nop|||
nop|||
nop|||

jmp  exp_lable9|||          #unavoided pic 1 (wathc dog)
nop|||
nop|||
nop|||

jmp  exp_lablea|||          #inner pic 2
nop|||
nop|||
nop|||

jmp  exp_lableb|||           #timer pic
nop|||
nop|||
nop|||

jmp  exp_lablec|||           # outer pic 4
nop|||
nop|||
nop|||

jmp  exp_labled|||          # outer pic 5
nop|||
nop|||
nop|||

exp_lable0:
movigl GR0 0|||
rtt|||
nop|||
nop|||

exp_lable1:
movigl GR0 1|||
rtt|||
nop|||
nop|||

exp_lable2:
movigl GR0 1|||
rtt|||
nop|||
nop|||

exp_lable3:
movigl GR0 3|||
rtt|||
nop|||
nop|||

exp_lable4:
movigl GR0 4|||
rtt|||
nop|||
nop|||

exp_lable5:
movigl GR0 5|||
rtt|||
nop|||
nop|||

exp_lable6:
movigl GR0 6|||
rtt|||
nop|||
nop|||

exp_lable7:
movigl GR0 7|||
rtt|||
nop|||
nop|||

exp_lable8:
movigl GR0 8|||
rtt|||
nop|||
nop|||

exp_lable9:
movigl GR0 9|||
rtt|||
nop|||
nop|||

exp_lablea:
movigl GR0 10|||
rtt|||
nop|||
nop|||

exp_lableb:
movigl GR0 11|||
rtt|||
nop|||
nop|||

exp_lablec:
movigl GR0 12|||
rtt|||
nop|||
nop|||

exp_labled:
addi gr31 gr30 1|||
movg2g gr30 gr31|||
rtt|||
nop|||
nop|||


boot:
.=1024
movigh GR0 0x0000  ||| 
movigl GR0 0x0000  ||| 
movigh GR1 0x1010  ||| 
movigl GR1 0x1010  ||| 
movigh GR2 0x2020  |||
movigl GR2 0x2020  ||| 
movigh GR3 0x3030  |||
movigl GR3 0x3030  ||| 
movigh GR4 0x4040  |||
movigl GR4 0x4040  ||| 
movigh GR5 0x5050  |||
movigl GR5 0x5050  ||| 
movigh GR6 0x6060  |||
movigl GR6 0x6060  ||| 
movigh GR7 0x7070  |||
movigl GR7 0x7070  ||| 
movigh GR8 0x8080  |||
movigl GR8 0x8080  ||| 
movigh GR9 0x9090  |||
movigl GR9 0x9090  ||| 

movigh GR10 0       |||
movigl GR10 0x0100  ||| 
movigh GR11 0       |||
movigl GR11 0x0110  ||| 
movigh GR12 0       ||| 
movigl GR12 0x0120  ||| 
movigh GR13 0       |||
movigl GR13 0x0130  ||| 
movigh GR14 0       |||
movigl GR14 0x0140  ||| 
movigh GR15 0       |||
movigl GR15 0x0150  ||| 
movigh GR16 0       ||| 
movigl GR16 0x0160  ||| 
movigh GR17 0       |||
movigl GR17 0x0170  ||| 
movigh GR18 0       |||
movigl GR18 0x0180  ||| 
movigh GR19 0       |||
movigl GR19 0x0190  ||| 
||store16 GR0  GR10 0 | store32    GR2  GR12  0
||store8  GR1  GR11 0 | store16    GR3  GR13  0
||store32 GR4  GR14 0 | load8      GR20 GR10  0
||load16  GR21 GR11 0 | store32    GR5  GR15  0
||store32 GR6  GR16 0 | load16     GR23 GR13  0
||load8   GR24 GR14 0 | load16     GR25 GR15  0
|||load32    GR23 GR13  0
|||load16    GR22 GR12  0
|||load32    GR21 GR11  0
|||load32    GR20 GR10  0

movigh GR30 0x0000  ||| 
movigl GR30 0x0000  ||| 
movigh GR31 0x0000  ||| 
movigl GR31 0x0000  ||| 
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
myloop:
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
jnc myloop|||
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
nop|nop|nop|nop
