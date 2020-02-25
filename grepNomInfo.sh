#!/bin/ksh

node=`hostname`
rm -f cpu_all.tmp zzzz.tmp ${node}_nmon_cpu.csv
for nmon_file in `ls *nmon`
do
  datestamp=`echo ${nmon_file} | cut -f2 -d"_"`
  grep CPU_ALL, $nmon_file > cpu_all.tmp
  grep ZZZZ $nmon_file > zzzz.tmp
  grep -v "CPU Total " cpu_all.tmp | sed "s/,/ /g" | \
  while read NAME TS USER SYS WAIT IDLE rest
  do
    timestamp=`grep ${TS} zzzz.tmp | awk 'FS=","{print $4" "$3}'`
    TOTAL=`echo "scale=1;${USER}+${SYS}" | bc`
    echo $timestamp,$USER,$SYS,$WAIT,$IDLE,$TOTAL >> \
    ${node}_nmon_cpu.csv
  done
  rm -f cpu_all.tmp zzzz.tmp
done
