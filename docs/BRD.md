# PIYVIAN ORBIT — Business Requirements Document (BRD)

**Product:** PIYVIAN ORBIT  
**Company:** PIYVIAN TECHNOLOGIES  
**Tagline:** One command center. Your world, in orbit.  
**Document status:** Draft v0.1 — discovery decisions consolidated  
**Date:** 31 October 2026  
**Primary product reference:** `PIYVIAN_ORBIT_Product_Blueprint_SRS_HLD_SDLC_Roadmap.pdf` (Draft v0.1, 27 October 2026)

> This BRD records the product direction and discovery decisions gathered so far. It is not yet the detailed SRS, HLD, security design, data model, or implementation plan. Items that require detailed rules, measurable thresholds, source-by-source feasibility checks, or technical design remain open for those later documents.

---

## 1. Executive Summary

PIYVIAN ORBIT is envisioned as a Personal AI Operating System that brings professional, personal, learning, and business workflows into one coordinated platform. A central Supervisor / Orchestrator routes work to specialist agents. Each specialist has a dedicated workspace, while shared context, permissions, workflow state, approvals, and audit history are governed centrally.

The first usable release is a **personal-use MVP** for the product owner. The architecture should preserve a path to invited users, organizations, teams, and future subscription SaaS without implementing multi-user complexity prematurely.

The first implementation focus is **Career Intelligence**, supported by Application Tracker, Resume Intelligence, and a connection to Learning Coach. The complete specialist-agent vision remains in scope for the long-term product and must not be discarded.

The product is intended to be a cloud-hosted, responsive web application, developed locally first and initially deployed using suitable free tiers where practical. Future native Android and iOS applications are planned after the responsive web experience.

ORBIT's agents should improve over time through explicit feedback, measured outcomes, evaluation datasets, controlled experiments, human-approved releases, monitoring, and rollback. They must not silently rewrite production code, expand their own permissions, or deploy arbitrary changes.

## 2. Product Vision and Objectives

### 2.1 Vision

Build one command center where a user can coordinate professional, personal, learning, and business activities through specialized AI agents under clear human control.

### 2.2 Product objectives

1. Provide a unified Command Center for natural-language requests and cross-agent coordination.
2. Provide dedicated workspaces for every specialist agent in the product vision.
3. Establish Career Intelligence as the first complete, useful workflow and a foundation for later agents.
4. Give users control over agent permissions, autonomy, approvals, data, memory, and feedback.
5. Preserve evidence, source attribution, and audit history for important results and actions.
6. Improve agent quality through governed evaluation and release practices.
7. Build a maintainable, secure, observable product that can evolve from personal use into a multi-user SaaS.
8. Teach and apply professional software engineering and Agentic AI engineering throughout development.

### 2.3 Product principles

- Plan the full product; implement and validate one module at a time.
- Start with a modular monolith; avoid premature microservices and Kubernetes.
- Use deterministic Python services for validation, filtering, deduplication, calculations, and state transitions.
- Use LLMs for language understanding, extraction, drafting, summarization, and reasoning where they provide measurable value.
- Use explicit workflows and state management for multi-step tasks.
- Require human approval for consequential external actions.
- Keep raw source evidence separate from normalized application data.
- Treat external job descriptions, emails, documents, and user-supplied content as untrusted input.
- Apply least privilege, data isolation, privacy controls, budget limits, testing, observability, and rollback.
- Adopt technology when it solves a requirement; do not add frameworks merely for appearance.

## 3. Users, Release Strategy, and Business Direction

### 3.1 Initial users

- **Initial release:** Product owner only (personal-use MVP).
- **Future direction:** Invited users, individuals, organizations, and teams.
- **Future SaaS:** Role-based access, workspace isolation, and subscription plans with usage limits and feature tiers.

### 3.2 Product access

- Responsive web application for desktop, tablet, and mobile browsers in the first release.
- Future native Android and iOS applications.
- English interface initially; additional interface languages may be introduced as the product evolves.
- Job listings may be processed in multiple languages, with language detection and translation support where feasible.

