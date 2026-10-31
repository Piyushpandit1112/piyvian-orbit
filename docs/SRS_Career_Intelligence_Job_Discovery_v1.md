# PIYVIAN ORBIT — Software Requirements Specification (SRS)
## Career Intelligence: Job Discovery v1

**Product:** PIYVIAN ORBIT  
**Company:** PIYVIAN TECHNOLOGIES  
**Document ID:** ORBIT-SRS-CI-JD-001  
**Version:** 0.1  
**Status:** Draft for review  
**Prepared:** 31 October 2026  
**Parent requirement baseline:** PIYVIAN ORBIT BRD v0.1 (approved in the project conversation)  
**Primary product reference:** PIYVIAN_ORBIT_Product_Blueprint_SRS_HLD_SDLC_Roadmap.pdf, Draft v0.1, 27 October 2026

> This SRS defines the first Job Discovery vertical slice. It does not replace the complete ORBIT Product Blueprint or the broader Career Intelligence requirements in the BRD. Requirements outside this slice remain part of the product roadmap unless explicitly changed through document versioning.

---

## 1. Purpose

This document specifies the user-visible and system requirements for **Job Discovery v1**, the first working vertical slice of Career Intelligence.

The release must let the product owner enter job-search criteria, manually retrieve job postings from one approved pilot source, normalize and validate the returned records, store source evidence and normalized job data in PostgreSQL, and view the resulting jobs in a responsive web interface.

The aim is to prove a complete, testable workflow before adding multiple connectors, scheduled discovery, advanced matching, or Agentic AI workflows.

## 2. Product context and guiding principles

PIYVIAN ORBIT is the Personal AI Operating System product of PIYVIAN TECHNOLOGIES. Career Intelligence is the first implementation module; it is not the entire product.

The complete specialist-agent catalogue remains in the product baseline:

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

Job Discovery v1 is deliberately a **deterministic software workflow**, not an AI agent. Python services perform retrieval orchestration, validation, normalization, persistence, and filtering. No LLM is required to deliver this slice.

Guiding principles:

- Start with a modular monolith; do not introduce microservices or Kubernetes for this slice.
- Keep source records and normalized application records distinct.
- Preserve source attribution, original URLs, and retrieval timestamps.
- Treat job-board content and external responses as untrusted data, never as instructions to the application.
- Never invent salary, sponsorship, eligibility, location, or other missing facts.
- Build the pilot in a way that can later support a connector framework, without implementing the full registry now.
- Develop and test locally first. Do not expose an internet-accessible deployment before the required authentication and security controls are in place.

## 3. Scope

### 3.1 In scope for Job Discovery v1

- A manual search initiated by the user from the Career Intelligence workspace.
- Search input for a role/title/keyword query and target country or location criteria supported by the selected pilot source.
- Optional basic filters where the pilot source reliably provides the necessary data, such as work arrangement and employment type.
- One job-source connector selected after a source feasibility and permission review.
- Retrieval of job postings using a permitted API, feed, ATS endpoint, or other authorized method.
- Preservation of the raw source response or a traceable raw source record, source metadata, and retrieval time.
- Mapping into a common ORBIT job record shape.
- Required-field validation and safe handling of missing optional fields.
- Basic deterministic filtering based on the criteria actually supported in this slice.
- PostgreSQL persistence for search runs, source observations, and normalized job records.
- Idempotent persistence of repeat observations of the same source posting, using a stable source identifier where available and a safe source-specific fallback where necessary.
- A FastAPI backend and a responsive React/Vite user interface, subject to the technology validation already identified in the BRD.
- Result, empty, loading, validation-error, and source-failure UI states.
- Automated unit, integration, API, and frontend tests appropriate to this slice.

### 3.2 Explicitly out of scope for this slice

The following remain in the Career Intelligence/product roadmap but are not required for Job Discovery v1:

- Scheduled searches (including the planned default daily schedule).
- Multiple production connectors and the full Source Connector Registry.
- Broad cross-source/fuzzy deduplication and human review of uncertain duplicate merges.
- Master Career Profile, resume upload/extraction, resume tailoring, or resume scoring.
- Saved search profiles and advanced user-configurable matching weights.
- Explainable match scoring or AI/LLM-based job analysis.
- Salary normalization, currency conversion, and advanced salary filtering.
- Work-authorization assessment, legal eligibility conclusions, or sponsorship inference.
- Application submission, Application Tracker workflows, email/Gmail/Outlook integration, or application-event parsing.
- Email/in-app alerts, reminders, or notification scheduling.
- RAG, vector search, LangChain, LangGraph, Deep Agents, MCP, and model routing.
- A multi-user SaaS implementation, organization/workspace administration, or subscription billing.
- Native Android/iOS applications.

