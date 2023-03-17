#!/bin/bash
for f in $(find $(dirname $0) -type f -name "*.py"); do 
  echo -n "$f: "
  sed '/^\s*#/d;/^\s*$/d' $f | grep -v "logging\." | wc -l
done
