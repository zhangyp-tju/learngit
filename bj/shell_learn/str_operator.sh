var=http://www.linuxidc.com/123.htm 
echo ${var#*//}
echo ${var##*/}
echo ${var%/*}
echo ${var%%/*}
echo ${var:0-7}

echo ${var:7:5}


new_str=${var}${var}
printf "double var is :${new_str}\n"

num=5
zeros=0
#if test ${num} -lt 100 && test ${num} -gt 4
if test ${num} -lt 100 -a ${num} -gt 4
then
    printf "this number of ${num} is between 1 and 100\n"
elif [ ${num} -gt ${zeros} -a ${num} -eq 5 ]
then
    printf "is 5\n"
else
    printf "wrong!!\n"

fi

#[ -z "$1" ] && help

#input=`echo " -input /logdata/uigs/appsearch/201506"`
input=`echo " -input /logdata/uigs/appsearch/201506"`/2015062$i/*.lzo$input
echo "input is: ${input}"
