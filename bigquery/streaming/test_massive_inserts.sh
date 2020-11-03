# This code uses the one by one insert and repeats it x times (1000 by default) in order to test massive insert performance
for i in {1..1000}

do

  ./insert1.sh>./log/$i.log 2>&1 &

done
