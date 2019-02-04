@echo off

ssh pacheco@10.149.71.3 sh train.sh
scp pacheco@10.149.71.3:~/laeufts C:\Temp\laeufts
set /p "x="<"C:\Temp\laeufts"
IF %x% EQU 0 (
    echo trying to start training
    start ssh pacheco@10.149.71.3 ./startTraining.sh
) ELSE (
    exit
)

echo >C:\Users\awachtberger\1.vbs wscript.sleep 15000
cscript C:\Users\awachtberger\1.vbs
del C:\Users\awachtberger\1.vbs

ssh pacheco@10.149.71.3 sh train.sh
scp pacheco@10.149.71.3:~/laeufts C:\Temp\laeufts
set /p "y="<"C:\Temp\laeufts"
IF %y% EQU 0 (
    echo trying to start training with one GPU
    start ssh pacheco@10.149.71.3 ./startTrainingSingleGPU.sh
) ELSE (
    exit
)

echo >C:\Users\awachtberger\1.vbs wscript.sleep 10000
cscript C:\Users\awachtberger\1.vbs
del C:\Users\awachtberger\1.vbs

ssh pacheco@10.149.71.3 sh train.sh
scp pacheco@10.149.71.3:~/laeufts C:\Temp\laeufts
set /p "z="<"C:\Temp\laeufts"
IF %z% EQU 0 (
    echo PLEASE CHECK YOUR TRAINING!
    C:\Users\awachtberger\Music\Kalimba.mp3
    pause
) ELSE (
    exit
)
