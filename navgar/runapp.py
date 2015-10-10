from paste.deploy import loadapp
 
application = loadapp('config:production.ini', relative_to='.')
