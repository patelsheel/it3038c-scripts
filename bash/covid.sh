#!/bin/bash
#This script will query covid data and display it 

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
STATES=$(echo $DATA | jq '.[0].states')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
ONVENTCURRENT=$(echo $DATA | jq '.[0].onVentilatorCurrently')

TODAY=$(date)

echo "ON $TODAY, in $STATES states there were $POSITIVE positive and $NEGATIVE negative COVID cases. With $HOSPITALIZED hospitalized and $ONVENTCURRENT on Ventilaor Currently."

