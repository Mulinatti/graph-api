from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from Functions.contar_arestas import contar_arestas
from Functions.calcular_graus import calcular_graus
from Functions.adj_para_incid import adj_para_incid

app = FastAPI()

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
  return {"message": "api root"}

@app.post("/grafo")
async def get_grafo(grafo: List[List]):
  res = {
    "num_vertices": len(grafo),
    "num_arestas": contar_arestas(grafo),
    "graus_vertices": calcular_graus(grafo, False),
    "matriz_incidencia": adj_para_incid(grafo, False, False, contar_arestas(grafo))
  }
  
  return res