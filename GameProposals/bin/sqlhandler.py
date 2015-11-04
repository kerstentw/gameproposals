import os, sys, psycopg2, time



def featuresget():
	
	#Iteration v0.01 (noreq): Will fetch all entries from SQL and will return a tuple
	#Iteration v0.02: Will fetch select entries and return tuple
	
	conn = psycopg2.connect("port = 5432 host = localhost dbname = gameproposals password = runner1$ user = postgres")
	
	cur = conn.cursor()
	
	cur.execute('SELECT * FROM "GP_features";') #NOTE that you have to maintain quote syntax so use '' around "" for fetching names of tables and columns
	return cur.fetchall()

def features_html_construct(html):
	'''Takes a tuple and returns a printable HTML'''
	pass
	
########################################################################################S
	
	
def blog_get():
	'''Fetches blog info from SQL '''
	conn = psycopg2.connect( "port = 5432 host = localhost dbname = gameproposals password = runner1$ user = postgres")
	cur = conn.cursor()
	
	cur.execute('SELECT * FROM "GP_blog";')
	return cur.fetchall()


#Iteration v0.13: This class object will decide if request from framework
#	is a blog or feature and return HTML as requested from html
#	ie. if the piece is a blog it will return blog formatting from the
#	blog table and likewise for the features.


class fetcher(object):
	def __init__(self):
		pass
	
	def features_get(self):
		pass
		
	def html_get(self):
		pass
