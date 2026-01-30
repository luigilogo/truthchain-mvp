// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CareerSoul - Soulbound Tokens for Work Experience
 * @dev Implementazione semplificata di SBT (Soulbound Token).
 * I token rappresentano skill o esperienze lavorative e NON possono essere trasferiti.
 */
contract CareerSoul {
    
    struct Experience {
        string role;          // Es. "ESG Manager"
        string company;       // Es. "GreenTech SpA"
        string skills;        // Es. "Reporting, Blockchain, Teamwork"
        uint256 issueDate;    // Data emissione
        address issuer;       // Chi ha validato (Datore di lavoro)
    }

    // Mappatura: Indirizzo Lavoratore -> Lista Esperienze
    mapping(address => Experience[]) public cvLedger;
    
    // Evento: Qualcuno è stato assunto o promosso
    event ExperienceMinted(address indexed worker, string role, address issuer);

    // Funzione: Un datore di lavoro "Minta" (conia) un'esperienza sul wallet del dipendente
    function issueExperience(address _worker, string memory _role, string memory _company, string memory _skills) public {
        
        cvLedger[_worker].push(Experience(
            _role,
            _company,
            _skills,
            block.timestamp,
            msg.sender // L'indirizzo di chi chiama la funzione (l'azienda)
        ));

        emit ExperienceMinted(_worker, _role, msg.sender);
    }

    // Funzione: Leggi il CV verificato di qualcuno
    function getCV(address _worker) public view returns (Experience[] memory) {
        return cvLedger[_worker];
    }

    // Funzione "Soulbound": Se provi a trasferire il token, fallisce.
    // In un ERC-721 normale qui ci sarebbe il codice di trasferimento.
    // Qui lo blocchiamo apposta.
    function transfer(address, uint256) public pure {
        revert("SBT: Non puoi trasferire la tua esperienza lavorativa!");
    }
}
