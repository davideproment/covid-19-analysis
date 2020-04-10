

from PIL import Image
import getDate

from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import wget

import shutil
import os
import os.path


filelist=[ f for f in os.listdir('./') if f.endswith('png') ]
for f in filelist:
    os.remove(os.path.join('./', f))

filelist=[ f for f in os.listdir('./') if f.endswith('pdf') ]
for f in filelist:
    os.remove(os.path.join('./', f))

url='http://wilma.to.isac.cnr.it/diss/paolo/covid-19/england/england_regions_COVID_prediction_day_' + getDate.getDateFigure() + '.pdf'
filename='./england_regions_COVID_prediction_day_' + getDate.getDateFigure() + '.pdf'
wget.download(url, filename)
print(filename)


images=convert_from_path(filename)
filename=r'./england_regions_COVID_prediction_day_' + getDate.getDateFigure() + '.png'
images[0].save(filename)
print(filename)


filename='england_regions_COVID_prediction_day_' + getDate.getDateFigure() + '.pdf'
if(os.path.exists('./allPredictions/' + filename)):
	os.remove('./allPredictions/' + filename)
shutil.move('./' + filename, './allPredictions/')
print('./allPredictions/' + filename)

