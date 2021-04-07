#!/bin/bash
clear
echo "+----------------------------+"
sleep 0.5
echo "|  Script Swordfish: A senha |"
sleep 0.5
echo -e "+----------------------------+\n"

if [[ $1 == "-h" ]];
then
  echo "    Primeiro arqumento é o número do problema."
  echo "    O segundo é o número da questão."
  echo "    Exemplo: ./main.sh 1 2"
  echo -e "    Nesse caso, resolver problema 1, questão 2\n"
  exit
fi

if [[ $1 -le 1 ]];
then
  echo "Problema 1"
  if [[ $2 -le 1 ]];
  then
    echo -e "Questão 1\n"
    read -p "Número mínimo de Threads: " ntMin
    read -p "Número máximo de Threads: " ntMax
    cd ..
    while [[ $ntMin -le $ntMax ]]; do
      java -cp bin/:lib/* BenchmarkNumerosPrimos $ntMin 100000;
      sleep 5;
      ((ntMin++))
    done
  elif [[ $2 -le 2 ]];
  then
    echo -e "Questão 2\n"
    read -p "Quantidade ideal de threads para esse programa: " ntIdeal
    read -p "Valor máximo para buscar primos: " mxPrimo
    echo
    mnPrimoInit=100000
    cd ..
    while [[ $mnPrimoInit -le $mxPrimo ]]; do
      java -cp bin/:lib/* BenchmarkNumerosPrimos $ntIdeal $mnPrimoInit;
      sleep 5;
      ((mnPrimoInit+=100000))
    done
  elif [[ $2 -le 3 ]];
  then
    echo "[EXTRA]"
  fi
fi

if [[ $1 -le 2 ]];
then
  echo "Prblema 2"
  if [[ $2 -le 1 ]];
  then
    echo -e "Questão 1\n"
    read -p "Tamanho mínimo do array em KB: " arrayMin
    read -p "Tamanho máximo do array em KB: " arrayMax
    cd ..
    while [[ $arrayMin -le $arrayMax ]]; do
      java -cp bin/:lib/* BenchmarkAcessoMemoria $arrayMin 100000000;
      sleep 5;
      ((arrayMin+=1024))
    done
  elif [[ $2 -le 2 ]];
  then
    echo "[EXTRA]"
  fi
  fi
fi