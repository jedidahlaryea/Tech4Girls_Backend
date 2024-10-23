#!/bin/bash
#Positional Argument in Bash Scripting
#$0 = scripts name or first argument
#$1 =second argument 
#$2 = third argument
#$3 =fourth argument

#echo "the first argument or the name of the script is: $0"
#echo "the second argument is: $1"
#echo "the third argument is: $2"
#echo "the fourth argument is: $3"

#sum=$(($1+$2))
#echo "The sum of $1 and $2 is: $sum"
#mul=$(($1*$2))
#echo "The mul of $1 and $2 is: $mul"
#diff=$(($1-$2))
#echo "The diff of $1 and $2 is: $diff"
#div=$(($1/$2))
#echo "The div of $1 and $2 is: $div"
#mod=$(($1%$2))
#echo "The mod of $1 and $2 is: $mod"

#touch file3
#mkdir folder3

#cp "$1" "$2"
#echo "$1 has been copied into $2"


# if [condition]
# then
#      statement
# fi

#read age

#if [ "$1" -gt 10 ] && [ "$2" -gt 10 ]
#then
 #   echo "Both numbers are greater than 10"
#else 
 #   echo "Boyh numbers sre not greater than 10"
#fi   

#read name

#if [[ ! $name == "Admin" ]];then
 #   echo "access denied"
#else
 #    echo "access granted"
#fi     

#while [ condition ] 
#do
#   [command]
#   [command]
#   [command]
# done

#number=1

#while [ $number -le 10 ]
#do 
 #  echo "$number"
  # number=$((number+1))
#done   

while true; do
  echo "Enter a number or type 'q' to quit"
  read number

  if [[ "$number" == "q" ]]; then
    break
  fi

  echo "You entered $number"
done 

echo "Exiting the loop"