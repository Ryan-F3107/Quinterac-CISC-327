#!/usr/bin/env bash
arg1="$1"
arg2="$2"
arg3="$3"
arg4="$4"
arg5="$5"
arg6="$6"
arg7="$7"
arg8="$8"
arg9="$9"
arg10="${10}"
arg11="${11}"
arg12="${12}"
arg13="${13}"
arg14="${14}"
arg15="${15}"
sh ./daily.sh $arg1 $arg2 $arg3 #deposits to the accounts created in daily
sh ./daily.sh $arg4 $arg5 $arg6 #withdraws from accounts created in daily
sh ./daily.sh $arg7 $arg8 $arg9 #transferring accounts
sh ./daily.sh $arg10 $arg11 $arg12 #create new accounts
sh ./daily.sh $arg13 $arg14 $arg15 #deposit into new accounts
SLEEP 100
#./weekly.sh Input4.txt Input5.txt Input6.txt Input7.txt Input8.txt Input9.txt Input10.txt Input11.txt Input12.txt Input13.txt Input14.txt Input15.txt Input16.txt Input17.txt Input18.txt
#./weekly.sh Input10.txt Input11.txt Input12.txt Input13.txt Input14.txt Input15.txt Input16.txt Input17.txt Input18.txt Input4.txt Input5.txt Input6.txt Input7.txt Input8.txt Input9.txt
