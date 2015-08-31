num="eeee"
num2=${num}_ori
num3=${num2}".csv"
printf "ddd-- ${num} dd-- ${num2}",${num3}

st=`date "+%Y%m%d"`
end=`date -d "-7 days" +%Y%m%d`
printf "\n${st},,,${end}\n"
