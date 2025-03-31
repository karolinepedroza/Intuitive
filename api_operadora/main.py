from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from infra.database import obter_cadastros_operadoras
from typing import Any

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/lista_cadastros_operadoras")
async def lista_cadastros_operadoras() -> Any:
    try:
        print("Iniciando consulta ao banco de dados...")
        cadastros = obter_cadastros_operadoras()
        print("Consulta realizada com sucesso!")
        return {"operadoras": cadastros}
    except Exception as e:
        print(f"Erro na consulta: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao obter cadastros das operadoras.")

if __name__ == "__main__":
    import uvicorn
    print("Iniciando a aplicação FastAPI...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)