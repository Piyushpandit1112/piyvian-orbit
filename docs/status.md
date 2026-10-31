
# PIYVIAN ORBIT — Project Status

Last updated: 2026-10-31
Status version: 0.2

## 1. Product Vision

PIYVIAN ORBIT is the Personal AI Operating System developed by PIYVIAN TECHNOLOGIES.

Tagline: "One command center. Your world, in orbit."

The goal is to bring professional, personal, learning and business workflows into one unified platform, coordinated by a central Supervisor and powered by specialist agents.

Career Intelligence is the first implementation module. The complete product vision must be preserved.

Primary product reference:
`PIYVIAN_ORBIT_Product_Blueprint_SRS_HLD_SDLC_Roadmap.pdf`

## 2. Complete Specialist Agent Catalogue

1. Supervisor / Orchestrator
2. Career Intelligence
3. Application Tracker
4. PIYVIAN Client Agent
5. Content / Social Media Agent
6. Learning Coach
7. Business Ideas Research Agent
8. Finance Agent
9. Personal / Family Health Assistant
10. Property Assistant
11. Personal Planner
12. Admin Studio

Do not remove or omit any specialist agent when planning implementation.

## 3. Product Experience Direction

The intended future product experience includes:

- Central AI Command Center.
- Dedicated specialist agent workspaces.
- Global tasks and approval inbox.
- Activity and audit history.
- Admin Studio for agent and AI operations management.
- Consistent navigation and design system.

The visual UI concept is a design reference, not a functioning application.

## 4. Engineering Principles

- Begin with a modular monolith.
- Use deterministic Python services for validation, filtering, deduplication and state transitions.
- Use LLMs for language understanding and reasoning where useful.
- Use human approval for consequential external actions.
- Preserve source evidence and audit history.
- Apply least-privilege permissions and data isolation.
- Avoid premature microservices and unnecessary infrastructure.
- Keep costs low during early development.

## 5. Learning Objectives

Learn and apply:

- Python and DSA in Python.
- OOP, SOLID and design patterns.
- Hexagonal Architecture and Clean Architecture.
- FastAPI, REST APIs and Pydantic.
- SQL, PostgreSQL and database design.
- Testing, debugging and security.
- Git, GitHub, CI/CD and deployment.
- HLD, LLD and system design.
- LangChain, LangGraph and Deep Agents.
- RAG, embeddings and vector databases.
- MCP, tools, skills and memory.
- LangSmith, evaluations and observability.

Career Intelligence should be taught and built slowly, step by step. Later agents can reuse the established foundations.

## 6. Current Development Environment

- Operating system: Windows.
- Python: 3.13.7.
- Git: 2.39.2.windows.1.
- Visual Studio Code: 1.143.1.
- Python virtual environment: `.venv`.
- Repository: https://github.com/Piyushpandit1112/piyvian-orbit
- Default branch: `main`.
- Repository visibility: Public.

Never commit secrets, API keys, passwords, `.env` files or private user records.

## 7. GitHub Progress

Completed and pushed:

- Initial `.gitignore`.
- Initial `README.md`.

The `docs/` directory has been created locally.

No application implementation has been committed yet.

## 8. Python Learning Progress

Topics covered:

- Lists, dictionaries, sets and tuples.
- Mutability, immutability and hashability.
- Hashing and set membership.
- Composite keys.
- String normalization.
- Python functions and return values.

Practical exercise completed in conversation:

A job deduplication prototype using normalized company, role and location values, tuple keys and a set.

This is a learning exercise only. It is not production implementation.

Production deduplication will follow the Product Blueprint:
- Prefer stable source IDs.
- Otherwise use cautious matching with normalized company, title, location and original URL.
- Preserve raw source data.
- Audit potential duplicate merges.

## 9. SDLC Progress

Current phase: Phase 0 — Discovery, Requirements and Engineering Setup.

Completed:
- Product Blueprint established.
- ChatGPT Project configured.
- GitHub repository created.
- Local repository cloned.
- Python, Git and VS Code verified.
- Virtual environment created.
- `.gitignore` committed and pushed.
- `README.md` committed and pushed.

Still open:
- Business Requirements Document (BRD).
- Career Intelligence Software Requirements Specification (SRS).
- Initial architecture decisions.
- Project conventions and testing setup.

No production application feature is complete yet.

## 10. Working Agreement

- Explain concepts before coding.
- Work one small step at a time.
- Let the learner write code and review their attempts.
- Include dry runs, edge cases and tests.
- Include relevant DSA, interview, LLD, HLD and architecture learning.
- Follow requirements, design, implementation, testing, documentation, GitHub and deployment practices.
- Keep job preparation progressing alongside ORBIT development.

## 11. Next Milestone

Continue Phase 0.

Next tasks:
1. Establish and baseline the ORBIT BRD.
2. Define Career Intelligence requirements.
3. Prepare the initial architecture decisions.
4. Complete the minimum engineering setup.
5. Begin implementation only after the relevant requirements and design are clear.

Update this document after every meaningful development session.

Distinguish clearly between proposed, implemented, tested and deployed features.
