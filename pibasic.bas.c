

10 REM CALCULATES PI
15 T = TIME
20 R1=1.00
30 R2=1.00
40 S1=1000000
50 I=0
60 W1=R1/S1
70 S2=0
80 Y0=SQR(R2-(I/S1)^2)
85 IF I>=S1 THEN 130
90 I=I+1
100 Y1=SQR(R2-(I/S1)^2)
110 S2=S2+W1*(Y0+Y1)/2.00
120 Y0=Y1
125 GOTO 85
130 S2=4.00*S2
140 DISP"PI=";S2
145 T=TIME-T
146 DISP"ELAPSED TIME=";T;" SEC"
150 END

