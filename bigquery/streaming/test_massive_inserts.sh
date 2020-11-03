for i in {1..100}

do

  ./insert1.sh>./log/$i.log 2>&1 &

done
