#!/bin/bash
for line in $(cat jog1.txt); do 
	count=0 
	for num in $(cat jog2.txt); do 
		if [ "$num" -eq "$line"  ]; then 
			#echo -e "$num   $count"
			let count++ 
		fi 
	done 
	echo -e "$count $line" >> qde_num.txt 
done
