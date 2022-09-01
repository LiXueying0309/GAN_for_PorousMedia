#! /bin/bash
#for loop from xxxx to xxxx 
for i in $(seq -f sand_org/sand_%g/ 1201 1319)
do
    #print case $i
    echo "Starting simulation sand_$i"

    #enter case directory
    cd sand_org/sand_$i/a/

    blockMesh
    snappyHexMesh
    
    cd ../../../
done
