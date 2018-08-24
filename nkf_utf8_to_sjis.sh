#/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage : $0 <csv file(utf8&LF format)>"
  exit 1
fi

nkf -s -c,Lw $1
