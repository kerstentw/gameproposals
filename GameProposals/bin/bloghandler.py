from time import localtime

def month_convert(number):


	month = {
	1: 'January',
	2: 'February',
	3: 'March',
	4: 'April',
	5: 'May',
	6: 'June',
	7: 'July',
	8: 'August',
	9: 'September',
	10: 'October',
	11: 'November',
	12: 'December',
	
	}
		
	if number > 12 or number < 1:
		return number
		
	else:
		return month[number]
	


def blog_app(): #Returns a tuple containing (title, author, timestamp, body)
	title = "THIS IS BLOG TITLE"
	author = "THIS IS AUTHOR"
	timestamp = str(localtime()[0]) + ", " + month_convert(localtime()[1]) + " " + str(localtime()[2])
	body = "THIS IS BODY"
	
	return (title,author, timestamp, body)
	
