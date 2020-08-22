

import getDate

'''
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
'''


filename='./README.md'

with open(filename, 'r') as file:
    # read a list of lines into data
    data = file.readlines()

data[8]='![Cumulative and daily deaths by England macro-area at ' + getDate.getDateFigure() + '](./england_regions_COVID_prediction_day_' + getDate.getDateFigure() + '.png)\n'

with open(filename, 'w') as file:
    file.writelines( data )