### 3.3 Hosting and cost direction

- Develop and test locally before deploying.
- Target free-tier cloud infrastructure for the early MVP where limits and reliability are acceptable.
- Treat free tiers as a cost-conscious starting point, not a guarantee of production-grade availability.
- Permit later upgrades when usage, data durability, reliability, security, or performance requires them.
- Provide global and per-agent AI usage budgets, alerts, and limits.

## 4. Complete Specialist-Agent Catalogue

The following catalogue preserves the full Product Blueprint vision.

1. **Supervisor / Orchestrator** — Understand user intent, route requests, coordinate agents and workflows, manage shared context, and enforce permissions and approvals.
2. **Career Intelligence** — Discover global job opportunities, manage search profiles, assess fit and eligibility, explain matches, and support career decisions.
3. **Application Tracker** — Track application lifecycle, evidence, communications, interviews, reminders, and history.
4. **PIYVIAN Client Agent** — Manage the client lifecycle, including prospecting, company research, CRM, outreach drafts, proposals, negotiation tracking, and relationships.
5. **Content / Social Media Agent** — Research, draft, organize, calendar, and prepare content for major social platforms, with approval before publication.
6. **Learning Coach** — Deliver adaptive learning paths, lessons, exercises, quizzes, DSA practice, code review, projects, skill-gap analysis, and interview preparation.
7. **Business Ideas Research Agent** — Research problems and market signals across industries worldwide, analyze competitors, and support idea validation and opportunity assessment.
8. **Finance Agent** — Support expense and budget tracking, statement imports, reports, savings insights, and authorized financial integrations; transactions require approval.
9. **Personal / Family Health Assistant** — Organize consent-based, separately protected profiles, health records, appointments, and reminders. It is not an autonomous diagnostic or treatment system.
10. **Property Assistant** — Support buying, selling, and renting research, listings, comparables, contacts, viewing tasks, and draft offers; commitments require approval.
11. **Personal Planner** — Coordinate tasks, calendars, deadlines, priorities, briefings, reminders, and approved external calendar integrations.
12. **Admin Studio** — Govern agent registry, versions, tools, skills, MCP servers, plugins, model providers, permissions, budgets, evaluations, observability, releases, and rollback.

A product capability does not automatically need to be a separate agent. A module may be a deterministic service, workflow, agent, or combination, depending on its responsibility.

## 5. Global Product Experience

### 5.1 Application shell

The web application should use a consistent shell with:

- Persistent navigation to Home / Command Center and specialist workspaces.
- Global search and natural-language command entry.
- Workspace and user profile controls.
- Notifications and pending-approval indicators.
- Global Tasks and Approvals access.
- Activity and History access.
- Settings and Admin Studio access according to role.

### 5.2 Command Center

The central AI Command Center should:

- Accept natural-language requests.
- Route intent through the Supervisor / Orchestrator.
- Show suggested actions, priorities, tasks, pending approvals, agent activity, and recent outputs.
- Explain which agent is working and the current workflow status.
- Preserve useful conversation and workflow context subject to retention and privacy controls.

### 5.3 Dedicated agent workspaces

Users must be able to open a specialist workspace directly as well as request work through the Command Center.

### 5.4 Global search

Provide global search across supported jobs, applications, documents, tasks, conversations, and agent outputs, subject to user permissions and data scope.

### 5.5 Dashboard and themes

- Allow configurable/rearrangeable dashboard widgets.
- Support light and dark themes, with automatic system-theme detection.
- Maintain text-based interaction and accessibility when voice features are available.

### 5.6 Voice interaction

Plan for voice input and spoken responses, while keeping text interaction available. Detailed provider, privacy, recording, and retention rules belong in the SRS and privacy design.

## 6. Career Intelligence — First Implementation Module

### 6.1 Global job-search coverage

