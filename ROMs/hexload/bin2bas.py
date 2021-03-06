import os;
import math;
import sys;

BIN_NAME = "hexload.bin"
mem = 0xF800

bin_size = os.stat(BIN_NAME).st_size;
grp8 = int( math.ceil( bin_size / 4.0 ) );

print "new "
print "clear "
print "10 REM Created by Filippo Bergamasco and modified by DaveP for the RC2014"
print "20 REM Version 0.01"
print "30 Print \"Loading Data\""
print "40 let mb=&Hf800"
print "50 print \"Start Address:\",hex$(mb) "
print "60 REM Go to READ Subroutine."
print "70 GOSUB 1000"
print "80 print \"End Address:\",hex$(mb-1)"
print ""
print "90 REM Change Pointer for USR"
print "100 GOSUB 1100"
print ""
print "110 REM RUN THE CODE!"
print "120 print usr(0)"
print "130 END "
print ""
print "1000 REM Routine to load Data"
print "1010 REM Needs var mb set to start location20 read a"
print "1020 read a"
print "1030 if a>255 then RETURN"
print "1040 rem print HEX$(mb),a"
print "1050 poke mb, a "
print "1060 let mb=mb+1 "
print "1070 goto 1020"
print ""
print "1100 REM    Location of pointer &H8049"
print "1110 print \"Change Jump Location\" "
print "1120 let mb=&H8048 "
print "1130 REM    JP start address (c3 00 f8) jp f800"
print "1140 poke mb,&Hc3 "
print "1150 poke mb+1,&H00 "
print "1160 poke mb+2,&Hf8"
print "1170 RETURN "

iidx=9010;
with open(BIN_NAME, "rb") as f:

    bts = f.read(12)

    while len(bts) >= 1:

        while len(bts) < 12:
            bts = bts + chr(0)

        sys.stdout.write( str(iidx) + " data " )

        for kk in range(0, len(bts)-1):
            sys.stdout.write( str( ord(bts[kk]) )+",")

        sys.stdout.write( str( ord(bts[len(bts)-1])) )
        bts = f.read(12)
        print ""

        iidx = iidx+30


print str(iidx)+" data 999"
print "9999 END"
print "run"
