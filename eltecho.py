import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class AppHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class ElTecho(AppHandler):
    def get(self):
        self.render('eltecho.html')

class Acerca(AppHandler):
    def get(self):
        self.render('acerca.html')


app = webapp2.WSGIApplication([('/', ElTecho),
                               ('/acerca', Acerca)
                               ],
                               debug=True)

