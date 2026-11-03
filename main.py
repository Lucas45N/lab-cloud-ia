from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Microservico IA - Cap 02")

class EntradaTexto(BaseModel):
    texto: str

@app.get("/")
def health_check():
    return {
        "status": "Online",
        "ambiente": "OCI Vinhedo",
        "versao": "v2.0 - Deploy Automatizado",
        "capitulo": 2
    }

@app.get("/status")
def status_infra():
    return {
        "orquestrador": "Docker Compose",
        "resiliencia": "restart-always",
        "status": "Operacional"
    }

@app.post("/analisar")
def analisar_texto(payload: EntradaTexto):
    qtd_palavras = len(payload.texto.split())
    return {
        "entrada": payload.texto,
        "tokens_estimados": int(qtd_palavras * 1.3),
        "status": 200
    }
