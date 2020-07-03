



from datetime import date


def getDateExcel():
	today = date.today()
	day=today.day
	month=today.strftime("%B")
	year=today.year
	return str(day) + '-' + month + '-' + str(year)


def getMonthExcel():
	today = date.today()
	month='%02d' %today.month
	return month


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


def getDateExcelModified():
	today = date.today()
	day=today.day
	month=today.strftime("%b")
	year=today.year
	return str(day) + '-' + month + '-' + str(year)


def getDateFigureModified():
	today=date.today()
	day=f'{today.day:02d}'
	month=f'{today.month:02d}'
	year=str(today.year)
	return year + '-' + 'Jul' + '-' + day 





