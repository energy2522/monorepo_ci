#!/bin/bash

a=($(echo "$1" | tr ',' '\n'))
echo ${a[1]}

result="["
i=0
while [ $i -lt "${#a[@]}" ]; do
  if [ $result != "[" ]; then
    result+=", "
  fi

  result+="\""${a[$i]}"\""
  i+=1
done

result+="]"

echo $result