Career Intelligence should be designed for worldwide job search, with no permanent country restriction. Users should be able to search any country and select multiple countries where desired.

The product must distinguish the ambition of worldwide coverage from actual connector coverage. Results can only be supplied from sources ORBIT can lawfully and technically access. The system must not claim universal coverage when sources are unavailable or incomplete.

### 6.2 Job titles and skills

Support the four initial target categories identified in the Product Blueprint:

- Backend / Software Engineer
- AI / Python Engineer
- Full-stack Engineer
- GenAI / Agent Engineer

Also support user-defined job titles, role keywords, and skills without restricting users to a fixed catalogue. Examples include Python Developer, .NET / C# Developer, Java Developer, React Developer, DevOps Engineer, Software Developer, and other titles users enter.

The role and skill catalogue must be extensible. Learning Coach may recommend skills based on relevant job-market evidence, but learning progress must not automatically be represented as professional proficiency.

### 6.3 Experience levels

Support all five levels, with multi-selection:

- Fresher / Entry-level
- Junior
- Mid-level
- Senior
- Lead / Principal / Architect

### 6.4 Work arrangement and employment type

Support multiple selections for work arrangement:

- On-site
- Hybrid
- Remote

Support multiple selections for employment type:

- Full-time
- Part-time
- Contract
- Internship
- Freelance
- Temporary
- Apprenticeship

Relocation preferences should also be configurable.

### 6.5 Country, work authorization, and sponsorship

- Provide a searchable global country selector.
- Allow users to record countries where they have work authorization and relevant restrictions or permit details, including expiry information where applicable.
- Keep the user's authorization status distinct from the employer's sponsorship offering.
- Do not make legal eligibility assumptions or provide unsupported guarantees.
- Provide a dedicated sponsorship filter with options: All, Yes / confirmed, No sponsorship, and Unknown / not verified.
- Preserve supporting source evidence for sponsorship claims.

### 6.6 Salary preferences

Support:

- Minimum and maximum salary.
- Selectable currencies (examples include INR, USD, EUR, GBP, AED, and others as relevant).
- Hourly, monthly, and annual periods.
- An option to hide jobs where salary is not disclosed.
- Preservation of the original source salary value, currency, and period where available.

Salary normalization and currency conversion rules require detailed SRS decisions; the original source value must remain available.

### 6.7 Master Career Profile

Maintain one Master Career Profile reused by multiple saved job-search profiles. Profile creation should support:

1. Resume upload and information extraction.
2. Manual entry through guided forms.
3. Review, edit, and explicit approval before extracted details are used.

Profile sections should include optional fields for:

- Personal and contact information.
- Education.
- Professional experience.
- Projects and achievements.
- Technical and soft skills.
- Certifications.
- Languages.
- GitHub, LinkedIn, and portfolio links.
- Work authorization and visa information.
- Career preferences.

Skills must have distinct states such as **Learning**, **Self-reported**, and **Verified**. The meaning and evidence requirements for Verified must be defined in the SRS.

### 6.8 Multiple saved job-search profiles

Allow multiple independent saved search profiles, each with its own:

- Job titles and skills.
- Countries and relocation preferences.
- Work arrangements and employment types.
- Experience levels.
- Salary range, currency, and period.
- Sponsorship filter.
- Matching priorities and minimum match threshold.
- Sorting preference.
- Search schedule and alert preferences.

All profiles reuse the Master Career Profile rather than duplicating career facts.

### 6.9 Job discovery modes and schedules

- Support manual searches at any time.
- Support scheduled automatic searches.
- Default automatic schedule: once daily.
- Allow configurable schedules, including every few hours, daily, weekly, or manual-only.
- Surface newly discovered matching jobs through in-app and email notifications, subject to user settings.
- Repeated runs must not create uncontrolled duplicate listings.

### 6.10 Job-source ecosystem

Target a broad, extensible source ecosystem that may include:

