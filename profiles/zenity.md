# Competitor — Zenity

Source: [salt.security/vs-zenity](https://salt.security/vs-zenity)

## Who they are

Zenity is an AI agent governance platform, founded by Microsoft cloud security veterans and backed by Microsoft's M12. It's purpose-built for observing and governing agent activity across SaaS and endpoint environments, especially the Microsoft stack (M365 Copilot, Azure AI Foundry, Teams agents). It monitors agents at the step level and correlates incidents across identity and posture signals.

## Aliases / names to watch for

* Zenity
* Zenity Labs (their research arm)
* "AI agent governance" / "agent security" / "AISPM"
* "Agentic Top 10" / "OWASP Agentic Top 10" (co-authored / promoted)
* Founder / spokesperson names: Ben Kliger, Michael Bargury, Karen Katz
* M12 (Microsoft's venture arm, their lead backer)
* Copilot Studio, Power Platform, Azure AI Foundry (their strongest coverage surfaces)

## Pillars they lean on

* **AI agent security posture management (AISPM)** — inventory + risk scoring for agents.
* **Agent runtime protection** — detect prompt injection, data exfiltration, tool abuse.
* **Low-code/no-code app security** — Power Platform, Copilot Studio, Salesforce Flow, ServiceNow.
* **Governance for citizen developers** — guardrails on who can build what.
* **Step-level agent behavior analysis** — correlating incidents across identity and posture signals.

## Positioning language they use

* "Secure every AI agent."
* "Agentic AI security."
* "From build time to run time."
* "The AI security platform for the enterprise."
* "AI Security Posture Management (AISPM)."

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

* Deep, native coverage of agent activity inside the Microsoft ecosystem — M365 Copilot, Azure AI Foundry, Teams agents — plus other supported enterprise SaaS (Salesforce, ServiceNow, ChatGPT Enterprise).
* Step-level agent behavior analysis and incident correlation across identity and posture signals.
* Agentic browser coverage via device agent.
* Genuinely valuable governance for organizations heavily concentrated in Microsoft's stack.

## Where we beat them (our attack angles)

* **No action-layer coverage:** Zenity doesn't cover the APIs, MCP servers, and downstream services where agent behavior actually turns into enterprise risk — the "hands" and "action layer" beyond the LLM.
* **Platform lock-in:** Coverage limited to supported platforms only — no LangChain, Databricks, CrewAI, or other custom agent frameworks. Salt is platform-agnostic by design.
* **No downstream/business logic protection:** No coverage of downstream enterprise APIs or business logic abuse once an agent's action leaves the SaaS boundary.
* **Requires a device agent** for endpoint visibility; Salt is fully out-of-band with zero device-agent dependency.
* **No Agentic Security Graph:** No cross-fabric correlation of LLM, MCP, API, and identity signals — Zenity correlates within its supported platforms only, not across the full fabric.
* **No shadow API / rogue MCP discovery:** Zenity's discovery model doesn't catch shadow APIs or rogue MCP servers created outside a monitored SaaS platform.
* **No pre-production governance:** Zenity's model activates once agents are deployed and producing behavior signals; Salt Code governs API/MCP creation at the repo/PR level before anything ships.

## Proof points / stats to use against Zenity

* 3 layers covered (LLM, MCP, API) vs. Zenity's platform-bound step-level view.
* 0 device agents or platform connectors required for Salt's API fabric visibility.
* 11 capabilities Salt has that Zenity's agent model doesn't cover (per the head-to-head table).
* 8 years of production API security research underpinning the Agentic Security Graph.

## Veiled-attack phrases to flag (things they'd say to swipe at Salt)

* "Legacy API security tools" → us.
* "Traffic-focused approaches miss the agent" → reframes our runtime strength as a blind spot.
* "Signature-based detection" → misrepresents behavioral ML as static rules.
* "Not built for the AI era" → obsoletes API-first vendors.
* "Point solutions for APIs" → positions Zenity as the broader platform.
* "You need to see the agent's intent, not just the traffic" → dismisses action-layer defense.
* "Governance starts at the model, not the request" → reframes shift-left as their category.

## Talk track

Zenity is a fine tool if a customer's agent footprint is 100% inside Microsoft 365/Azure AI/Teams and they only need to know what an agent *intended* to do. The moment agents call custom internal APIs, hit MCP servers, run in LangChain/CrewAI/Databricks, or touch anything outside Zenity's supported platform list, Zenity goes dark. That's exactly the layer Salt is built for — position Salt as covering the "hands and action" (APIs/MCP/business logic) that Zenity's "brain-level" step monitoring never reaches. Frame it as complementary-but-incomplete for Microsoft-heavy accounts, and as a hard gap for anyone with a heterogeneous or custom agent stack.
