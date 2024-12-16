from fastapi import FastAPI
from endpoints import total_endpoints

app = FastAPI()



total_endpoints(app)
