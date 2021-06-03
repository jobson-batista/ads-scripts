#!/bin/bash

taxa_chegada=1
taxa_chegada_max=25

echo $taxa_chegada
while [ $taxa_chegada -lt $taxa_chegada_max ]
do
	if [ $taxa_chegada -eq 1 ]
	then
		java -cp bin:lib/* ServidorWeb $taxa_chegada 0.84 10 30 >> output/problema1-cm$taxa_chegada_max.txt
	else
		java -cp bin:lib/* ServidorWeb $taxa_chegada 0.84 10 30 | cut -d$'\n' -f2 >> output/problema1-cm$taxa_chegada_max.txt
	fi
	((taxa_chegada++))
	echo $taxa_chegada
done