- Major global job portals and specialist job boards.
- Remote-work platforms.
- Company career pages.
- ATS job-board endpoints, including Greenhouse, Lever, Ashby, and other supported platforms.
- Government, university, and public-sector portals where accessible.
- Authorized APIs, RSS / Atom feeds, and licensed aggregators.
- Job-alert emails from connected Gmail and Outlook accounts.
- User-submitted job links and manually entered job opportunities.
- User-submitted job-board and company-career URLs, evaluated for a permitted integration method.

Build a Source Connector Registry rather than hardcoding individual sites into Career Intelligence. Each connector should eventually expose configuration, permissions, coverage, health, last-sync time, error information, and source attribution.

Source prioritization must consider coverage, reliability, permissions, and cost. No guarantee should be made that every job listing or every provider can be accessed. Do not bypass access controls, CAPTCHAs, rate limits, paywalls, or platform terms. Source feasibility, attribution, rate limits, and retention rules must be reviewed individually.

### 6.11 Job ingestion, normalization, and deduplication

The intended flow is:

1. Run a permitted source connector.
2. Preserve the raw source record and metadata.
3. Normalize into a common job schema.
4. Validate required and optional fields.
5. Deduplicate cautiously.
6. Apply deterministic filters.
7. Rank results transparently.
8. Optionally apply LLM analysis to shortlisted jobs where it adds value.
9. Store source evidence and show the original source and application link.

Deduplication requirements:

- Prefer stable source IDs when available.
- Otherwise use cautious matching based on normalized company, title, location, and original URL.
- Keep raw data separate from normalized fields.
- Maintain an audit trail for potential duplicate merges.
- Do not silently merge uncertain records.

### 6.12 Matching, ranking, and sorting

Provide an explainable ORBIT match estimate using relevant factors such as:

- Role and skills.
- Experience and seniority.
- Location and work arrangement.
- Salary preferences.
- Work authorization and sponsorship evidence.

Users must be able to customize the importance of matching factors and set a minimum match threshold, or choose to see all jobs. Match scores must be presented as ORBIT estimates, not probabilities of being hired or guarantees of suitability.

Provide sorting options:

- Best Match (default).
- Newest First.
- Salary.
- Experience Match.

Sorting must remain distinct from the match score. The detailed formula, calibration, missing-data treatment, and evaluation metrics will be defined in the SRS.

### 6.13 Job listing actions

For discovered jobs, users should be able to:

- Save.
- Shortlist.
- Mark Not Interested.
- Compare multiple jobs.
- View job details and evidence.

### 6.14 Job lifecycle and freshness

Support listing statuses:

- ACTIVE
- STALE
- CLOSED
- EXPIRED

Show first-discovered and last-verified timestamps. Confirmed expired or closed listings should stop appearing in active recommendations. Previously saved jobs and application history must be preserved; application records must not be deleted merely because a posting disappears.

The rules and time windows that determine STALE, CLOSED, and EXPIRED require SRS definition.

### 6.15 Resume Intelligence

Support:

- PDF, DOCX, and LaTeX resume uploads.
- Extraction of skills, education, projects, and experience.
- User review and approval of extracted profile data.
- Job-specific resume tailoring and cover-letter drafting.
- Multiple role-specific resume versions and version history.
- PDF and editable `.tex` export.
- Explainable match, readability, and readiness feedback.

Any resume score must be labelled as an ORBIT estimate. ORBIT must not claim to calculate the true score used by an employer's ATS.

### 6.16 Application submission

- Manual submission is the default.
- ORBIT may support an approved submission workflow only where an authorized integration permits it.
- Each application submission requires explicit user approval.
- Platform restrictions must be respected; no bypassing site protections.
- Record reliable confirmation evidence before marking an application APPLIED.

### 6.17 Application Tracker

Support manual tracking and evidence-based event detection from connected mailboxes.

Statuses include:

- DISCOVERED
- MATCHED
- SHORTLISTED
- READY_FOR_REVIEW
- APPLIED
- INTERVIEW
- REJECTED
- OFFER
- WITHDRAWN
- CLOSED
- STALE
- NEEDS_REVIEW for ambiguous detected events

