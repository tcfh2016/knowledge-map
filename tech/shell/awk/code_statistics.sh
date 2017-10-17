#!/bin/bash

function ParseStatisticsLine
{
  echo -n "$commitId," >> test.stat

  changedFileNum=(`echo "$statisticsLine" | awk 'BEGIN {FS=","} {print $1}'`)
  echo -n "$changedFileNum," >> test.stat

  insertedLineNum=(`echo "$statisticsLine" | awk 'BEGIN {FS=","} {print $2}'`)
  echo -n "$insertedLineNum," >> test.stat

  deletedLineNum=(`echo "$statisticsLine" | awk 'BEGIN {FS=","} {print $3}'`)
  echo "$deletedLineNum" >> test.stat
}

echo "SHA1,ChangedFiles,InsertedLines,DeletedLines" > $1.stat

for commitId in `cat $1`
do
  echo $commitId

  statisticsLine=`git show --stat $commitId | grep -i "changed,"`
  ParseStatisticsLine
done

cp $1.stat $1.csv

