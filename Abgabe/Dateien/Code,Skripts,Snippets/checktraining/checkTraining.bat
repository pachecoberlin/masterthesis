ssh pacheco@10.149.71.3 sh train.sh
scp pacheco@10.149.71.3:~/laeufts C:\Temp\laeufts
set /p "x="<"C:\Temp\laeufts"
IF %x% EQU 0 (
    C:\Users\awachtberger\Music\Kalimba.mp3
    exit
)
scp pacheco@10.149.71.3:~/loss.txt C:\Users\awachtberger\Desktop\Python\data\loss.txt
cd C:\Users\awachtberger\Desktop\Python\
python plot.py -all -i 1000
scp C:\Users\awachtberger\Desktop\Python\loss.txt pacheco@192.168.0.5:~/data/loss.txt