A discovered or shortlisted job must never become APPLIED without reliable submission evidence. Application events should retain event time, detection time, source, supporting message or job ID, confidence, parser version, and any review decision. Ambiguous events must be presented for review rather than silently changing status.

### 6.18 Email integration

Plan Gmail and Microsoft Outlook integrations with explicit mailbox permissions. Detect and classify relevant events, including:

- Submission acknowledgements.
- Interview invitations.
- Rejection notifications.
- Employer updates and offers.

Email-derived events should include supporting evidence and confidence. Uncertain events go to NEEDS_REVIEW. Mailbox access and retention must be configurable and revocable.

### 6.19 Notifications and reminders

Provide in-app notifications and email alerts, configurable independently by the user.

Support reminders for:

- Interview dates and preparation.
- Application follow-ups.
- Application deadlines.
- Pending tasks and missing documents.

Reminder timing and delivery preferences require SRS details.

### 6.20 Career data ownership

Users must be able to:

- Export career data.
- Download resumes and generated documents.
- Delete individual records.
- Delete the complete Career Profile and associated data.
- Control access granted to connected services.

Deletion must account for derived data, indexes, backups, and retention obligations; detailed deletion semantics belong in the privacy and SRS design.

## 7. Learning Coach and Career Feedback Loop

The Learning Coach should support:

- Structured learning paths.
- Lessons and learning resources.
- Exercises and quizzes.
- DSA practice in Python.
- LLD, HLD, system design, and Agentic AI learning.
- Code review and project-based learning.
- Interview preparation.
- Skill-gap analysis based on relevant job requirements.
- Progress tracking and adaptive recommendations.

Career Intelligence may identify commonly requested skills from relevant jobs and pass evidence-backed gaps to Learning Coach. Learning progress must remain distinct from verified professional experience. A skill should only be promoted to a stronger profile state through an explicit user update or a defined verification process.

## 8. Cross-Agent Requirements and Remaining Specialist Agents

### 8.1 PIYVIAN Client Agent

Support the complete client lifecycle: prospecting, leads, contacts, CRM, company research, follow-ups, outreach drafts, proposals, negotiation tracking, and relationship management. Sending outreach or making commitments requires the applicable approval.

### 8.2 Content / Social Media Agent

Support major social platforms through a common content calendar and workflow. Prepare content research, drafts, previews, and schedules. No public content is published without explicit approval. Actual platform coverage depends on authorized APIs and integrations.

### 8.3 Business Ideas Research Agent

Research problems and market signals worldwide across any industry. Support hypothesis creation, competitor analysis, validation experiments, and evidence-backed opportunity assessment. Avoid presenting uncertain research as fact.

### 8.4 Finance Agent

Support manual expense entry, CSV and bank-statement imports, budgets, reports, savings goals, and financial insights. Authorized integrations may be added where available. Insights must be distinguished from financial transactions. Transactions require explicit approval.

### 8.5 Personal / Family Health Assistant

Support personal and family profiles with separate consent and data isolation. Organize records, documents, appointments, and reminders. It must not autonomously diagnose, prescribe, or change treatment.

### 8.6 Property Assistant

Support buying, selling, and renting research, listing comparisons, comparables, contact management, viewing tasks, and draft offers. No property commitment or offer is made without approval.

### 8.7 Personal Planner

Support tasks, priorities, deadlines, recurring tasks, calendars, daily briefings, reminders, and external calendar integrations. Coordinate with other agents under permission controls.

### 8.8 Admin Studio

Provide an owner-only administration experience initially, designed for future role-based administration. Capabilities include:

- Agent registry and identity.
- Purpose, version, and input/output schemas.
- Allowed tools and tool permissions.
- Model policy and provider configuration.
- Memory and data scope.
- Per-agent budgets and usage limits.
- Evaluation datasets and results.
- Approval and autonomy policy.
- Health, error, and performance monitoring.
- Change history, controlled release, and rollback.
- MCP server, skills, plugin, integration, RAG source, and model registries.