No item is removed from the long-term vision by being excluded from this first slice.

## 4. Users and operating environment

### 4.1 Primary user

The first usable release is a personal-use MVP for the product owner. Future multi-user access is an architectural direction, not a feature to build into this slice prematurely.

### 4.2 Operating environment

- Local development on the existing Windows development machine.
- Python backend using FastAPI/Pydantic as the preferred direction.
- React/Vite responsive web frontend as the preferred direction.
- PostgreSQL as the persistence layer.
- English interface for the initial implementation.
- Desktop browser as the primary development/test target, with responsive behavior for tablet and mobile browser widths.

Exact dependency versions and hosting provider are implementation/architecture decisions and must be recorded separately.

## 5. Definitions

| Term | Definition |
|---|---|
| Source | A job board, ATS endpoint, company career page, feed, or other provider from which a listing is retrieved. |
| Pilot connector | The one approved source integration used in Job Discovery v1. |
| Raw source record | The source payload or preserved source representation before ORBIT normalization. |
| Normalized job | An ORBIT job record mapped into the application's common field structure. |
| Source observation | A record of a posting as observed from a particular source at a particular retrieval time. |
| Search run | One user-initiated manual search, including criteria, start/end time, outcome, and result counts. |
| Stable source identifier | A provider-assigned identifier that reliably identifies a posting within that provider. |
| Idempotent persistence | Repeating retrieval of the same source posting does not create uncontrolled duplicate posting records. |
| Unknown | A value that the source does not provide or that ORBIT cannot verify. Unknown must not be silently converted into Yes or No. |

The terms **MUST**, **MUST NOT**, **SHOULD**, and **MAY** are used as normative requirement language.

## 6. User workflow

1. The user opens the Career Intelligence workspace.
2. The user enters a job title, role, or keyword query.
3. The user selects one or more target countries/locations from those supported by the source, or selects a broad search option if the pilot source supports it.
4. The user optionally chooses basic filters that the pilot source can reliably support.
5. The user starts a manual search.
6. ORBIT validates the request and displays a loading/searching state.
7. The backend invokes the approved pilot connector.
8. ORBIT preserves the retrieved source records and source metadata.
9. ORBIT maps valid records into the normalized job structure and records validation outcomes for invalid records.
10. ORBIT applies supported deterministic filters and persists the search run and records.
11. The UI displays the returned jobs with source attribution and original links.
12. The user can open the original listing at the source.
13. A later search for the same posting updates/records its observation without uncontrolled duplicate creation.

## 7. Functional requirements

### 7.1 Search request and validation

**FR-JD-001 — Manual search initiation**  
The system MUST allow the user to initiate a job search manually from the Career Intelligence workspace.

**FR-JD-002 — Role/query input**  
The system MUST accept free-text role, job-title, or keyword input. It MUST NOT restrict the user to a fixed list of role titles.

**FR-JD-003 — Country/location criteria**  
The system MUST accept country/location criteria supported by the pilot connector. The product direction remains worldwide; the interface and source status MUST distinguish requested coverage from the pilot connector's actual coverage.

**FR-JD-004 — Optional basic filters**  
The system MAY expose work arrangement, employment type, or other basic filters when the pilot source exposes compatible, reliable fields. A filter MUST NOT be presented as applied when the source cannot support it; the UI must explain any unsupported criterion.

**FR-JD-005 — Input validation**  
The system MUST reject an empty role/query and invalid or unsupported request values before invoking the connector. Validation errors MUST be understandable to the user.

**FR-JD-006 — Search-run record**  
The system MUST assign a unique identifier to each accepted search run and record its criteria, initiation time, completion time, status, result count, and error summary where applicable.

### 7.2 Source retrieval

**FR-JD-007 — Approved pilot source**  
The system MUST retrieve postings from exactly one selected pilot source for this slice. The source MUST be selected only after documenting its permitted access method, terms/permissions, rate limits, attribution requirements, and technical feasibility.

