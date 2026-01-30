// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TruthChain - ESG Certification Ledger
 * @dev Smart Contract per la tracciabilità immutabile della filiera Made in Italy.
 * Progettato per garantire la trasparenza (Brand Activism) e prevenire il Greenwashing.
 */
contract TruthChain {
    
    // Struttura di un "Lotto" di prodotto (es. Vino, Olio)
    struct ProductBatch {
        uint256 id;
        address producer;        // Chi ha creato il lotto (Identità Wallet)
        string productType;      // Es. "Vino Barolo DOCG"
        string location;         // Es. "Serralunga d'Alba, IT"
        string esgCertificateHash; // Hash IPFS del certificato ESG/BIO (Non modificabile)
        uint256 carbonFootprint; // Dato ambientale (es. kgCO2eq)
        uint256 timestamp;       // Data di registrazione
        bool isVerified;         // Stato verifica (da ente terzo)
    }

    // Mappatura per salvare i lotti
    mapping(uint256 => ProductBatch) public batches;
    uint256 public batchCount = 0;

    // Evento pubblico: Chiunque può ascoltare la blockchain e vedere che un nuovo lotto è nato
    event BatchCreated(
        uint256 indexed batchId,
        address indexed producer,
        string productType,
        uint256 timestamp
    );

    // Funzione per registrare un nuovo lotto (La "Prova" digitale)
    function createBatch(
        string memory _productType,
        string memory _location,
        string memory _certificateHash,
        uint256 _carbonFootprint
    ) public {
        batchCount++;
        
        batches[batchCount] = ProductBatch(
            batchCount,
            msg.sender, // L'indirizzo wallet dell'azienda che chiama la funzione
            _productType,
            _location,
            _certificateHash,
            _carbonFootprint,
            block.timestamp,
            true 
        );

        // Emette l'evento per la trasparenza pubblica
        emit BatchCreated(batchCount, msg.sender, _productType, block.timestamp);
    }

    // Funzione per leggere i dati (Per il QR Code del consumatore)
    function getBatch(uint256 _id) public view returns (ProductBatch memory) {
        return batches[_id];
    }
}
