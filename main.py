""" import neccessary libs"""
from fastapi import FastAPI
import uvicorn

api = FastAPI()

if __name__ == "__main__":
    uvicorn.run(api, port=8080, host="0.0.0.0")
