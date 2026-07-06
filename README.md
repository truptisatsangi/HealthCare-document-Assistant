# Phase1: PDF Chatbot using FastAPI + LangChain

Upload PDF (upload - parse - extract text )

↓

Chunk

↓

Embedding 

↓

Vector DB (Local)

↓

Ask Question

↓

Answer

# Phase 2: Convert this application into production grade HealthCare document Assistant

## What exactly is this?
In this App the hospital upload relevant documents of the users like
- Medical reports
- Discharge summaries
- Lab reports
- Insurance documents
- Treatment guidelines 

Then user can ask queries related to his health based on the reports uploaded by the hospital such as

- What medications is the patient taking?
- Summarize the diagnosis.
- Does this patient have diabetes?
- What follow-up is recommended?

NOTE: For now this application is supporting only a single user and a single hospital. It will soon be scalable with the help of authentication and sessions to support multi patients and multi hospitals support. Keep an eye on it 

## Now steps to achieve the phase 2

1. Clean project structure
2. Define models & configuration 
    - Pydantic models
    - config.py
    - Environment variables

3. Implement Services

    - Report Service
    - Chunking Service
    - Embedding Service
    - Retrieval Service
    - Prompt Service
    - LLM Service

4. Create API routes

    - POST /upload
    - POST /ask
    - GET /documents
    - GET /health

5. Integrate Vector DB + RAG + LLM

    - Store embeddings
    - Retrieve Top-K
    - Build prompt
    - Generate answer

6. Testing

    - Happy path
    - Invalid PDF
    - Empty PDF
    - Invalid query
    - No relevant context

7. Production improvements

    - Logging
    - Custom exceptions
    - Input validation
    - Metadata
    - Configurable chunk size, Top-K, temperatureexceptions etc  


## Architecture

                 Hospital User
                       │
                POST /upload
                       │
                 Validation Layer
                       │
                 PDF Parser
                       │
                 Chunking Service
                       │
               Embedding Service
                       │
      (Chunk + Metadata + Embedding)
                       │
                  Chroma Vector DB
                       │
        ────────────────────────────────────
                    User Query
                       │
                  POST /ask
                       │
               Query Embedding
                       │
              Similarity Retrieval
                       │
                 Top-K Chunks
                       │
                 Prompt Builder
                       │
                  LLM (Phi/OpenAI)
                       │
               Answer + Sources
               

### Entities/Actors 
- Hospital 
- User 
- Admin

### API
- POST /upload 
- POST /ask
- GET /documents
- DELETE /documents
- GET /health

### Services 
- PDF Service
- Chunking Service
- Embedding Service
- Retrieval Service
- LLM Service
- Prompt Service

### Database 
Vector DB (Chroma)

### Models
**UploadRequest**
- patient_id
- patient_name
- report (UploadFile)

**AskRequest**
- patient_id
- query
- category (optional) ENUM -> (general, current medication, summary, deasease query, recommedation)

**AnswerResponse**
- patient_id
- answer
- sources (page, filename)
- category

**DocumentMetadata**
- patient_id
- filename
- upload_time
- page_count

![alt text](<Screenshot from 2026-07-06 17-09-33.png>)
