#!/bin/bash

numServer=1
numServer_max=25

echo $numServer
while [ $numServer -lt $numServer_max ]
do
	if [ $numServer -eq 1 ]
	then
		java -cp bin:lib/* ServidorWeb 9.5 0.84 $numServer 30 >> output/problema1-cm$numServer_max.txt
	else
		java -cp bin:lib/* ServidorWeb 9.5 0.84 $numServer 30 | cut -d$'\n' -f2 >> output/problema1-cm$numServer_max.txt
	fi
	((numServer++))
	echo $numServer
done


