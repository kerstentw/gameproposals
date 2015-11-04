#!python=/usr/bin/python2.7

import web, site

site.addsitedir("/var/www/GameProposals/bin") # this is to gain access to local modules
import bloghandler, sqlhandler

urls = (
"/home","HOME",
"/forum", "FORUM",
"/blog", "BLOG",
"/features", "FEATURES",
"/about", "ABOUT",
"/wiki", "WIKI",
"/favicon.ico","icon",
)

app = web.application(urls, globals())
render = web.template.render('/var/www/GameProposals/templates', base = '/var/www/GameProposals/templates/layout')


#########################################################Handler Classes

class HOME(object):
	
	def GET(self):
		try:
			news = open("/var/www/GameProposals/bin/sitenews.txt",'r')
			read_news = news.read()
			content = read_news
		
		except: 
			content = "There is no new news."

		finally:
			return render.home2(content = content)
		
	def POST(self):
		pass
		
		
		
class FORUM(object):
	
	def GET(self):
		content = "The Forum page is linked to frame."
		return render.forum(content = content)
		
	def POST(self):
		pass
		
		
class BLOG(object):
	
	def GET(self):
		content = (sqlhandler.blog_get(), bloghandler.blog_app()) # Blogs are kept in tuples as follows: (title, author, timestamp, body)
		return render.blog(content = content)
		
	def POST(self):
		pass
		
		
		
class FEATURES(object):

	def GET(self):
		content = sqlhandler.featuresget()
		return render.features(content = content)
		
	def POST(self):
		pass
		
		
		
class ABOUT(object):

	def GET(self):

		text = open("var/www/GameProposals/bin/aboutme.txt", "r")
		textread = text.read()
		content = textread
		
		
		
		return render.about(content = content)
			
	
	def POST(self):
		pass
		
		
class icon(object):
	
	def GET(self):

		raise web.seeother("static/favicon.ico")


		
class WIKI(object): #UNDER CONSTRUCTION
		
	def GET(self):
		content = "Under Construction"
		return render.wiki(content = content)
		
	def POST(self):
		pass
		
#########################################RUNS
		
app = web.application(urls, globals())
application = app.wsgifunc()
