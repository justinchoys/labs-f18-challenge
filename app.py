from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<poke>', methods=['GET'])
def pokenum(poke):
	r = requests.get('http://pokeapi.co/api/v2/pokemon/{0}/'.format(poke))
	json_r = r.json()
	#json_r = json.loads(r.content)
	try:
		int(poke)
		temp = 'id'
	except ValueError:
		temp = 'pokemon'
		
	return render_template('pokemon.html', r = json_r, query_type = temp)
 
if __name__ == '__main__':
    app.run()
