from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class Grafo(BaseModel):
  vertices: int
  arestas: int
  valorado: bool

@app.get("/")
def read_root():
  return {"message": "api root"}

@app.post("/grafo")
async def get_grafo(grafo: Grafo):
  return grafo