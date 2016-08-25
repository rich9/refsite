import bottle
import os
import pymongo

@bottle.route('/')
def site_index():
	return bottle.template('index_template')

def main():
	bottle.debug(True)
	port = int(os.getenv('$PORT', 8080))
	bottle.run(host="http://refsite.herokuapp.com", port=port)

if __name__ == '__main__':
    main()