**FR-JD-008 — Permitted access**  
The connector MUST use an authorized access method. It MUST NOT bypass authentication controls, CAPTCHAs, paywalls, rate limits, or platform terms. If the source's permitted access conditions change, retrieval MUST be disabled or reviewed before continuing.

**FR-JD-009 — Source attribution**  
Each retrieved posting MUST retain the source name/provider identifier and the original posting URL, where supplied.

**FR-JD-010 — Retrieval timestamp**  
Each source observation MUST include the time ORBIT retrieved it. A provider's posted/updated timestamp MUST be stored separately and only when supplied by the provider.

**FR-JD-011 — Bounded retrieval**  
The connector MUST apply documented request limits and timeout behavior. It MUST NOT issue unbounded pagination or uncontrolled repeated requests.

**FR-JD-012 — Source failure handling**  
Timeouts, rate limits, provider errors, malformed responses, and connectivity failures MUST be converted into controlled search-run outcomes. Raw exception traces and secrets MUST NOT be shown in the UI.

### 7.3 Raw record preservation and normalization

**FR-JD-013 — Raw data preservation**  
The system MUST preserve the raw source record or an equivalent source representation sufficient to audit the normalized fields. It MUST preserve relevant retrieval metadata. Retention limits and sensitive-data handling are subject to the data governance decisions recorded in the HLD.

**FR-JD-014 — Normalized job structure**  
The system MUST map each accepted posting to a common normalized job structure. At minimum, the structure MUST support:

- ORBIT job record identifier
- source/provider identifier
- stable source posting identifier, when provided
- job title
- company/employer name
- location text and structured country/location values when available
- work arrangement when available
- employment type when available
- job description or source-provided summary when available
- original posting/application URL
- source-provided posted/updated timestamps when available
- first-seen and last-seen timestamps maintained by ORBIT
- source salary text and currency/period when provided
- source-provided sponsorship/visa text only when provided
- raw source record reference

Optional information MUST remain null/unknown when not supplied. The system MUST NOT fabricate or infer missing facts.

**FR-JD-015 — Required-field validation**  
A record MUST be rejected from the displayable normalized result set when it lacks the minimum fields required to identify and open a job posting (job title, employer/company where available under the source contract, and a valid original posting URL). The pilot-source mapping contract MUST define whether employer name is mandatory for that provider. Rejection reason and counts MUST be recorded without exposing unsafe raw data.

**FR-JD-016 — Optional-field handling**  
Missing optional fields MUST NOT cause an otherwise valid job to fail. The UI MUST display a neutral “Not provided” or omit the field rather than inventing a value.

**FR-JD-017 — Raw/normalized separation**  
Raw source data MUST remain distinguishable from normalized fields. A normalization change MUST NOT silently overwrite the preserved source evidence.

### 7.4 Filtering and persistence

**FR-JD-018 — Deterministic filtering**  
The system MUST use deterministic code to apply the supported search criteria. The first slice MUST NOT use an LLM to decide whether a listing matches the query.

**FR-JD-019 — Basic idempotency**  
The system MUST prevent repeated observations of the same posting from creating uncontrolled duplicate job records within the pilot source. It SHOULD prefer a stable source identifier. If none exists, the pilot integration MUST define and test a source-specific fallback identity key, such as a canonicalized posting URL. This requirement does not authorize fuzzy cross-source merging.

**FR-JD-020 — Observation history**  
The system SHOULD retain the first-seen and last-seen timestamps for each posting and record each source observation or an auditable update. Full duplicate-merge audit workflows are deferred to the Source Connector Framework slice.

**FR-JD-021 — PostgreSQL persistence**  
Accepted search runs, source observations, normalized job records, and validation/retrieval outcomes MUST be persisted in PostgreSQL. A successful UI response MUST only claim records were saved after the database transaction has committed.

**FR-JD-022 — Persistence failure**  
A database failure MUST produce a controlled error outcome. The UI MUST NOT report that results were saved when persistence did not succeed.

**FR-JD-023 — Repeatability**  
The same source response and criteria processed repeatedly MUST produce predictable normalized results and MUST NOT create uncontrolled duplicate records.

### 7.5 Results interface

**FR-JD-024 — Search status**  
The UI MUST communicate idle, validating, searching, completed, completed-with-record-issues, empty-results, and failed states as applicable.

