#!/bin/ksh

node=`hostname`
rm -f mem_all.tmp zzzz.tmp ${node}_nmon_mem.csv
for nmon_file in `ls *nmon`
do
  datestamp=`echo ${nmon_file} | cut -f2 -d"_"`
  grep MEM, $nmon_file > mem_all.tmp
  grep ZZZZ $nmon_file > zzzz.tmp
  grep -v "Memory MB " mem_all.tmp | sed "s/,/ /g" | \
  while read NAME TS USER SYS WAIT IDLE FREE rest
  do
    timestamp=`grep ${TS} zzzz.tmp | awk 'FS=","{print $4" "$3}'`
    TOTAL=`echo "scale=1;${USER}-${FREE}" | bc`
    echo $timestamp,$USER,$SYS,$WAIT,$IDLE,$FREE,$TOTAL >> \
    ${node}_nmon_mem.csv
  done
  rm -f mem_all.tmp zzzz.tmp
done
