#================================================================
#   
#   
#   Filename   : batchFolder.sh
#   Author     : Xueying Li
#   Created on  2021年08月02日 星期一 11时06分38秒
#   Description:
#
#================================================================

i=1201
for dir in sand_org;  # loop through files
do echo 
    mkdir -p "$dir"/sand_$i
    i=$((i+1))
done
