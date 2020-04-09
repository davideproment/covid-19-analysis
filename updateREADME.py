

import getDate

import fileinput

filename='./README.md'

print(getDate.getPastDateFigure(), getDate.getDateFigure())


old='![Cumulative and daily deaths by England macro-area at ' + getDate.getPastDateFigure() + '](./england_regions_COVID_prediction_day_' + getDate.getPastDateFigure() + '.png)'
new='![Cumulative and daily deaths by England macro-area at ' + getDate.getDateFigure() + '](./england_regions_COVID_prediction_day_' + getDate.getDateFigure() + '.png)'

#print(old)
#print(new)

macs = {old : new}

for line in fileinput.input(filename, inplace=True):
    line=line.rstrip('\r\n')
    print(macs.get(line, line))