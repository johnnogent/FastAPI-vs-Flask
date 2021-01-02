# FastAPI-vs-Flask

In this repository I am making a test comparing FastAPI to Flask on one single use case

pi_flask and pi_fastapi are respectively in flask and in fastapi, they both receive a number as input and they calculate PI based on Monte-Carlo algorithm.
When running the programs, fastapi is slightly faster than flask, however, depending on simulations flask can be faster. 

run fastapi with 
      uvicorn pi_fastapi:app --reload
      
run flask with
      python pi_flask.py


