#!/bin/bash
function ParseCounter
{
	echo -n "$startTime," >> $OutputFile
	for((i=0;i<=11;i++));do
		PMID="M8061C$i"
		counter=(`cat $InputFile | sed "s/^.*<${PMID}>//g" | sed "s/<\/${PMID}>.*//g"`)
		echo -n "$counter," >> $OutputFile
	done
	PMID="M8061C19"
	counter=(`cat $InputFile | sed "s/^.*<${PMID}>//g" | sed "s/<\/${PMID}>.*//g"`)
	echo "$counter" >> $OutputFile
}


rm LNCEL-*.stat LNCEL-*.csv
echo "startTime,M8061C0,M8061C1,M8061C2,M8061C3,M8061C4,M8061C5,M8061C6,M8061C7,M8061C8,M8061C9,M8061C10,M8061C11,M8061C19" > LNCEL-1.stat
cp LNCEL-1.stat LNCEL-2.stat
cp LNCEL-1.stat LNCEL-3.stat

for file in `ls $1`
do
	if [ -d $1"/"$file ]
	then
		echo "is directory."
	else
		startTime=`cat $1"/"$file | sed 's/^.*startTime=//g' | sed 's/interval.*//g' | head -n 1 | sed 's/"//g'` 		

		cat $1"/"$file | sed 's/measurementType/AAAAmeasurementType/g' | sed 's/AAAA/\n/g' | grep -i "LTE_M_per_LNCEL" > temp.txt
		cat temp.txt | grep -i 'LNCEL-1' > LNCEL-1.txt
		cat temp.txt | grep -i 'LNCEL-2' > LNCEL-2.txt
		cat temp.txt | grep -i 'LNCEL-3' > LNCEL-3.txt
		for((j=1;j<=3;j++));do
			InputFile=LNCEL-$j.txt
			OutputFile=LNCEL-$j.stat
			ParseCounter
		done
	fi
done

cp LNCEL-1.stat LNCEL-1.csv
cp LNCEL-2.stat LNCEL-2.csv
cp LNCEL-3.stat LNCEL-3.csv