Future organization and SaaS roles require workspace isolation and role-based access control.

## 9. Shared Agent Intelligence, Memory, and Self-Improvement

### 9.1 Shared intelligence infrastructure

Provide shared knowledge infrastructure without unrestricted cross-agent access. Access must be controlled by user permissions, agent scope, data sensitivity, and future tenant/workspace boundaries.

Agents may communicate through the Supervisor and, where justified, directly through governed message contracts. Direct communication must not bypass permission checks, approval policy, audit logging, or workflow controls.

### 9.2 Memory categories

Maintain distinct concepts for:

- Workflow and checkpoint state.
- User preference memory.
- Structured application/product records (database as source of truth).
- Approved knowledge and RAG documents.
- Evaluation history and outcomes.

Users should be able to view, edit, and delete remembered preferences. Retention and expiry rules must be defined for workflow state. Source, owner, timestamp, permissions, and version must be retained for indexed knowledge.

### 9.3 Self-improvement lifecycle

The target lifecycle is:

1. Collect explicit user feedback and consented, verified outcomes.
2. Create or update evaluation examples.
3. Compare candidate prompt, model, tool, retrieval, or ranking versions.
4. Run quality, safety, regression, privacy, latency, and cost checks.
5. Require approval before releasing behavior changes.
6. Monitor the released version.
7. Roll back when quality or safety regresses.

The system may propose changes to prompts, model settings, tools, skills, retrieval, and ranking logic. Production code changes remain subject to normal Git review, testing, and deployment practices. Agents must not self-deploy arbitrary code or grant themselves permissions.

### 9.4 Feedback and model-training consent

Users should be able to:

- View feedback and activity used for agent improvement.
- Correct or delete inaccurate feedback.
- Enable or disable learning from their activity.
- Separately consent to use of their data for model training or fine-tuning.

Preference learning, prompt/ranking improvement, and model training are separate activities and must have separate controls and records. Sensitive personal, career, financial, health, family, and property data must not automatically become model-training data.

### 9.5 Model routing

Support a hybrid model strategy with hosted and local/open-source models. Model selection should be routed according to task quality, complexity, privacy, latency, and cost. Support per-task and per-agent model policies, fallback behavior, and global/per-agent budgets. The exact providers and models will be selected through technical evaluation rather than hardcoded as permanent choices.

## 10. Agent Autonomy and Approval Governance

### 10.1 Autonomy levels

Each agent should support configurable autonomy levels:

1. **Assist:** Analyze, recommend, and draft; the user performs external actions.
2. **Approved execution:** Execute an action only after explicit user approval.
3. **Bounded autonomy:** Perform predefined low-risk tasks automatically within permissions, budgets, and limits.

Agents cannot increase their own autonomy level or permission scope.

### 10.2 Consequential actions

Human approval remains required for consequential actions, including:

- Job application submissions.
- Client outreach and external commitments.
- Public content publication.
- Financial transactions.
- Property offers or commitments.

The final action policy and risk categories will be specified in the SRS and security design.

### 10.3 Central Approval Center

Provide a single Approval Center for requests from all agents. Each approval request must show:

- Requesting agent and workflow.
- Proposed action and intended target.
- Reason and relevant context.
- Supporting evidence.
- Permissions requested or used.
- Risk and consequence summary.
- Approve, Reject, and Request Changes actions.

Record the decision and actor in audit history. An approval applies only to the specific action and scope shown; it must not be treated as broad or indefinite consent.

## 11. Technology Direction and Learning Scope

Technology choices are intended direction and require validation during architecture and implementation. Do not treat this list as a requirement to introduce every tool in the first release.

