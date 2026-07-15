# Competitor — Zenity

Source: [salt.security/vs-zenity](https://salt.security/vs-zenity)

## Who they are

Zenity is a cybersecurity company based in Tel Aviv, Israel, founded in 2020 by former Microsoft cloud security veterans Ben Kliger and Michael Bargury. They provide an agentic AI security platform focused on continuous discovery, posture management, and runtime threat detection for enterprise AI agents, copilots, and low-code/no-code applications. Their ICP includes large enterprises — particularly Fortune 500 companies in financial services, consulting, and technology — that are heavily adopting SaaS automation ecosystems, custom cloud AI frameworks, and endpoint coding assistants. They are backed by Microsoft's M12 venture arm and purpose-built for observing and governing agent activity across SaaS and endpoint environments, especially the Microsoft stack (M365 Copilot, Azure AI Foundry, Teams agents).

## Aliases / names to watch for

- Company: Zenity
- Products: **Zenity Observe**, **Zenity Govern**, **Zenity Defend**
- Category framing they own: "AISPM" (AI Security Posture Management), "AIDR" (AI Detection and Response), "Agentic AI Security", "Intent-based detection"
- Founders / spokespeople: Ben Kliger (CEO), Michael Bargury (CTO), Karen Katz
- Research arm: **Zenity Labs** — known for "AgentFlayer" zero-click exploit research and "OpenClaw" security research
- Frameworks they co-lead: OWASP Low-Code/No-Code Top 10, OWASP Agentic Top 10
- Backers to expect namedropped: Microsoft M12, AWS, Intel Capital
- Coverage surfaces to expect: M365 Copilot, Copilot Studio, Power Platform, Azure AI Foundry, Salesforce Flow, ServiceNow, ChatGPT Enterprise, Teams agents

## Pillars they lean on

- **Observe (AI Observability)** — Discover and inventory AI agents across all platforms with clear insight into ownership, permissions, integrations, and runtime behavior.
- **Govern (AISPM)** — Apply secure-by-design policies to agent configurations, permissions, tool access, and memory before deployment.
- **Defend (AIDR)** — Monitor step-level agent execution, correlate behavior with context, and enforce inline controls to stop unsafe actions in real time.

## Positioning language they use

- Taglines: "Secure AI Agents Everywhere", "Purpose-Built to Secure How Enterprises Actually Operationalize AI"
- Category names they push: AI Agent Governance, AISPM, AIDR
- Signature phrases: "Intent-based detection", "From buildtime to runtime", "Defense-in-Depth for AI Agents", "Step-level behavioral monitoring"

## Known claims / customer names to listen for

- Named customers: Fortune 200 consulting firms, Fortune 50 financial services companies, Fortune 20 technology organizations.
- Public metrics: "90% reduction in security violations" and "95% of high-risk violations automatically remediated" for a major consulting client.
- Partnerships: strategic integrations with Microsoft (M12), AWS, Intel Capital.
- Research: "AgentFlayer" zero-click research at Black Hat / DEF CON; CTO's OWASP Low-Code/No-Code Top 10 leadership.

## Our core framing against them

**"Zenity monitors agent behavior. Salt secures the APIs where behavior becomes damage."** Zenity tells you what your agents intended; Salt secures what they actually did to the API fabric. Zenity's governance stops at the SaaS/platform boundary — agents don't.

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

## What Zenity does well (steelman)

- Deep, native coverage of agent activity inside the Microsoft ecosystem — M365 Copilot, Azure AI Foundry, Teams agents — plus other supported enterprise SaaS (Salesforce, ServiceNow, ChatGPT Enterprise).
- Step-level agent behavior analysis and incident correlation across identity and posture signals.
- Agentic browser coverage via device agent.
- Genuinely valuable governance for organizations heavily concentrated in Microsoft's stack.

## Where we beat them (our attack angles)

- **No action-layer coverage:** Zenity doesn't cover the APIs, MCP servers, and downstream services where agent behavior actually turns into enterprise risk — the "hands" and "action layer" beyond the LLM.
- **Platform lock-in:** Coverage limited to supported platforms only — no LangChain, Databricks, CrewAI, or other custom agent frameworks. Salt is platform-agnostic by design.
- **No downstream/business logic protection:** No coverage of downstream enterprise APIs or business logic abuse once an agent's action leaves the SaaS boundary.
- **Requires a device agent** for endpoint visibility; Salt is fully out-of-band with zero device-agent dependency.
- **No Agentic Security Graph:** No cross-fabric correlation of LLM, MCP, API, and identity signals — Zenity correlates within its supported platforms only, not across the full fabric.
- **No shadow API / rogue MCP discovery:** Zenity's discovery model doesn't catch shadow APIs or rogue MCP servers created outside a monitored SaaS platform.
- **No pre-production governance for APIs/MCP:** Zenity's model activates once agents are deployed and producing behavior signals; Salt Code governs API/MCP creation at the repo/PR level before anything ships.
- **No cryptographically signed audit replay** for long-term regulatory defensibility.
- **No inline network proxy (SASE)** for enforcing rate limits or hard financial budgets on raw agent traffic.

## Where they don't overlap

- **API fabric depth:** Zenity focuses on monitoring the agent's intent inside the host SaaS platform but stops at the agent boundary; no deep API fabric security or destination-endpoint monitoring for underlying business logic abuse.
- **Audit defensibility:** Operational runtime/monitoring tool, not an evidence platform; no cryptographically signed, deterministic audit replays for long-term regulatory compliance.
- **Traffic-layer enforcement:** Architecture relies on native SaaS API integrations and endpoint agents rather than an inline network proxy — no raw traffic rate-limiting or financial guardrails.

## Proof points / stats to use against Zenity

- 3 layers covered (LLM, MCP, API) vs. Zenity's platform-bound step-level view.
- 0 device agents or platform connectors required for Salt's API fabric visibility.
- 11 capabilities Salt has that Zenity's agent model doesn't cover (per the head-to-head table).
- 8 years of production API security research underpinning the Agentic Security Graph.

## Veiled-attack phrases to flag

Phrases Zenity would use to swipe at Salt or other incumbents — with the translation:

- "Legacy security approaches that focused on filtering prompts or inspecting model outputs in isolation" → reframes traditional prompt firewalls / point tools as outdated.
- "Detection after exfiltration is not security" → attacks log-based SIEM/EDR and any retrospective tooling.
- "Prompt filtering is a valuable first layer. It isn't a security architecture." → obsoletes content-moderation-only vendors.
- "Traditional security tools... were not designed to observe or govern this execution layer" → swipe at CNAPP/CSPM and API-security incumbents.
- "Legacy API security tools" → direct swipe at Salt.
- "Traffic-focused approaches miss the agent" → reframes our runtime strength as a blind spot.
- "Signature-based detection" → misrepresents behavioral ML as static rules.
- "Not built for the AI era" → obsoletes API-first vendors.
- "Point solutions for APIs" → positions Zenity as the broader platform.
- "You need to see the agent's intent, not just the traffic" → dismisses action-layer defense.
- "Governance starts at the model, not the request" → reframes shift-left as their category.

## History with us (analyst / market context)

- April 2026 — Zenity named a "Representative Vendor" in the 2025 Gartner Market Guide for AI TRiSM and a "Cool Vendor in Agentic AI TRiSM"; frequently positioned in direct analyst bake-offs against other AI security platforms.

## Talk track

Zenity is a fine tool if a customer's agent footprint is 100% inside Microsoft 365/Azure AI/Teams and they only need to know what an agent *intended* to do. The moment agents call custom internal APIs, hit MCP servers, run in LangChain/CrewAI/Databricks, or touch anything outside Zenity's supported platform list, Zenity goes dark. That's exactly the layer Salt is built for — position Salt as covering the "hands and action" (APIs/MCP/business logic) that Zenity's "brain-level" step monitoring never reaches. Frame it as complementary-but-incomplete for Microsoft-heavy accounts, and as a hard gap for anyone with a heterogeneous or custom agent stack.
