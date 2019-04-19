
import jinja2

env = jinja2.Environment()
env.loader = jinja2.FileSystemLoader('templates')

template = env.get_template('test.html')

print(template.render(compliment="you're good"))


