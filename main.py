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


#Tipo de objeto a ser recebido na requisição
class Request(BaseModel):
  matriz: List[List[int]]
  valorado: bool


#CRIAÇAO DAS ROTAS - Tudo que será retornado para o front-end.
@app.get("/")
def read_root():
  return {"message": "api root"}

@app.post("/grafo")
async def get_grafo(grafo: Request):
  res = {
    "matriz_adjacencia": grafo.matriz,
    "num_vertices": len(grafo.matriz),
    "num_arestas": contar_arestas(grafo.matriz, False, grafo.valorado),
    "graus_vertices": calcular_graus(grafo.matriz, False),
    "matriz_incidencia": adj_para_incid(grafo.matriz, False, grafo.valorado, contar_arestas(grafo.matriz, False, grafo.valorado))
  }
  
  return res


@app.post("/digrafo")
async def get_grafo(digrafo: Request):
  res = {
    "matriz_adjacencia": digrafo.matriz,
    "num_vertices": len(digrafo.matriz),
    "num_arestas": contar_arestas(digrafo.matriz, True, digrafo.valorado),
    "graus_vertices": calcular_graus(digrafo.matriz, True),
    "matriz_incidencia": adj_para_incid(digrafo.matriz, True, False, contar_arestas(digrafo.matriz, True, digrafo.valorado))
  }
  
  return res