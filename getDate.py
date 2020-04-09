



from datetime import date


def getDateExcel():
	today = date.today()
	day=today.day
	month=today.strftime("%B")
	year=today.year
	return str(day) + '-' + month + '-' + str(year)


def getDateFigure():
	today=date.today()
	day=f'{today.day:02d}'
	month=f'{today.month:02d}'
	year=str(today.year)
	return year + '-' + month + '-' + day 


def getPastDateFigure(pastDate=-1):
	today=date.today()
	day=f'{today.day+pastDate:02d}'
	month=f'{today.month:02d}'
	year=str(today.year)
	return year + '-' + month + '-' + day 







