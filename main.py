import pymongo
import bottle

@bottle.route('/')
def site_index():
	return bottle.template('index_template')

bottle.debug(True)
bottle.run(host='localhost', port=8080)