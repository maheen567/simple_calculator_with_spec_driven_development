# AI-Native Book + Embedded RAG Chatbot System Constitution

## Core Principles

### I. Spec-Driven Development
No implementation without written specification; All architectural decisions documented

### II. Modular Architecture
Clear separation: frontend, API, database, vector store; RAG pipeline split into ingestion, embedding, retrieval, generation

### III. Grounded Responses
All chatbot answers must use retrieved context; No hallucinations; If answer not found: “This answer is not available in the book.”

### IV. Production Standards
Clean structure; Environment-based configuration; Secure secret handling; Typed Python where applicable

### V. Reproducibility
Setup works from fresh clone; Clear installation and deployment documentation

### VI. Scalability Awareness
Qdrant Cloud for vector storage; Neon Serverless Postgres for structured data; Session-aware chat support

## Technical Stack

Frontend: Docusaurus v2, GitHub Pages deployment, Embedded React chatbot component; Backend: FastAPI (Python 3.11+), OpenAI Agents / ChatKit SDK, RESTful API with CORS configured; Database: Neon Serverless Postgres; Vector Database: Qdrant Cloud Free Tier; Embeddings: OpenAI embedding model.

## Book Content Standards

Explain: Spec-Driven Development, AI-native architecture, RAG systems, Vector databases & embeddings, Agents design, Deployment workflow; Writing clarity: Flesch-Kincaid 9–12; Code examples must be accurate and runnable.

## Governance

All changes must be versioned according to semantic versioning (MAJOR.MINOR.PATCH). Amendments require documentation, approval, and a migration plan. Compliance will be reviewed periodically.

**Version**: 1.0.0 | **Ratified**: 2026-02-26 | **Last Amended**: 2026-02-26