**FR-JD-025 — Job result display**  
Each displayed result MUST show the job title, employer, location when available, source, original posting link, and relevant source dates when available.

**FR-JD-026 — Optional job attributes**  
Work arrangement, employment type, salary, and sponsorship/visa information MAY be displayed only when supplied by the source. Unknown values MUST remain visibly unknown or be omitted.

**FR-JD-027 — Source link behavior**  
The user MUST be able to open the original posting URL. External links MUST be handled safely and MUST NOT be replaced by an ORBIT-generated link that obscures the source.

**FR-JD-028 — Search result persistence**  
The user MUST be able to refresh the page and still retrieve persisted results for a completed search run, using the run identifier or an equivalent user-facing history mechanism.

**FR-JD-029 — Responsive layout**  
The workspace MUST be usable at desktop, tablet, and mobile browser widths. The first UI may prioritize desktop but MUST not become unusable on narrow screens.

**FR-JD-030 — Accessible interaction**  
Search controls, status messages, and result links SHOULD be keyboard accessible and use semantic labels. Errors MUST be associated with the relevant control where feasible.

### 7.6 Logging and operational behavior

**FR-JD-031 — Structured operational events**  
The backend MUST record structured events for search initiation/completion, connector outcome, validation counts, persistence outcome, and unexpected failures.

**FR-JD-032 — Sensitive-data minimization**  
Logs MUST NOT contain credentials, access tokens, secrets, or unnecessary personal information. Raw provider payloads MUST not be copied wholesale into ordinary application logs.

**FR-JD-033 — User-safe failure message**  
The interface MUST show a concise actionable message for connector or persistence failures and MUST keep implementation details out of end-user messages.

## 8. External interface requirements

### 8.1 Pilot source interface

The pilot connector's detailed interface depends on the source selected. Before implementation, a source decision record MUST capture:

- provider and job-board identity;
- official API/feed/ATS documentation or other permission basis;
- terms of use and permitted usage;
- authentication requirements and secret storage needs;
- rate limits, pagination behavior, and request constraints;
- geographical and job-category coverage;
- fields available and fields that are not available;
- source attribution and linking requirements;
- response examples/fixtures for automated tests;
- known limitations and operational risks.

### 8.2 Backend API

The backend SHOULD expose a versioned REST API. The initial API capability must support:

- submitting a manual search request;
- receiving a search-run identifier and current outcome;
- retrieving a search-run summary and its persisted results;
- receiving consistent validation and failure responses.

The exact paths, HTTP status codes, request/response Pydantic models, and pagination contract belong in the API/LLD design and must be documented before implementation is considered complete.

### 8.3 Database interface

PostgreSQL is the system of record for the persisted data in this slice. Database access MUST occur through the backend, not directly from the browser. Schema migration tooling and transaction boundaries will be defined in the HLD/LLD.

## 9. Data requirements

The first slice is expected to persist the following logical records. This is a requirements-level view, not the final relational schema.

| Logical record | Required purpose | Key information |
|---|---|---|
| SearchRun | Audit each manual search | Run ID, criteria snapshot, start/end time, status, counts, error summary |
| SourceObservation | Preserve what the provider returned | Source, retrieval time, source posting ID, raw record/reference, response metadata |
| Job | Provide the normalized posting used by the UI | ORBIT job ID, normalized fields, source identity, first/last seen, raw evidence reference |
| ValidationOutcome | Explain rejected or incomplete source records | Search run, source record reference, outcome, machine-readable reason |

The final schema must use appropriate constraints and indexes. It must preserve source-specific identity and avoid treating a source observation as proof that an application was submitted.

## 10. Non-functional requirements

**NFR-JD-001 — Maintainability**  
The code MUST be organized so retrieval, normalization, validation, persistence, API delivery, and UI presentation have clear responsibilities. The implementation SHOULD follow Ports and Adapters / Hexagonal Architecture principles without adding unnecessary abstraction layers.

**NFR-JD-002 — Testability**  
The connector MUST be replaceable by a deterministic fake in tests. Business rules MUST be testable without calling a live job source.

**NFR-JD-003 — Reliability**  
External source failures MUST NOT crash the application process. Search runs MUST end in an explicit success, partial/record-issues, empty, or failure state.

**NFR-JD-004 — Data integrity**  
Persistence operations MUST use database transactions and integrity constraints where appropriate. A failed transaction MUST not leave an inconsistent half-written search result.

