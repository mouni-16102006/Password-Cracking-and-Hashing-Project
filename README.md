# Password Hashing & Cracking Simulation

A educational cybersecurity tool built in Python that simulates how modern identity systems protect user passwords using cryptographic hashing (SHA-256) and salting, alongside a demonstration of how attackers attempt to crack weak hashes using Dictionary and Brute-Force attack methods.

---

## 🔒 Project Overview & Use Case Diagram

In cybersecurity, passwords should never be stored in plain text. This project breaks down the defense-in-depth concepts of **one-way cryptographic hashing** and **salting** used to secure databases, while simultaneously demonstrating the offensive side: how weak mathematical algorithms or poor password choices are easily exploited by threat actors.

The diagram below maps out how a user safely registers a password vs. how an attacker tries to intercept and crack that password database.

```mermaid
graph TD
    %% Define Actors
    subgraph Users ["Actors"]
        User[("👤 Normal User<br/>(Registration)")]
        Attacker[("🥷 Threat Actor<br/>(Cracking)")]
    end

    %% System Boundaries
    subgraph DefensiveSystem ["System Database (Defense)"]
        SaltGen["1. Generate Random Salt"]
        HashFunc["2. SHA-256 Hash Function<br/>(Password + Salt)"]
        DB[("🗄️ Secure Database<br/>[Username | Salt | Hash]")]
    end

    subgraph OffensiveSystem ["Cracking Engine (Offensive)"]
        Wordlist["📁 Dictionary / Wordlist<br/>(rockyou.txt)"]
        CrackEngine{"Hash Match<br/>Simulator"}
        Success(["🎯 Password Cracked!"])
    end

    %% Workflow Connections
    User ==>|Inputs Plaintext Password| SaltGen
    SaltGen ==> HashFunc
    HashFunc ==>|Stores Securely| DB

    DB -.->|Database Leaked / Stolen| CrackEngine
    Wordlist ==>|Feeds Common Passwords| CrackEngine
    CrackEngine ==>|Finds Matching Math| Success

    %% Styling
    classDef defensive fill:#2ea44f,stroke:#fff,stroke-width:1px,color:white,font-weight:bold;
    classDef offensive fill:#d32f2f,stroke:#fff,stroke-width:1px,color:white,font-weight:bold;
    classDef storage fill:#fff3e0,stroke:#e65100,stroke-width:2px;

    class SaltGen,HashFunc defensive;
    class CrackEngine,Success offensive;
    class DB,Wordlist storage;