- **Backend:** Python, with FastAPI and Pydantic evaluated for API and schema validation.
- **Frontend:** React and Vite for the responsive web application.
- **Database:** PostgreSQL locally and in cloud environments.
- **Agent building blocks:** LangChain.
- **Stateful workflows and orchestration:** LangGraph.
- **Complex long-running agent harness:** Deep Agents, used where planning, subagents, and context management justify it.
- **Observability and evaluation:** LangSmith and vendor-neutral OpenTelemetry; evaluate MLflow alternatives where useful.
- **Interoperability:** Model Context Protocol (MCP), plus governed tools, skills, and plugins.
- **RAG and embeddings:** Add when approved-document retrieval is required; evaluate PostgreSQL with pgvector before introducing a separate vector database.
- **Open-source ML ecosystem:** Hugging Face Transformers, Datasets, Evaluate, Sentence Transformers, and PEFT/LoRA where justified.
- **Local models:** Evaluate Ollama or other runtimes according to hardware, privacy, quality, latency, and cost.
- **Classical ML:** Consider ranking/model improvements only when enough validated feedback data exists.
- **Testing:** pytest and appropriate frontend/API testing tools.

Learning objectives alongside product delivery include Python, DSA in Python, OOP, SOLID, design patterns, dependency injection, Hexagonal Architecture / Ports and Adapters, Clean Architecture, modular monolith design, SQL, system design, LLM engineering, ML fundamentals, RAG, vector search, MCP, agent orchestration, evaluations, security, deployment, and operations.

## 12. Security, Privacy, and Data Governance

The product must be designed for sensitive personal information from the beginning, even while the initial release is single-user.

Requirements include:

- Authentication using email/password and Google sign-in (subject to provider feasibility).
- Authorization and least-privilege permissions.
- Separation of user, agent, and future workspace/tenant data.
- Secure secrets handling; secrets and `.env` files must never be committed to Git.
- Encryption in transit and appropriate encryption at rest.
- Revocable integration access and scoped credentials.
- Human approval for consequential actions.
- Audit records for important actions, approvals, tool calls, and data changes.
- Treat job descriptions, web pages, emails, documents, and tool responses as untrusted input; guard against prompt injection and unsafe tool instructions.
- Redact secrets and sensitive personal data from logs and traces.
- Separate consent for feedback use and model training.
- User export and deletion capabilities.
- Backup, restore, and disaster-recovery procedures.
- Security and AI safety testing, including prompt-injection and excessive-agency scenarios.

Health, finance, career, family, and property information must have appropriate access boundaries and retention policies. The system must not make unsupported legal, medical, financial, or employment claims.

## 13. Reliability, Quality, and Operational Requirements

The target quality strategy includes:

- Controlled retries, timeouts, and fallback behavior.
- Resumable workflows and checkpointing where appropriate.
- Clear failure reporting and human escalation.
- Automated backups, restore testing, data export, and recovery procedures.
- Unit, integration, API, end-to-end, security, AI evaluation, performance, and regression tests.
- Structured logging, traces, metrics, and cost/latency monitoring.
- Source and result provenance.
- Accessible, responsive, keyboard-navigable interfaces and clear feedback.
- Model and AI workflow evaluations with regression datasets.

Numeric service-level objectives, recovery objectives, latency targets, retention periods, and cost budgets are not yet set. They must be measured and baselined in the SRS/HLD rather than invented in this BRD.

## 14. Delivery Strategy and Phasing

### Phase 0 — Discovery and engineering setup

- Consolidate product and business requirements.
- Baseline Career Intelligence SRS.
- Create repository conventions, documentation, and architecture decisions.
- Establish local development environment and repeatable tests.

### Phase 1 — Job discovery v1

- Implement one permitted job-source connector as a pilot.
- Normalize, filter, and save records.
- Preserve source links and evidence.
- Test normal and failure cases.

The pilot is not a permanent limit on source coverage.

### Phase 2 — Source framework

- Build connector contracts and registry.
- Add more permitted sources.
- Establish common schema, cautious deduplication, and configurable role/country filters.

### Phase 3 — Tracker and persistence

