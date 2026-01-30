# 💎 CareerSoul: The Trustless Professional Identity Protocol

![Status](https://img.shields.io/badge/Status-PoC_Live-success) ![Tech](https://img.shields.io/badge/Tech-Soulbound_Tokens-blueviolet) ![ESG](https://img.shields.io/badge/Focus-Social_Governance-green) ![License](https://img.shields.io/badge/license-MIT-blue)

> **"Dal Curriculum autodichiarato (LinkedIn) alla Reputazione Verificata crittograficamente."**

## 🌐 Vision
**CareerSoul** è un protocollo decentralizzato basato su **Soulbound Tokens (SBT)** che mira a risolvere la crisi di fiducia nel mercato del lavoro globale (*Fake Resume Epidemic*).

Attualmente, piattaforme come LinkedIn si basano su dichiarazioni non verificate. CareerSoul introduce il concetto di **Self-Sovereign Identity (SSI)** professionale: le competenze, le esperienze e le soft skills diventano asset digitali immutabili, firmati crittograficamente dai datori di lavoro e dai colleghi, e legati indissolubilmente all'identità del lavoratore.

---

## ⚠️ Il Problema (The Gap)
1.  **Credential Inflation:** I CV sono pieni di esagerazioni non verificabili.
2.  **Inefficienza:** Le aziende spendono miliardi in *Background Checks* manuali.
3.  **Bias Cognitivi:** Le assunzioni si basano spesso su prestigio universitario o bias di genere/etnia, ignorando le competenze reali (merito).
4.  **Soft Skills Invisibili:** Nessuno certifica l'empatia, la leadership o l'impegno sociale (ESG), rendendo difficile per le aziende valutare il fit culturale.

## 🛠 La Soluzione Tecnologica
Utilizziamo **Smart Contracts su Ethereum** per emettere certificati digitali che seguono lo standard **SBT (Soulbound Tokens)**.

* **Non Trasferibili:** A differenza di Bitcoin o NFT artistici, un SBT non può essere venduto. Se ottengo una certificazione, rimane nel mio wallet per sempre.
* **Trust Triangle:**
    * **Issuer (Emittente):** L'Azienda o Università (firma con la sua chiave privata).
    * **Holder (Lavoratore):** Riceve il Token nel suo Wallet.
    * **Verifier (Recruiter):** Verifica matematicamente la firma sulla Blockchain senza intermediari.

---

## 🎓 Collegamento ai Moduli del Master D-ESG

Il progetto è sviluppato come applicazione pratica e trasversale dei concetti appresi:

### 1. Blockchain Technology (Prof. Schifanella)
* Utilizzo di **Solidity** per creare token non fungibili e non trasferibili (SBT).
* Implementazione di funzioni di **Hashing (Keccak256)** per garantire l'integrità dei dati off-chain.
* Concetto di **Oracolo** nel backend Python per collegare dati reali (HR software) alla Blockchain.

### 2. Brand Activism & Governance (Prof.ssa Bertato)
* **Internal Brand Activism:** I dipendenti diventano ambasciatori certificati dei valori aziendali.
* **ESG Reporting:** Le aziende possono dimostrare con dati certi la qualità del capitale umano e le iniziative di welfare/formazione, migliorando il rating "G" (Governance).

### 3. Social Impact & Territorio (Prof.ssa Viano / Prof.ssa Bragaglia)
* **Meritocrazia Algoritmica:** Il sistema rimuove i bias umani. Un'esperienza validata ha lo stesso peso matematico indipendentemente dal genere o dall'etnia del lavoratore.
* **Valore ai Soft Skills:** Certificazione di attività di volontariato e impatto sociale territoriale come competenze professionali reali.

---

## 💻 Tech Stack

Il progetto è strutturato in tre livelli:

| Layer | Tecnologia | Descrizione |
| :--- | :--- | :--- |
| **Blockchain** | `Solidity` | Smart Contract `CareerSoul.sol` per la gestione degli SBT. |
| **Backend** | `Python (FastAPI)` | API Oracle per la validazione dei DID aziendali e calcolo ESG Score. |
| **Frontend** | `HTML5 / CSS3` | Interfaccia "Glassmorphism" per la visualizzazione del Wallet. |

## 🚀 Come Testare il PoC (Proof of Concept)

### 1. Smart Contract
Il contratto si trova in `/contracts/CareerSoul.sol`. Definisce la struttura dati `Experience` e impedisce il trasferimento del token (`revert` sulla funzione transfer).

### 2. Backend API
L'API simula un nodo validatore. Esegue il calcolo dell'**ESG Impact Score** basato sulle keyword delle skill (es. "Sustainability", "Ethics").

### 3. Frontend Demo
Apri il file `index.html` nel browser per visualizzare la dashboard del lavoratore con i certificati validati on-chain.

---

## 🔮 Roadmap Futura
- [ ] Integrazione ZKP (Zero-Knowledge Proofs): Per provare di avere una skill senza rivelare l'identità completa (Privacy GDPR).
- [ ] DAO di Validazione: Permettere ai colleghi di votare le skill tramite un sistema di reputazione ponderata.
- [ ] LinkedIn Plug-in: Visualizzare il badge "Verified by CareerSoul" direttamente sul profilo social.

---
*Progetto sviluppato da Luigi Logozzo per il Master D-ESG - Università di Torino.*