**NFR-JD-005 — Security**  
Secrets MUST be stored outside source control and must not be embedded in frontend code. External content MUST be treated as untrusted input. User-visible errors and logs MUST be sanitized.

**NFR-JD-006 — Privacy**  
Only data needed for job discovery and traceability SHOULD be retained. The raw payload retention period and deletion/export behavior must be settled before any hosted deployment.

**NFR-JD-007 — Performance measurement**  
The application MUST provide immediate feedback that a search has started and MUST enforce source request timeouts. A numerical end-to-end latency target is intentionally left open until the pilot source and its observed response times are known; the target must then be baselined rather than guessed.

**NFR-JD-008 — Portability**  
The application MUST run locally using documented setup steps and environment configuration. Secrets and machine-specific paths MUST not be committed.

**NFR-JD-009 — Responsive usability**  
Core search and result-viewing workflows MUST remain usable in current desktop and mobile browsers.

**NFR-JD-010 — Observability foundation**  
The code SHOULD emit structured logs with a correlation/search-run identifier. Full distributed tracing, LangSmith, and OpenTelemetry rollout may follow in the observability phase.

## 11. Error and edge-case requirements

The implementation and tests MUST cover at least the following:

1. Empty role/query.
2. Unsupported or malformed country/location input.
3. Successful provider response with zero postings.
4. Provider response with missing optional fields.
5. Provider response with missing required fields.
6. Duplicate posting returned twice within one response.
7. Same posting returned in a later search run.
8. Invalid or missing original URL.
9. Provider timeout or connection failure.
10. Provider rate-limit response.
11. Unexpected provider response shape/schema change.
12. Database unavailable during persistence.
13. Browser refresh after a completed search.
14. Unsafe or malformed text in job title/description (must be rendered as text, not executable markup).
15. Source response containing malicious prompt-like instructions (must be treated as job content, not instructions to ORBIT).

## 12. Acceptance criteria

Job Discovery v1 is acceptable for its local MVP milestone when all of the following are demonstrated:

- **AC-001:** A user can submit a valid manual role/keyword search.
- **AC-002:** The selected pilot connector retrieves records through its documented permitted access method.
- **AC-003:** The system records the search criteria and search-run lifecycle.
- **AC-004:** Raw source evidence and retrieval metadata are preserved separately from normalized fields.
- **AC-005:** Valid records are normalized into the agreed common job structure.
- **AC-006:** Invalid records are rejected or quarantined with reason counts; they do not crash the whole search.
- **AC-007:** Missing optional fields do not invalidate otherwise valid postings and are never fabricated.
- **AC-008:** Supported deterministic criteria are applied consistently.
- **AC-009:** Jobs and search-run data are persisted in PostgreSQL and remain available after a page refresh.
- **AC-010:** Repeated observations of the same posting do not create uncontrolled duplicates within the pilot source.
- **AC-011:** The results screen shows title, employer, available location, source attribution, and original posting link.
- **AC-012:** Provider timeouts, rate limits, malformed responses, and database failures produce controlled outcomes and understandable messages.
- **AC-013:** Automated tests cover normal, boundary, and failure cases using fixtures/fakes; a routine test run does not depend on the live provider.
- **AC-014:** No LLM, autonomous application action, schedule, or unapproved scraping behavior is required or used.
- **AC-015:** Setup and test instructions are documented in the repository.

A local MVP milestone does not constitute production deployment. Internet-accessible hosting requires authentication, authorization, secrets management, transport security, and the other applicable security controls to be implemented and reviewed first.

## 13. Proposed implementation boundaries

The following is a provisional module boundary to guide architecture discussion, not a requirement to create every item as a separate package immediately:

- **Career search use case:** validates the request and coordinates a search run.
- **Pilot source adapter:** retrieves and maps provider-specific responses.
- **Normalization/validation:** converts source data into the common job model and records validation results.
- **Persistence adapter:** stores search runs, observations, normalized jobs, and outcomes in PostgreSQL.
- **API layer:** exposes the search and result retrieval operations.
- **Frontend workspace:** collects criteria and renders run state/results.

The application should remain a modular monolith. The source adapter boundary should make it possible to add further connectors in the later Source Connector Framework slice.

## 14. Open decisions before implementation

These are intentionally left open rather than guessed:

