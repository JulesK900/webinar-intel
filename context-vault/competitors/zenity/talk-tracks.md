# Zenity — talk tracks and known claims

## Our core framing against them

**"Zenity monitors agent behavior. Salt secures the APIs where behavior becomes damage."** Zenity tells you what your agents intended; Salt secures what they actually did to the API fabric. Zenity's governance stops at the SaaS/platform boundary — agents don't.

## Talk track

Zenity is a fine tool if a customer's agent footprint is 100% inside Microsoft 365/Azure AI/Teams and they only need to know what an agent *intended* to do. The moment agents call custom internal APIs, hit MCP servers, run in LangChain/CrewAI/Databricks, or touch anything outside Zenity's supported platform list, Zenity goes dark. That's exactly the layer Salt is built for — position Salt as covering the "hands and action" (APIs/MCP/business logic) that Zenity's "brain-level" step monitoring never reaches. Frame it as complementary-but-incomplete for Microsoft-heavy accounts, and as a hard gap for anyone with a heterogeneous or custom agent stack.

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

## Known claims / customer names to listen for

- Named customers: Fortune 200 consulting firms, Fortune 50 financial services companies, Fortune 20 technology organizations.
- Public metrics: "90% reduction in security violations" and "95% of high-risk violations automatically remediated" for a major consulting client.
- Partnerships: strategic integrations with Microsoft (M12), AWS, Intel Capital.
- Research: "AgentFlayer" zero-click research at Black Hat / DEF CON; CTO's OWASP Low-Code/No-Code Top 10 leadership.

## Proof points / stats to use against Zenity

- 3 layers covered (LLM, MCP, API) vs. Zenity's platform-bound step-level view.
- 0 device agents or platform connectors required for Salt's API fabric visibility.
- 11 capabilities Salt has that Zenity's agent model doesn't cover (per the head-to-head table).
- 8 years of production API security research underpinning the Agentic Security Graph.

## Learned from webinars

<!-- The pipeline appends new recurring claims, phrases, and themes here after each analyzed webinar. Curate freely: this file is an edit surface. -->


- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity positioning around 'AI standards and governance' as thought leadership authority (OWASP GenAI Security Project core team membership)
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Agentic AI security framed as standards/compliance governance play rather than runtime behavior detection
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity positioning Karen Katz's OWASP GenAI Security Project core team role as direct standards-body authority over agentic AI risk taxonomy and security frameworks
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity framing agentic AI security primarily as a standards/compliance/governance play anchored in regulatory and policy authority rather than runtime detection or API protection
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity is positioning itself as the vendor that authored and owns the OWASP Agentic Top 10 taxonomy, implying market-standard authority over agentic AI risk classification.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity claims the 2026 OWASP Agentic Top 10 refresh is a 'total rebuild' they are driving, positioning them as the force reshaping industry risk frameworks.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity added a 'maturity model' to their taxonomy offering, claiming to define how enterprises measure agentic AI security maturity—a governance authority play beyond detection.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity asserts their taxonomy has become the de facto market language ('almost any client or prospect...use these terms'), implying they own the vocabulary competitors must adopt.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity is mapping regulatory compliance across 42 instruments and 10 jurisdictions, positioning themselves as a regulatory/compliance mapping authority to compete with posture management vendors.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity is anchoring drift detection specifically to EU AI Act Article 72 obligations, tying their governance value prop directly to regulatory mandates.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity's runtime dependency graph ('assembles itself live with every execution') is being positioned as a replacement for traditional SBOM—a direct attack on shift-left and build-time governance approaches.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity reframes prompt injection as an attacker TTP ('delivery truck'), not a vulnerability—a semantic reposition that de-emphasizes API-layer detection and elevates supply-chain/trust-layer as the primary threat.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity is implying that the top agentic CVEs are concentrated in semi-autonomous frameworks (copilots), not fully autonomous agents, which weakens the 'urgent future threat' narrative and favors their copilot-focused governance positioning.
- (2026-07-18, [AMA: Inside the OWASP State of Agentic AI Security & Governance](https://www.youtube.com/watch?v=jK1Z7Z6zlW0)) Zenity is positioning skill registries and MCP registries as the fastest-moving attack surface, placing supply-chain governance above API/business-logic abuse in the threat hierarchy.
