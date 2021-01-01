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
  value = 4*m/n
  difference = 100 * (value - math.pi) / math.pi
  return {'value': value,
	'diff%': difference,
	'time': end-start,
	}
