# jK1Z7Z6zlW0

- **Channel:** 
- **URL:** https://www.youtube.com/watch?v=jK1Z7Z6zlW0

## Overview
This was a Zenity-hosted webinar launching the second version of the OWASP 'State of Agentic AI' report, co-presented by Karen Katz (Zenity), Rock Lambros (Zenity, OWASP), Ariel (Pillar Security), and Evgeniy (Hive Trace). The panel walked through updates to the agent taxonomy, threat analysis, MCP/protocol landscape, AI-BOM, regulatory landscape, and a new enterprise adoption maturity model.

## What was covered
- Why a v2 was needed: threats moved from forecast to documented CVEs and real incidents (coding agents wiping prod DBs, zero-click Copilot data exfiltration)
- Updated agent taxonomy with new axes: agent type/domain, build method (framework vs. no/low-code), composition (single vs. multi-agent), and autonomy level as a cross-cutting risk dimension
- Threat analysis reframing prompt injection as a delivery mechanism (TTP) rather than a vulnerability, appearing across 6 of 10 categories
- Supply chain elevated as the fastest-moving attack surface: MCP servers, skill registries, plugin marketplaces, tool descriptions, and memory poisoning (Postmark MCP incident cited)
- AI-BOM discussion pivoting from buildtime component lists to runtime behavior descriptions, since agents assemble dependencies dynamically
- Regulatory update: 42 instruments across 10 jurisdictions, EU AI Act Article 72 'drift detection', DORA/NIS2/NY/CA incident clocks, EU strict no-fault product liability, CISA BOD, US executive orders
- New Enterprise Adoption Maturity Model mapping adoption tiers (Shadow AI → citizen dev → in-house agents → multi-agent → federated) against governance maturity
- Repeated emphasis that Shadow AI discovery is Tier 0 and the required starting point before any governance can happen

## Direct competitor mentions
- No direct mention of Salt Security or any named API security competitor throughout the webinar
- Postmark MCP named as the marquee supply-chain incident example
- OWASP GenAI Security Project, LLM Top 10 (Steve Wilson co-lead), Helen Oakley's AI-BOM initiative referenced as aligned OWASP work
- Anthropic and Linux Foundation credited for MCP standardization

## Indirect mentions
- Rock: 'treating [prompt injection] as a checkbox that you can solve... you're just going to waste time' — veiled swipe at prompt-firewall and content-moderation-only vendors
- Ariel: buildtime SBOMs 'describe a system that stopped existing the moment the agent ran' — indirect knock on static/shift-left-only API and AppSec tools, which could be aimed at Salt's traditional runtime-observed model as well as APIsec/42Crunch
- Rock on supply chain: 'attackers stopped attacking the agent and started poisoning what the agent trusts' — reframes the action layer (Salt's turf) as downstream/less important than the trust graph Zenity governs
- Repeated 'blast radius' language tied to autonomy and composition — implicit positioning that governance at the agent/platform layer is the correct control point vs. traffic/API-layer defense
- 'Shadow AI' as Tier 0 discovery gap — implicitly reframes discovery around agents/copilots (Zenity's turf) rather than shadow APIs/MCP endpoints (Salt's turf)

## Where they touched our territory
- MCP discovery and governance — Zenity claiming the discovery narrative around MCP servers, which is core to Salt's Unified Agentic Discovery pillar
- Supply chain / rogue MCP detection — Postmark MCP example lands squarely in territory Salt claims via Illuminate and AG-SPM
- Drift detection tied to EU AI Act Article 72 — overlaps directly with Salt's AG-SPM compliance governance positioning
- Runtime behavioral analysis and 'blast radius' framing — overlaps with Salt's AG-DR behavioral threat protection
- Incident reporting clocks (DORA 4hr, NIS2 24hr) requiring continuous oversight — a natural Salt wedge for API/agent runtime evidence, but Zenity is claiming the narrative
- Shadow discovery as the mandatory first step — Salt says this about shadow/zombie APIs; Zenity is repositioning it around shadow AI/agents

## Where they contradicted us
- Framing prompt injection and agent trust-graph poisoning as THE dominant threat surface implicitly downgrades API-layer/business-logic abuse (Salt's core AG-DR value prop)
- Ariel's claim that buildtime inventories 'describe a system that stopped existing' undercuts any static or pre-runtime API inventory narrative and pressures Salt Code's shift-left story
- The maturity model positions governance maturity around agent composition and autonomy — not around API attack surface — implicitly making Salt's API-centric maturity narrative feel orthogonal or incomplete
- Rock's point that 'top 5 CVEs are all semi-autonomous frameworks, not fully autonomous' subtly argues risk lives in framework/platform config (Zenity turf) rather than at the action layer
- Regulatory framing centers on agent oversight and drift, not on API governance — a land grab on the compliance narrative Salt uses for AG-SPM

## Where they left an opening
- Zero discussion of the API/action layer where agent intent becomes damage — no mention of business logic abuse, east-west API traffic, or downstream enterprise APIs
- No mention of platform-agnostic frameworks like LangChain, CrewAI, or Databricks — confirms Zenity's SaaS-platform-bound coverage gap
- AI-BOM discussion admitted current standards (CycloneDX, SPDX) can't describe agentic behavior — Salt can position the Agentic Security Graph as the missing runtime grammar
- Ariel explicitly said Shadow AI is 'completely ungoverned' and discovery must come first — but Zenity's discovery is platform-bound; Salt's agentless, out-of-band discovery of shadow APIs and rogue MCPs is a direct counter
- The Postmark MCP example was framed as a supply-chain problem but no answer was given for how to detect the malicious BCC behavior at runtime on the API/traffic side — Salt's behavioral runtime story fits exactly here
- Regulatory 4-hour incident clocks discussed with no answer for how you actually produce forensic evidence — Salt's audit/replay and API-level telemetry is a natural fill
- No mention of inline enforcement, rate limiting, or blocking — both vendors share this gap, but Salt's integrations with WAFs/gateways/CrowdStrike/Wiz give a stronger enforcement story
- Multi-agent and federated agentic systems admitted as 'not there yet' — Salt can claim readiness via the Agentic Security Graph before Zenity's model matures

## Recommended response
- Publish a Salt Labs blog titled 'Intent Is Not Impact: Why the Postmark MCP Incident Proves You Need Action-Layer Defense' — walk through the Postmark case and show how behavioral API baselining catches the malicious BCC exfil that agent-layer governance misses, directly rebutting Zenity's supply-chain framing
- Update the Zenity battle card with three new objection handlers: (1) 'Agent maturity model is platform-bound — ask them how they cover LangChain/CrewAI/Databricks and shadow MCPs created outside monitored SaaS'; (2) 'Their AI-BOM story admits buildtime inventories are dead — Salt's Agentic Security Graph is the runtime grammar they said doesn't exist yet'; (3) 'Ask how they produce a 4-hour DORA incident report without API-layer telemetry'
- Arm the field with a talk track anchored on EU AI Act Article 72 drift detection and DORA/NIS2 incident clocks: position AG-SPM + AG-DR as the only way to produce continuous oversight evidence at the action layer, and pair it with a co-sell motion for Microsoft-heavy accounts where Zenity covers Copilot and Salt covers everything the agents actually call
