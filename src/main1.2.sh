#!/bin/bash
clear
echo "+----------------------------+"
sleep 0.5
echo "|  Script Swordfish: A senha |"
sleep 0.5
echo -e "+----------------------------+\n"

echo "[1] Problema 1"
echo -e "[2] Problema 2\n"

read -p "Qual problema você quer resolver? " problem
echo ""
if [[ problem -eq 1 ]];
then
  echo "[A] Letra A"
  echo -e "[B] Letra B\n"
  read -p "Qual problema você quer resolver? " letter
  if [[ letter == "a" ]] || [[ letter == "A" ]];
  then

  fi

  read -p "Número mínimo de Threads: " ntMin
  read -p "Número máximo de Threads: " ntMax
  read -p "Número máximo para buscar primos: " nm

  ninit=100000
  cd ..
  while [ $ntMin -le $ntMax ] && [ $ninit -le  $nm ]; do
    java -cp bin/:lib/* BenchmarkNumerosPrimos $ntMin $ninit
    if [[ $ntMin -le $ntMax ]];
    then
      ((ntMin++))
    fi
    if [[ $ninit == $nm ]];
    then
      break
    fi
    ((ninit+=50000))
  done
elif [[ problem == 2 ]]
then
  echo ""
fi