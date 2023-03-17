for v in forward up down do 
  echo -n "$v: "
  awk -v v="$v"  '$1 == v {sum += $2} END {print sum}' data.txt
done
#forward: 2033
#up: 1075
#down: 1843
#============
#x = forward = 2033
#y = down - up = 1843 - 1075 = 768
#answer = xy = 1561344