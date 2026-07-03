# Enterprise Agentic AI Platform

## Project Vision

Build an **Enterprise Agentic AI Platform** from scratch using Python, LangGraph, and Gemini.

The goal is **not** to build a simple chatbot or follow tutorials. The goal is to understand how enterprise AI systems are architected, implemented, tested, and scaled.

Every feature should be implemented only after understanding the underlying architecture.

---

# Learning Philosophy

This project follows five steps for every new feature:

1. Understand the problem.
2. Design the architecture.
3. Implement the smallest possible change.
4. Test the implementation.
5. Refactor when necessary.

The focus is on becoming an AI Engineer rather than learning isolated code snippets.

---

# Technology Stack

* Python
* LangGraph
* Google Gemini
* Streamlit
* Git

Future additions (when needed):

* FastAPI
* Docker
* PostgreSQL
* Redis
* Vector Database
* MCP
* RAG
* Multi-Agent Systems
* Observability
* CI/CD

---

# Current Project Structure

```text
LangGraph-Chatbot/
│
├── app.py
├── chatbot.py
├── config.py
├── graph.py
├── nodes.py
├── state.py
├── requirements.txt
│
├── services/
│   └── llm_service.py
│
├── tools/
│   ├── __init__.py
│   └── calculator.py
│
└── PROJECT_CONTEXT.md
```

---

# Current Architecture

```text
                Streamlit UI
                      │
                      ▼
                 chatbot.py
                      │
                      ▼
                 LangGraph
                      │
              GraphState
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Greeting Node    Math Node     Search Node
                                      │
                                      ▼
                              llm_service.py
                                      │
                                      ▼
                                   Gemini
```

---

# Current GraphState

```python
class GraphState(TypedDict):
    question
    classification
    response
    tool_used
    messages
```

Current responsibilities:

* question → Current user request
* classification → Router decision
* response → Final response
* tool_used → Tool execution metadata
* messages → Conversation history (implementation in progress)

---

# Completed Modules

## Module 1 – Foundation

Completed:

* Python virtual environment
* Project structure
* Gemini API integration
* Streamlit interface

---

## Module 2 – LangGraph

Completed:

* StateGraph
* Nodes
* Conditional routing
* Workflow architecture

---

## Module 3 – Tools

Completed:

* Safe AST calculator
* Calculator tool integration
* Math routing

---

## Module 4 – Software Engineering

Completed:

* Git installation
* Git configuration
* First Git repository
* First Git commit

---

## Module 5 – Stateful Architecture

Completed:

* GraphState
* MemorySaver
* thread_id support
* Graph checkpointing

---

## Module 6 – Architecture Refactoring

Completed:

Created a dedicated Services layer.

Current structure:

```text
services/
    llm_service.py
```

Responsibilities:

* Gemini communication
* API error handling
* Future location for conversation-aware LLM logic

---

# Current Status

The application currently supports:

* Greeting
* Calculator
* Gemini responses
* LangGraph workflow
* MemorySaver
* thread_id

Conversation memory is **not yet complete**.

Reason:

Although checkpoints are enabled, conversation messages are not yet being appended to GraphState and therefore are not being supplied to the LLM.

---

# Current Learning Module

## Module 7 – Conversation Engine

Current objective:

Implement enterprise-grade conversation memory.

Architecture to implement:

```text
User
 │
 ▼
HumanMessage
 │
 ▼
GraphState.messages
 │
 ▼
LLM Service
 │
 ▼
Gemini
 │
 ▼
AIMessage
 │
 ▼
GraphState.messages
 │
 ▼
Checkpoint
```

Topics to learn:

* BaseMessage
* HumanMessage
* AIMessage
* SystemMessage
* ToolMessage
* Conversation state
* Checkpoint lifecycle
* Context management

---

# Architectural Principles

This project follows:

* Separation of Concerns
* Single Responsibility Principle
* Modular Architecture
* Enterprise Layered Design
* Shared GraphState
* Services Layer
* Tool Layer
* Small incremental refactoring
* Test after every change

---

# Roadmap

## Phase 1

* Foundation
* LangGraph
* Calculator
* Routing
* Git

Status:

Completed

---

## Phase 2

Stateful Agent

* Checkpointer
* Thread ID
* Conversation Memory
* Session Management
* Persistent Memory

Status:

In Progress

---

## Phase 3

Enterprise Agent

* Tool Registry
* Weather Tool
* Search Tool
* SQL Tool
* File Tool
* API Tool
* MCP Integration

Status:

Planned

---

## Phase 4

Retrieval-Augmented Generation

* Embeddings
* Chunking
* Vector Database
* Retrieval Pipeline
* Knowledge Base

Status:

Planned

---

## Phase 5

Multi-Agent Systems

* Supervisor Agent
* Research Agent
* Coding Agent
* Planner Agent
* Reviewer Agent

Status:

Planned

---

## Phase 6

Enterprise Platform

* Observability
* Logging
* Evaluation
* Authentication
* Deployment
* Docker
* FastAPI
* Production Architecture

Status:

Planned

---

# Coding Rules

Every implementation must follow this order:

1. Explain the concept.
2. Explain the architecture.
3. Identify the correct responsibility.
4. Implement the smallest change.
5. Test.
6. Refactor if necessary.

Avoid tutorial-style coding.

Understand every line before writing it.

Build the platform exactly as an enterprise AI engineering team would.
