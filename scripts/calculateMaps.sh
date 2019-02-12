#!/bin/bash
cd ../alexeydarknet/cyclist/
datas=$(ls *.data)
cd ../../weights/
cd $1
for data in $datas
	do
	for weight in *.weights
	    do
		../../alexeydarknet/darknet detector map ../../alexeydarknet/cyclist/$data train.cfg $weight -i 1 > map_result.txt
	        echo >> $data
        	echo >> $data
	        echo $weight >> $data
        	cat ../../alexeydarknet/cyclist/$data | grep valid >> $data
	        tail map_result.txt -n 6 >> $data
	done
done
exit
