# jK1Z7Z6zlW0

- **Channel:** 
- **URL:** https://www.youtube.com/watch?v=jK1Z7Z6zlW0

## Overview
Zenity co-hosted an OWASP-affiliated webinar announcing the second version of the 'State of Agentic AI Security and Governance' report. Panelists included Zenity's Karen Katz and Rock Lambros alongside contributors from Pillar Security and ITMO/Hive Trace, framed as an OWASP Agentic AI Security Initiative deliverable rather than an overt Zenity pitch.

## What was covered
- Rationale for a v2 report: shift from forecasting to documented CVEs, real incidents (coding agent wiping prod DBs, zero-click Copilot data exfil)
- Updated agent taxonomy with new axes: agent type/domain, build method (framework vs. low-code), composition (single vs. multi-agent), and autonomy level as a cross-cutting risk dimension
- Key trends: safety converging with security, non-human/agent identity, regulatory landscape, explainable AI challenges
- Threat analysis reframing prompt injection as a delivery mechanism/TTP rather than a vulnerability; supply chain elevated as fastest-moving attack surface (poisoning tool descriptions, memory, skills, MCP)
- MCP adoption and Postmark MCP incident as canonical supply chain case; A2A adoption still nascent
- AI-SBOM discussion led by Helen Oakley's work — shift from build-time inventory to runtime-assembled dependency graphs
- Regulatory deep-dive: EU AI Act Article 72 (implicit drift detection), DORA 4-hour clocks, NIS2, US executive orders, CISA BOD 3-day patch cycle, EU no-fault product liability
- New Enterprise Adoption Maturity Model mapping AI adoption tiers (Shadow AI → citizen developer → in-house agents → multi-agent/federated) against governance maturity, with discovery as the mandatory first step

## Direct competitor mentions
- Karen Katz opens: 'I'm Zenity director for AI security and OWASP lead for the Agentic top 10'
- Rock Lambros: 'My day-to-day role is the director of AI standards and governance at Zenity and I'm also on the core team of the OWASP GenAI security project agentic security initiative'
- Ariel introduced as 'founding engineer and AI security researcher at the office of the CTO at Pillar Security'
- Evgeny: 'I run AI security research at ITMO university and I run a company called Hive Trace'
- Postmark MCP named as the notable supply chain incident: 'legitimate for many releases... new version came with only one line added, blind copy to the attacker email'

## Indirect mentions
- 'Almost every category we forecasted last year now has a CVE assigned to it' — implicit swipe at incumbents (including Salt) who treat agentic risk as future/hypothetical
- 'Prompt injection is not the vulnerability, it's the delivery mechanism' — dismisses prompt-firewall/point-tool vendors and reframes the problem toward Zenity's step-level intent monitoring
- 'Attackers stopped attacking the agent and started poisoning what the agent trusts' — positions traditional API/traffic security (Salt's home turf) as looking at the wrong layer
- 'Traditional SBOM is a build-time list... agents don't work that way, they discover tools, load skills, spawn sub-agents at runtime' — implicit knock on shift-left/API testing vendors and any static inventory approach
- 'Buildtime inventory describes a system that stopped existing the moment the agent ran' — undermines any pre-production or config-time governance posture (could hit Salt Code framing if not carefully positioned)
- 'Article 72 quietly demands drift detection without using the words' — Zenity implicitly claiming they cover this; a swipe at API security tools that don't map to AI-specific regulatory clauses
- 'Shadow AI is completely ungoverned... the very first thing is a discovery phase' — Zenity anchoring the discovery narrative for AI/agents specifically, adjacent to Salt's Illuminate pillar

## Where they touched our territory
- Discovery of agents/shadow AI as the mandatory Tier 0 activity — directly overlaps Salt Illuminate / Unified Agentic Discovery
- Supply chain / MCP poisoning as the top attack surface — Salt's Agentic Security Graph (LLM→MCP→API) is explicitly built for this correlation
- Runtime behavior monitoring and 'blast radius' analysis for multi-agent systems — overlaps AG-DR behavioral protection
- Regulatory mapping (EU AI Act, DORA, NIS2) and drift detection — overlaps AG-SPM posture/compliance governance
- AI-SBOM and runtime dependency graphs — conceptually overlaps Salt's Agentic Security Graph and inventory story
- Incident reporting clocks requiring 'continuous oversight' — Salt's out-of-band big-data baselining is arguably better positioned than Zenity's platform-bound view to deliver this

## Where they contradicted us
- Rock's claim that 'buildtime inventory describes a system that stopped existing the moment the agent ran' directly undercuts Salt Code's pre-production repo/PR governance value prop if left unanswered
- Framing prompt injection and supply chain as the dominant threat vectors while never mentioning API abuse, business-logic attacks, or east-west API traffic — implicitly asserting that the API/action layer isn't where the real risk lives
- 'Governance-first, discovery-first' narrative anchored inside SaaS/agent platforms suggests API security is downstream/secondary rather than the destination where damage actually occurs
- Positioning Zenity contributors as the OWASP thought leaders on agentic taxonomy, threat modeling, and maturity — creating a halo that 'Zenity = the reference architecture' for agentic security

## Where they left an opening
- Zero discussion of what happens after the agent calls an API — no coverage of business-logic abuse, API auth bypass, or east-west API traffic once an action leaves the SaaS boundary
- No mention of custom/heterogeneous agent stacks (LangChain, CrewAI, Databricks) — the entire conversation implicitly assumes SaaS-hosted or framework-based agents Zenity can observe
- AI-SBOM framed as immature and unenforced by regulators — Salt can counter with a concrete Agentic Security Graph that already delivers the runtime dependency view they're describing as aspirational
- Regulatory clocks (DORA 4hr, NIS2 24hr) require deterministic detection and evidence — Zenity offers no cryptographically signed audit replay; Salt can own the 'defensible evidence' narrative
- Panel repeatedly says 'we're not there yet' on multi-agent and federated deployments — Salt can plant a flag that its API-layer correlation already works today regardless of orchestration framework
- Discovery discussion stayed at the 'agent' level — no mention of shadow APIs, zombie APIs, or rogue MCP servers created outside monitored SaaS platforms
- No customer names, no quantified outcomes, no architecture specifics — the webinar was standards-flavored thought leadership, leaving room for Salt to counter with concrete enterprise proof points (Armis, Berkshire, Siemens, 20K RPS, 96% alert reduction)

## Recommended response
- Publish a Salt Labs blog titled something like 'Prompt Injection is the Delivery Truck — The API is the Vault' that agrees with Rock's TTP framing and then pivots hard to the action layer: show a Postmark-MCP-style scenario end-to-end and demonstrate that only API/MCP correlation (Agentic Security Graph) catches the exfil path. Cite the OWASP report to ride its SEO.
- Update the Zenity battle card with three new plays: (1) 'Buildtime SBOM is dead' rebuttal — position Salt Code as runtime-informed, not static, feeding PR-level governance from live API telemetry; (2) Regulatory defensibility play — highlight cryptographically signed audit replay and drift detection mapped to EU AI Act Article 72 and DORA 4-hour clocks; (3) Platform-agnostic play — call out that Zenity's panel never mentioned LangChain/CrewAI/Databricks and use that as the disqualifier in heterogeneous accounts.
- Arm sellers with a one-liner talking point: 'Zenity will tell you what your agent intended inside Microsoft 365. Salt tells you what it actually did to your API fabric — and gives you the signed evidence when the regulator's 4-hour clock starts.' Pair with a discovery question set: 'Do your agents ever call a custom internal API, an MCP server you built, or a non-SaaS framework? If yes, where does Zenity go dark?'
