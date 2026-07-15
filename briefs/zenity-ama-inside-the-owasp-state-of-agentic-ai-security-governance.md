# AMA: Inside the OWASP State of Agentic AI Security & Governance

- **Channel:** Zenity
- **URL:** https://www.youtube.com/watch?v=jK1Z7Z6zlW0

## Overview
This webinar was a Zenity-hosted panel discussion launching the second version of the OWASP 'State of Agentic AI Security and Governance' report. The panel featured OWASP contributors discussing updates to the taxonomy, threat analysis, MCP/protocol landscape, AI SBOM, regulatory landscape, and a new enterprise adoption maturity model. It was framed as an industry/community conversation rather than a Zenity product pitch, though Zenity's category framing (agent-centric, intent-based) permeates the discussion.

## Speakers
- Karen Katz — Director for AI Security, Zenity (and OWASP lead for Agentic Top 10) ([search](https://www.google.com/search?q=Karen+Katz+Director+for+AI+Security+Zenity+linkedin))
- Rock Lambros — Director of AI Standards and Governance, Zenity (OWASP GenAI Security Project core team) ([search](https://www.google.com/search?q=Rock+Lambros+Director+of+AI+Standards+and+Governance+Zenity+linkedin))
- Ariel — Founding Engineer & AI Security Researcher, Office of the CTO, Pillar Security ([search](https://www.google.com/search?q=Ariel+Founding+Engineer+%26+AI+Security+Researcher+Office+of+the+CTO+Pillar+Security+linkedin))
- Evgeniy (Gani) — AI Security Research lead at ITMO University; runs Hive Trace ([search](https://www.google.com/search?q=Evgeniy+AI+Security+Research+lead+at+ITMO+University%3B+runs+Hive+Trace+linkedin))

## What was covered
- Rationale for a second version of the OWASP State of Agentic AI report: last year was forecast, this year is documented incidents, CVEs, and real breaches
- Updated agent taxonomy — new axes covering agent type/domain, how they're built (framework vs low/no-code), composition (single vs multi-agent), and autonomy level as a cross-cutting risk dimension
- Key trends: safety converging with security, non-human vs agent identities, regulatory pressure, explainability challenges, and prioritizing risk by footprint rather than autonomy level
- Threat analysis: prompt injection reframed as a delivery mechanism/TTP (not a vulnerability), and supply chain as the fastest-moving attack surface (tool descriptions, memory files, skill registries, MCP plugins)
- Agentic protocol landscape — MCP has exploded in adoption (Postmark MCP incident highlighted); A2A still nascent
- AI SBOM / AIBOM — buildtime inventories insufficient because agents assemble dependency graphs at runtime; need behavior-level descriptions
- Regulatory landscape: 42 instruments across 10 jurisdictions, EU AI Act Article 72 implicitly demanding drift detection, incident reporting clocks (DORA 4hr, NIS2 24hr), EU strict product liability, US executive orders and CISA BOD
- New enterprise adoption maturity model — tiers from shadow AI through citizen developer to multi-agent/federated systems, mapped against governance maturity

## Direct competitor mentions
_None._

## Indirect mentions
- [0:28:25](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1705s) Rock Lambros: 'everyone calls prompt injection the vulnerability and it's not... it's the delivery mechanism.' — reframes traditional prompt-firewall/point vendors as missing the point; aligns with Zenity's 'prompt filtering isn't a security architecture' swipe.
- [0:29:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1752s) Rock Lambros: 'attackers stopped attacking the agent and started poisoning what the agent trusts... tool descriptions, memory file, dependencies.' — positions traditional API/runtime tools (including Salt) as looking at the wrong layer, favoring Zenity's agent-context view.
- [0:37:01](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2221s) Rock Lambros: 'Traditional SBOM is a buildtime list. Agents... don't work that way... your buildtime inventory describes a system that stopped existing kind of the moment that the agent ran.' — veiled attack on shift-left/code-based governance approaches like Salt Code, arguing runtime agent behavior can't be governed pre-production.
- [0:40:11](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2411s) Ariel: 'even if all of the components look safe when you actually deploy to production at runtime something completely different happens.' — implicit swipe at pre-production/API-inventory approaches, favoring agent behavioral monitoring.
- [0:53:44](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3224s) Ariel: 'the very first thing that needs to be taken into consideration really is a discovery phase where you're able to identify what's going on, how is it being deployed, what's it connected to.' — Zenity claiming the discovery ground that Salt's Illuminate pillar owns for APIs/MCP.

## Where they touched our territory
- [0:29:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1752s) Ariel: discussion of MCP threat models, skill registries, and plugin marketplaces as new supply chains — directly overlaps Salt's Unified Agentic Discovery (Illuminate) and rogue MCP detection.
- [0:34:52](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2092s) Evgeniy: 'The most notable incident on MCP is... the Postmark MCP when this server was legitimate for many releases... at some point the new version came with only one line added, blind copy to the attacker email.' — squarely in Salt's MCP governance and posture territory (AG-SPM / Salt Code).
- [0:37:17](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2237s) Rock Lambros: 'for any high-stakes workflows you need to reconstruct afterwards which tool and which agents touched the outcome' — this is exactly Salt's Agentic Security Graph value prop (LLM→MCP→API correlation).
- [0:41:38](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2498s) Rock Lambros: 'no regulator actually wrote the words do drift detection, but how are you going to start your 4hour clock on something that makes automated decisions' — Salt's AG-SPM continuous drift/posture story.
- [0:53:44](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3224s) Ariel: shadow AI discovery as tier-zero of maturity model — overlaps Salt's shadow/zombie API and agent discovery messaging.

## Where they contradicted us
- [0:37:01](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2221s) Rock Lambros: 'Traditional SBOM is a buildtime list... your buildtime inventory describes a system that stopped existing the moment the agent ran.' — undercuts Salt Code's shift-left/PR-level governance narrative by arguing pre-production artifacts are stale.
- [0:29:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1752s) Rock Lambros: 'attackers stopped attacking the agent and started poisoning what the agent trusts.' — reframes the threat as being about agent trust/context, subtly implying API-layer defense misses the real attack surface (contradicts Salt's action-layer positioning).
- [0:40:11](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2411s) Ariel: 'even if all of the components look safe when you actually deploy to production at runtime something completely different happens' — challenges the value of inventory/discovery-first approaches without behavioral step-level monitoring (Zenity's category).

## Where they left an opening
- Zero discussion of API-layer defense, business logic abuse, or east-west/internal traffic — the panel never addressed what happens once an agent's action leaves the SaaS/agent boundary and hits enterprise APIs.
- No mention of platform coverage limitations — the panel talked abstractly about 'agents everywhere' but never addressed LangChain, CrewAI, Databricks, or custom-built agent frameworks where Zenity has gaps.
- MCP discussion focused on supply-chain poisoning of tool descriptions but did NOT address discovery of rogue/shadow MCP servers stood up outside monitored SaaS platforms — Salt's Illuminate advantage.
- Regulatory conversation heavily emphasized incident-reporting clocks and drift detection but Zenity has no cryptographically signed audit replay — a compliance evidence gap we can exploit.
- AISBOM discussion admitted current standards can't describe agentic runtime behavior — Salt's Agentic Security Graph directly answers this, and no Zenity panelist claimed they had a solution.
- Panel repeatedly acknowledged shadow AI is ungoverned and organizations don't know what MCPs are in use — direct opening for Salt's agentless, out-of-band discovery story vs Zenity's device-agent + platform-connector model.
- Karen (Zenity) herself said enterprises 'don't even know what MCPs are in use' — a candid admission that undermines Zenity's own discovery claims and invites Salt's positioning.

## Recommended response
- Publish a blog titled 'Buildtime + Runtime: Why Agentic Security Needs Both' that directly rebuts Rock Lambros' 'buildtime inventory describes a system that stopped existing' framing — position Salt Code + AG-DR + Agentic Security Graph as the only platform that connects PR-level governance to runtime behavior with feedback loops, and explicitly reference the OWASP report's own AISBOM gap.
- Update the Zenity battle card with three new proof points from this webinar: (1) Zenity's own director admits enterprises 'don't even know what MCPs are in use' — use to attack their discovery claims; (2) the Postmark MCP incident as a case for Salt's cross-platform MCP discovery + posture (not just SaaS-bound); (3) new regulatory drift-detection angle (EU AI Act Article 72, DORA 4hr clock) tied to Salt's continuous AG-SPM vs Zenity's platform-bound monitoring.
- Arm the field with a talking point: 'Zenity's own OWASP panel spent 60 minutes on agent intent, prompt injection, and SBOMs — and never once mentioned the API or the business logic behind the agent. That silence IS the gap. Ask them where the action layer lives.' Pair with a one-pager mapping every OWASP report theme (taxonomy, supply chain, AISBOM, drift, maturity model) to a specific Salt pillar.
