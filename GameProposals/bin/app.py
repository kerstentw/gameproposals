import web, 

urls = (
"/home","HOME",
"/forum", "FORUM",
"/blog", "BLOG",
"/features", "FEATURES",
"/about", "ABOUT",
"/wiki", "WIKI",
)

app = web.application(urls, globals())
render = web.template.render('templates/', base = 'layout')


#########################################################Handler Classes

class HOME(object):
	
	def GET(self):
		content = " LINKED!!!!!!!!!!! "
		return render.home(content = content)
		
	def POST(self):
		pass
		
		
		
class FORUM(object):
	
	def GET(self):
		content = "The Forum page is linked to frame."
		return render.forum(content = content)
		
	def POST(self):
		pass
import bloghandler	
		
		
class BLOG(object):
	
	def GET(self):
		content = bloghandler.blog_app() # Blogs are kept in tuples as follows: (title, author, timestamp, body)
		return render.blog(content = content)
		
	def POST(self):
		pass
		
		
		
class FEATURES(object):

	def GET(self):
		content = "The features are linked to frame."
		return render.features(content = content)
		
	def POST(self):
		pass
		
		
		
class ABOUT(object):

	def GET(self):
		content = "About it linked to frame."
		return render.about(content = content)
		
	def POST(self):
		pass
		
		
		
class WIKI(object): #UNDER CONSTRUCTION
		
	def GET(self):
		content = "Under Construction"
		return render.wiki(content = content)
		
	def POST(self):
		pass
		
#########################################RUNS
		
		
if __name__ == "__main__":
	app.run()