- Persist jobs and application records.
- Add state history, evidence, and reminders.
- Enforce evidence-based status transitions.

### Subsequent phases

- Backend API and UI.
- Master career profile and explainable matching.
- First LLM use case.
- Resume Intelligence.
- RAG and semantic retrieval where justified.
- LangGraph workflows and approvals.
- MCP and authorized integrations.
- LangSmith/OpenTelemetry, evaluations, scheduling, and operations.
- Admin Studio and governed improvement lifecycle.
- Remaining specialist agents.
- SaaS readiness, organization/workspace isolation, and subscription controls.

Exact phase boundaries may be refined in the SRS and roadmap, but the complete agent catalogue and product vision must remain preserved.

## 15. Business-Level Acceptance Criteria

The product direction will be considered correctly represented when:

1. The complete specialist-agent catalogue is preserved.
2. The first usable release is personal-use, while future multi-user SaaS is architecturally considered.
3. Users can create multiple job-search profiles that reuse one Master Career Profile.
4. Job search supports global country selection, configurable roles/skills, work arrangements, employment types, experience levels, salary, sponsorship, and authorization preferences.
5. Actual source coverage and restrictions are shown honestly.
6. Job results preserve source attribution and original application links.
7. Job matching is explainable and does not claim hiring probability.
8. Sponsorship and eligibility are distinct, evidence-backed, and not guessed.
9. Job deduplication preserves raw records and audits uncertain merges.
10. Application statuses are evidence-based; a job is never marked APPLIED without submission evidence.
11. Resume extraction requires review; resume scores are not represented as the employer's true ATS score.
12. Consequential actions require explicit approval.
13. Agent memory and shared knowledge respect permissions and scope.
14. Agent improvement uses evaluations, approval, monitoring, and rollback.
15. Sensitive data is not automatically used for model training.
16. The system provides data export, deletion, permission controls, and auditability.
17. Quality and operational behavior are tested across software and AI workflows.

## 16. Open Items for the SRS and HLD

The following are intentionally not fully specified in this BRD:

- Detailed Career Profile fields, validation, and evidence rules.
- Exact role/skill taxonomy and matching formula.
- Eligibility logic by country and the boundary between system facts and legal advice.
- Sponsorship evidence definitions and source-of-truth hierarchy.
- Job-source-by-source access feasibility, rate limits, attribution, coverage, and connector priority.
- Job normalization schema, stable IDs, fuzzy matching thresholds, and duplicate-merge review behavior.
- Salary normalization and currency conversion behavior.
- Exact stale/closed/expired determination rules.
- Application state-transition table and evidence schema.
- Gmail/Outlook scopes, consent, event parsing, retention, and NEEDS_REVIEW workflow.
- Resume extraction, template management, scoring methodology, and export details.
- Reminder scheduling, notification delivery, and retry policy.
- Shared memory data model, access filtering, expiry, deletion, and RAG indexing policy.
- Agent message contracts, supervisor routing, and direct agent-to-agent authorization.
- Model/provider selection, routing policy, evaluation datasets, and budget values.
- Self-improvement approval roles and release criteria.
- Authentication, authorization, encryption, logging, retention, backup, and recovery details.
- Measurable availability, performance, latency, recovery, accessibility, and cost objectives.
- Organization/workspace model and subscription tiers for future SaaS.
- Mobile app implementation strategy and voice interaction providers.

## 17. Document Governance

- This document is a draft BRD v0.1 based on the Product Blueprint and discovery decisions recorded through 31 October 2026.
- Decisions are considered confirmed only where explicitly accepted in the discovery conversation.
- Detailed implementation choices must be documented in the SRS, HLD, or Architecture Decision Records (ADRs).
- Changes to the product vision or confirmed requirements should be recorded with rationale and impact.
- Update `docs/status.md` after meaningful project milestones.
- Do not mark any feature implemented, tested, or deployed merely because it appears in this BRD or in a visual design concept.

---

**End of BRD Draft v0.1**