1. **Pilot connector:** Which single provider offers an appropriate permitted access method, useful coverage, stable identifiers or a safe identity fallback, and adequate fields?
2. **Search geography for the pilot:** Which initial country/location and query examples will be used for connector verification? This does not restrict the product's global ambition.
3. **Exact filter set:** Which optional filters can the pilot source reliably support without misleading the user?
4. **Raw-payload retention:** What raw source fields must be retained, for how long, and what deletion/export behavior applies?
5. **API contract:** Exact endpoints, response shapes, pagination, and synchronous execution limits.
6. **UI scope:** Whether the first screen also includes a lightweight search-run history list or only the most recent run plus a way to reopen a run.
7. **Measurable performance target:** Set after pilot measurements.
8. **Hosted-release security gate:** Confirm authentication provider and deployment security design before any public deployment.

A decision log should capture each resolved item with its rationale and date. The pilot connector must not be selected solely because it is popular; permission, documented access, coverage, data quality, reliability, and cost matter.

## 15. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Source does not permit the intended access | Verify official documentation and terms before building; stop if permission is unclear. |
| Source coverage is narrow or region-specific | Show actual pilot coverage; keep the connector boundary extensible. |
| Provider schema changes | Use fixtures, schema validation, controlled errors, and connector-specific tests. |
| Missing job fields | Preserve unknown values; reject only records that fail the defined minimum contract. |
| Duplicate postings | Enforce source-scoped idempotency; defer uncertain cross-source merges. |
| Prompt injection embedded in job text | Treat all external content as data; no LLM is used in this slice. |
| Secret leakage in a public repository | Use environment variables/secret storage; keep `.env` and credentials out of Git. |
| Early scope expansion | Enforce the out-of-scope list and deliver the vertical slice before adding schedules or AI. |

## 16. Traceability to the BRD and Blueprint

| Source requirement/theme | How Job Discovery v1 addresses it |
|---|---|
| Blueprint: Phase 1 - one permitted source pilot | One approved pilot connector, subject to source review. |
| Blueprint: preserve raw data, normalize, validate, filter, and save | FR-JD-013 to FR-JD-023. |
| Blueprint: preserve source evidence and source links | FR-JD-009, FR-JD-013, FR-JD-014, FR-JD-025 to FR-JD-027. |
| BRD: worldwide job-search ambition, honest actual coverage | FR-JD-003 and source-coverage handling. |
| BRD: broad source ecosystem, no unauthorized scraping | FR-JD-007 and FR-JD-008; further connectors deferred. |
| BRD: source-ID-first cautious deduplication | FR-JD-019; full cross-source matching deferred. |
| BRD: deterministic processing before LLM use | FR-JD-018; LLM use deferred. |
| BRD: local development, FastAPI/Pydantic, React/Vite, PostgreSQL direction | Sections 4 and 8. |
| BRD: quality, tests, security, and source provenance | Sections 10 to 12. |

## 17. Document approval and change control

This document is **Draft v0.1** and is ready for review. It becomes the implementation baseline only after explicit approval. Changes to scope or requirements after approval must be recorded in a new version and reflected in the repository's decision/status documentation.

| Review item | Status |
|---|---|
| Product Blueprint alignment | Drafted against the uploaded Blueprint |
| BRD alignment | Drafted against BRD v0.1 |
| Manual-search-first sequence | Confirmed by user on 31 October 2026 |
| Pilot connector selection | Open |
| API/DB detailed design | Open - belongs to HLD/LLD |
| User approval of this SRS | Pending |

---

## Appendix A — Learning outcomes paired with this slice

The product requirements above define what the software must do. The following concepts will be taught as the implementation is designed and built, before introducing code for each area:

1. Requirement decomposition, use cases, acceptance criteria, and traceability.
2. Python domain models, type hints, validation, and error handling.
3. Functions, collections, normalization, idempotency, and algorithmic complexity.
4. HTTP, REST, request/response contracts, and FastAPI fundamentals.
5. Ports and Adapters / Hexagonal Architecture and dependency inversion.
6. PostgreSQL fundamentals, relational modelling, constraints, indexes, and transactions.
7. Unit vs integration vs API tests, fixtures, fakes, and test design.
8. Git commits, reviewable milestones, documentation, and local deployment practices.

We will implement one small requirement at a time. You will write the code first; I will review it and provide hints before giving a complete implementation unless you request one.
