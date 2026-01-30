import time
import hashlib
import random
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from datetime import datetime

# --- CONFIGURAZIONE ---
app = FastAPI(
    title="CareerSoul API Protocol",
    description="Decentralized Identity Oracle & SBT Issuer Node",
    version="2.1.0-beta",
    docs_url="/docs"
)

# --- MODELLI DATI (Pydantic) ---
# Simula la struttura dati rigida richiesta dalla Blockchain (Smart Contract)
class SoulboundRequest(BaseModel):
    worker_wallet: str = Field(..., description="Indirizzo Ethereum del lavoratore")
    role: str = Field(..., description="Ruolo ricoperto (es. ESG Manager)")
    company: str = Field(..., description="Nome Azienda Emittente")
    skills: List[str] = Field(..., description="Lista competenze validate")
    issuer_did: str = Field(..., description="DID (Decentralized ID) dell'azienda")

class VerificationResponse(BaseModel):
    tx_hash: str
    token_id: str
    block_number: int
    timestamp: str
    gas_used: float
    esg_impact_score: int  # Bonus: Calcoliamo l'impatto sociale!

# --- LOGICA DI BUSINESS ---

def simulate_gas_fee():
    """Simula il costo computazionale della rete Ethereum."""
    return round(random.uniform(0.002, 0.005), 6)

def calculate_esg_score(skills: List[str]) -> int:
    """
    Algoritmo 'Social Impact' (Modulo Viano/Bardini).
    Assegna un punteggio basato sulla natura etica delle skill.
    """
    impact_keywords = ['sustainability', 'esg', 'diversity', 'inclusion', 'carbon', 'green', 'social']
    score = 50 # Base score
    for skill in skills:
        if any(key in skill.lower() for key in impact_keywords):
            score += 10
    return min(score, 100) # Cap a 100

def generate_keccak_mock(data: str) -> str:
    """Simula l'hashing crittografico di Ethereum."""
    return "0x" + hashlib.sha3_256(data.encode()).hexdigest()

# --- ENDPOINTS API ---

@app.get("/")
def read_root():
    return {
        "node_status": "ONLINE",
        "protocol": "CareerSoul SBT v2",
        "connected_peers": 142,
        "last_block": 18239402
    }

@app.post("/mint-experience", response_model=VerificationResponse, status_code=status.HTTP_201_CREATED)
async def mint_sbt(request: SoulboundRequest):
    """
    ORACLE NODE:
    1. Riceve la richiesta dall'Azienda.
    2. Valida la firma crittografica (simulata).
    3. Esegue la transazione sullo Smart Contract 'CareerSoul'.
    4. Emette il Token Soulbound non trasferibile.
    """
    
    # 1. Simulazione validazione DID (Anti-Fraud)
    if not request.issuer_did.startswith("did:eth:"):
        raise HTTPException(status_code=400, detail="Invalid Issuer DID format")

    # Simuliamo un tempo di attesa per la "Proof of Work/Stake"
    # (Effetto scenico per la demo)
    time.sleep(1.5) 

    # 2. Creazione della Transazione
    tx_content = f"{request.worker_wallet}{request.role}{datetime.now()}"
    tx_hash = generate_keccak_mock(tx_content)
    token_id = str(random.randint(1000, 9999))
    
    # 3. Calcolo Score ESG
    impact_score = calculate_esg_score(request.skills)

    # 4. Risposta del Nodo
    return {
        "tx_hash": tx_hash,
        "token_id": f"SBT-{token_id}",
        "block_number": random.randint(18000000, 19000000),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "gas_used": simulate_gas_fee(),
        "esg_impact_score": impact_score
    }

@app.get("/verify-credential/{token_id}")
async def verify_credential(token_id: str):
    """
    Endpoint pubblico per i Recruiter.
    Verifica se un token è valido e non revocato.
    """
    # Simuliamo che il token esista sempre per la demo
    return {
        "token_id": token_id,
        "is_valid": True,
        "revoked": False,
        "issuer_signature": "0xVALIDATED_BY_CAREERSOUL_PROTOCOL",
        "blockchain_explorer_url": f"https://etherscan.io/token/{token_id}"
    }
