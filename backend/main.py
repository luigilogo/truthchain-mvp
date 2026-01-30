from fastapi import FastAPI
from pydantic import BaseModel
import datetime

# In un caso reale, qui importeremmo web3.py per connetterci al contratto
# from web3 import Web3 

app = FastAPI(
    title="TruthChain API",
    description="Backend per la certificazione ESG su Blockchain",
    version="1.0.0"
)

# Modello dei dati che l'azienda invia
class BatchData(BaseModel):
    product_type: string
    location: string
    certificate_url: string # Link al PDF del certificato
    carbon_footprint: float

# Simulazione Database (in memoria)
fake_blockchain_db = []

@app.post("/register-batch/")
async def register_batch(data: BatchData):
    """
    Simula la scrittura su Blockchain (transazione).
    In produzione, questa funzione chiamerebbe 'createBatch' dello Smart Contract.
    """
    
    # Creazione dell'Hash simulato (Impronta digitale del certificato)
    # Citazione Schifanella: L'hash garantisce l'integrità del dato off-chain.
    mock_hash = f"0x{hash(data.certificate_url + str(datetime.datetime.now()))}"
    
    new_block = {
        "id": len(fake_blockchain_db) + 1,
        "data": data,
        "tx_hash": mock_hash,
        "timestamp": datetime.datetime.now(),
        "status": "IMMUTABLE_ON_CHAIN"
    }
    
    fake_blockchain_db.append(new_block)
    
    return {
        "message": "Lotto registrato con successo su TruthChain",
        "qr_code_url": f"https://truthchain.app/verify/{new_block['id']}",
        "blockchain_tx": mock_hash
    }

@app.get("/verify/{batch_id}")
async def verify_product(batch_id: int):
    """
    Endpoint pubblico per il consumatore che scansiona il QR Code.
    Restituisce i dati verificati (Brand Activism).
    """
    # Recupera dal "Ledger"
    for block in fake_blockchain_db:
        if block["id"] == batch_id:
            return block
    return {"error": "Prodotto non trovato o contraffatto"}
