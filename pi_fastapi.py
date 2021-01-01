# from typing import Optional

from fastapi import FastAPI
import random, math, time

app = FastAPI()


@app.get("/")
def api_pi(n : int):
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
  return {'valeur': valeur,
			'ecart%': ecart,
			'temps': end-start,
			}

'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
'''
