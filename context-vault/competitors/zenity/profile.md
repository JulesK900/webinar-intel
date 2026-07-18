# Competitor — Zenity

Source: [salt.security/vs-zenity](https://salt.security/vs-zenity)

## Who they are

Zenity is a cybersecurity company based in Tel Aviv, Israel, founded in 2020 by former Microsoft cloud security veterans Ben Kliger and Michael Bargury. They provide an agentic AI security platform focused on continuous discovery, posture management, and runtime threat detection for enterprise AI agents, copilots, and low-code/no-code applications. Their ICP includes large enterprises — particularly Fortune 500 companies in financial services, consulting, and technology — that are heavily adopting SaaS automation ecosystems, custom cloud AI frameworks, and endpoint coding assistants. They are backed by Microsoft's M12 venture arm and purpose-built for observing and governing agent activity across SaaS and endpoint environments, especially the Microsoft stack (M365 Copilot, Azure AI Foundry, Teams agents).

## Pillars they lean on

- **Observe (AI Observability)** — Discover and inventory AI agents across all platforms with clear insight into ownership, permissions, integrations, and runtime behavior.
- **Govern (AISPM)** — Apply secure-by-design policies to agent configurations, permissions, tool access, and memory before deployment.
- **Defend (AIDR)** — Monitor step-level agent execution, correlate behavior with context, and enforce inline controls to stop unsafe actions in real time.

## Positioning language they use

- Taglines: "Secure AI Agents Everywhere", "Purpose-Built to Secure How Enterprises Actually Operationalize AI"
- Category names they push: AI Agent Governance, AISPM, AIDR
- Signature phrases: "Intent-based detection", "From buildtime to runtime", "Defense-in-Depth for AI Agents", "Step-level behavioral monitoring"

## What Zenity does well (steelman)

- Deep, native coverage of agent activity inside the Microsoft ecosystem — M365 Copilot, Azure AI Foundry, Teams agents — plus other supported enterprise SaaS (Salesforce, ServiceNow, ChatGPT Enterprise).
- Step-level agent behavior analysis and incident correlation across identity and posture signals.
- Agentic browser coverage via device agent.
- Genuinely valuable governance for organizations heavily concentrated in Microsoft's stack.

## Head-to-head comparison

| Capability | Salt | Zenity |
|---|---|---|
| AI Observability and LLM Monitoring (discovery, posture, behavioral detection) | Yes | Yes |
| Full API Fabric Coverage (all APIs, any platform/framework) | Yes | No |
| Agentic Security Graph (LLM, MCP, API, identity correlation) | Yes | No |
| Unified Agentic Discovery (APIs, MCP servers, AI assets across exposure, cloud, code, runtime) | Yes | No |
| Salt Code Governance (governs API/MCP creation in repos/PRs pre-production) | Yes | No |
| Runtime-to-Code Remediation (runtime findings feed back into dev workflows) | Yes | No |
| Agent-Aware Sequence Correlation (multi-step intent across sessions/tools/services) | Yes | No |
| Behavioral Action-Layer Protection (machine-speed business-logic abuse detection) | Yes | No |
| Internal & East-West Coverage | Yes | No |
| Action-Layer Data Security (sensitive data mapped across APIs/MCP/agent actions) | Yes | No |
| Platform-Agnostic Agentic Coverage (LangChain, CrewAI, Databricks, custom agents) | Yes | No |
| No Device Agent Required | Yes | No (requires device agent for endpoint visibility) |

## Where they don't overlap

- **API fabric depth:** Zenity focuses on monitoring the agent's intent inside the host SaaS platform but stops at the agent boundary; no deep API fabric security or destination-endpoint monitoring for underlying business logic abuse.
- **Audit defensibility:** Operational runtime/monitoring tool, not an evidence platform; no cryptographically signed, deterministic audit replays for long-term regulatory compliance.
- **Traffic-layer enforcement:** Architecture relies on native SaaS API integrations and endpoint agents rather than an inline network proxy — no raw traffic rate-limiting or financial guardrails.

## History with us (analyst / market context)

- April 2026 — Zenity named a "Representative Vendor" in the 2025 Gartner Market Guide for AI TRiSM and a "Cool Vendor in Agentic AI TRiSM"; frequently positioned in direct analyst bake-offs against other AI security platforms.
