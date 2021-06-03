#!/bin/bash

taxaChegada=8
taxaChegada_max=10
echo $taxaChegada
while [ $taxaChegada -lt $taxaChegada_max ]
do
	if [ $taxaChegada -eq 1 ]
	then
		java -cp bin:lib/* ServidorWeb $taxaChegada 0.84 8 30 >> output/problema1-taxaChegada$taxaChegada_max.txt
	else
		java -cp bin:lib/* ServidorWeb $taxaChegada 0.84 8 30 | cut -d$'\n' -f2 >> output/problema1-taxaChegada$taxaChegada_max.txt
	fi
	((taxaChegada+=1/2))
	echo $taxaChegada
done


