# Phase1: PDF Chatbot using FastAPI + LangChain

Upload PDF (upload - parse - extract text ) -> Done

↓

Chunk -> Done

↓

Embedding -> Done

↓

Vector DB

↓

Ask Question

↓

Answer

# Phase 2: Convert this appication into production grade HealthCare document Assistant

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

- step1: Clean the file structure - Done
- step2: Build functionalities for upload, ask, documents etc
- step3: Make API routes for all of them
- step4: Test
- step5: Connect it with RAG and LLM
- step6: Test
- step 7: Refactor code for better logging, specific exceptions etc  