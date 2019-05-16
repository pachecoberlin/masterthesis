#!/bin/bash

cat temp.txt | grep rate > loss.txt

# Test if the process is running and giving information if so
wtf=$(ps -ef | grep [d]arknet | wc -l)
# if only 1 is only the ps call, musst be 2 while running
if [ $wtf = "1" ]
then
      echo "TRAINING IS NOT RUNNING"
        echo 0 > laeufts
#      setsid /home/pacheco/darknet/darknet detector train /home/pacheco/darknet/cyclist/cyclist.data  /home/pacheco/da$else
      echo "training is on"
        echo 1 > laeufts
fi
ls -al /home/pacheco/darknet/backup | grep backup
ls -al /home/pacheco/ | grep loss.txt
ps -u pacheco -f | grep darknet
exit