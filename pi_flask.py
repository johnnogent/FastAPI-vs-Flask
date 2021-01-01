from flask import Flask, request, jsonify
import random, math, time
from flask_swagger import swagger

app = Flask(__name__ )

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)


@app.route("/", methods = ['GET'])
def api_pi():
  n = int(request.args['n'])
  start = time.time()
  m = 0
  for i in range(n):
    x = random.random()
    y = random.random()
    if x*x + y*y <=1:
      m += 1
  end = time.time()
  valeur = 4*m/n
  ecart = 100 * (valeur - math.pi) / math.pi
  return jsonify({
			'valeur': valeur,
			'ecart%': ecart,
			'temps': end-start,
			})
  
if __name__ == "__main__":
   app.run(port=5000,host='0.0.0.0')
