# AMA: Inside the OWASP State of Agentic AI Security & Governance

- **Channel:** Zenity
- **Webinar type:** competitor-hosted (their claims analyzed)
- **URL:** https://www.youtube.com/watch?v=jK1Z7Z6zlW0

## Overview
A webinar discussing the second version of the OWASP State of Agentic AI report, which documents the evolution of agentic AI security from forecasting to real-world incident analysis. The speakers highlighted major updates including refined taxonomy, threat analysis backed by CVEs and documented incidents, regulatory landscape changes, and a new enterprise adoption maturity model.

## Speakers
- Karen Katz — Director of Security, Zenity; OWASP Agentic Top 10 Lead ([search](https://www.google.com/search?q=Karen+Katz+Director+of+Security+Zenity%3B+OWASP+Agentic+Top+10+Lead+linkedin))
- Rock Lambros — Director of AI Standards and Governance, Zenity; OWASP GenAI Security Project Core Team ([search](https://www.google.com/search?q=Rock+Lambros+Director+of+AI+Standards+and+Governance+Zenity%3B+OWASP+GenAI+Security+Project+Core+Team+linkedin))
- Ariel — Founding Engineer and AI Security Researcher, Office of the CTO at Pillar Security ([search](https://www.google.com/search?q=Ariel+Founding+Engineer+and+AI+Security+Researcher+Office+of+the+CTO+at+Pillar+Security+linkedin))
- Genei — AI Security Researcher, ITMO University; Founder, Hive Trace ([search](https://www.google.com/search?q=Genei+AI+Security+Researcher+ITMO+University%3B+Founder+Hive+Trace+linkedin))

## What was covered
- Evolution from speculative forecast (v1) to documented incidents with CVEs and real-world examples in the 2025 version
- Refined agent taxonomy incorporating agent types, domains, building approaches, composition models, and autonomy levels as key risk evaluation axes
- Threat analysis showing prompt injection as a delivery mechanism across multiple categories and supply chain poisoning as the fastest-moving attack surface
- AI SBOM framework adapted for agentic systems that assemble dependencies at runtime, with challenges in describing behavior and addressing regulatory requirements
- Regulatory landscape update covering EU AI Act Article 72 drift detection requirements, incident reporting timelines across jurisdictions, and EU strict liability shifts
- Enterprise adoption maturity model mapping shadow AI, platform-based, citizen developer, in-house, and multi-agent tiers to appropriate governance levels
- MCP (Model Context Protocol) adoption and security risks, including the Postmark supply chain incident example
- Practical recommendations for discovery, governance implementation, and contractual requirements driven by federal procurement and insurance providers

## Key positioning claims
- [0:10:22](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=622s) Rock Lambros: 'director of AI standards and governance at Zenity' — positions Zenity as a standards/governance authority, not just a product vendor.
- [0:09:56](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=596s) Karen Katz: 'Zenity director for security and OWASP lead for the Agentic top 10' — claims direct ownership of the OWASP Agentic Top 10 taxonomy as Zenity IP/authority.
- [0:14:27](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=867s) Rock Lambros: 'the 2026 version...It's a total rebuild' — frames Zenity as driving the refresh of the industry's agentic risk taxonomy.
- [0:14:39](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=879s) Rock Lambros: 'We added a maturity model' — Zenity positioning itself as the vendor defining how enterprises should measure agentic AI security maturity.
- [0:15:46](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=946s) Karen Katz: 'almost any client or prospect that I'm talking with actually use this terms' — asserts Zenity's taxonomy is the market's default language.
- [0:30:37](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1837s) Ariel: 'prompt injection as a TTP' — reframes prompt injection as an attacker technique category, elevating Zenity's threat model authority.
- [0:37:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2232s) Rock Lambros: 'The dependency graph assembles itself live with every execution' — positions Zenity's runtime dependency view as the new SBOM.
- [0:42:50](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2570s) Rock Lambros: 'we mapped 42 instruments against 10 jurisdictions...in the US alone there's something like 175 different AI related regulations' — Zenity claiming a compliance-mapping authority position.
- [0:44:16](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2656s) Rock Lambros: 'article 72...quietly demands drift detection' — Zenity anchoring drift detection to EU AI Act obligations as their governance value prop.

## Swipes at us / other vendors
- [0:28:40](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1720s) Rock Lambros: 'everyone calls prompt injection the vulnerability and it's not...it's the delivery mechanism...the delivery truck' — swipe at every vendor (including Salt-adjacent messaging) that markets prompt-injection detection as a core defense; positions competitors as chasing symptoms.
- [0:29:23](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1763s) Rock Lambros: 'attackers stopped attacking the agent and started poisoning what the agent trusts' — implicit swipe at agent-centric or API-centric vendors who don't cover supply chain/skills/MCP registries; positions Zenity's supply-chain focus as ahead.
- [0:31:10](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1870s) Ariel: 'these are all new supply chains that are being quickly adopted and are not necessarily being scrutinized well' — veiled shot at incumbents (including API security vendors like us) not covering skill registries and agent supply chains.
- [0:37:00](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2220s) Rock Lambros: 'Traditional ESBOM is a buildtime list. Agents...discover tools, they load skills, they spawn sub agents at runtime' — swipe at shift-left/SBOM/build-time inventory tools; brushes against Salt Code's pre-production governance positioning.
- [0:53:13](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3193s) Ariel: 'shadow AI...which is completely ungoverned' — implicit swipe at API-security and traditional discovery vendors that don't see agents built on low-code/citizen-developer platforms.

## Where they touched our territory
- [0:37:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2232s) Rock Lambros: 'The dependency graph assembles itself live with every execution' — directly overlaps our Agentic Security Graph pillar; they are claiming the same live-correlation ground.
- [0:44:16](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2656s) Rock Lambros: 'article 72...quietly demands drift detection' — encroaches on AG-SPM's drift detection and EU AI Act mapping message.
- [0:42:50](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2570s) Rock Lambros: 'we mapped 42 instruments against 10 jurisdictions' — competes with our Posture Management & Compliance Governance pillar.
- [0:32:31](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1951s) Genii: 'MCP...is widely adopted standard for connecting the agents to tools' and [0:34:49] Genii: 'postmark MCP...new version came with a blind copy to the attacker email' — touches our MCP-server discovery and rogue-MCP protection story.
- [0:50:24](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3024s) Genii: 'adoption tier such as shadow AI...or using the platforms or the citizen developer' — overlaps our Unified Agentic Discovery (Illuminate) pillar.
- [0:14:29](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=869s) Rock Lambros: 'We rebuilt a thread analysis around documented cases' — competes for the runtime threat authority positioning we own with Salt Labs and AG-DR.

## Where they contradicted us
- [0:37:00](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2220s) Rock Lambros: 'Traditional ESBOM is a buildtime list. Agents...discover tools, they load skills, they spawn sub agents at runtime' — undercuts the Salt Code narrative that pre-production/repo-level governance is where you catch agentic risk; forces us to explicitly connect Salt Code to runtime feedback loops.
- [0:28:40](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1720s) Rock Lambros: 'prompt injection...is the delivery mechanism...the delivery truck' — reframes the threat model in a way that de-emphasizes API-layer detection unless we explicitly show that Salt catches the payload's downstream action, not the prompt.
- [0:29:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1752s) Rock Lambros: 'supply chain...by far probably the fastest moving attack surface' — reframes the #1 agentic problem as supply chain (skills, MCP registries, models), not API/business-logic abuse where Salt leads.
- [0:25:38](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1538s) Rock Lambros: 'the top five CVES...are all kind of semi-autonomous frameworks, not the scary fully autonomous stuff' — implies current risk is concentrated in copilots/frameworks (Zenity's turf), weakening our 'fully agentic future' urgency narrative.

## Where they left an opening
- [0:34:49](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2089s) Genii: 'the postmark MCP...new version came with a blind copy to the attacker email' — Zenity described the incident but offered no runtime detection story; Salt's AG-DR behavioral baselining would have caught the anomalous BCC exfiltration at the API layer. Perfect case-study hook.
- [0:14:06](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=846s) Rock Lambros: 'coding agent wiping production databases' and [0:14:12] 'emails that have walked out confidential data out of a co-pilot with zero clicks' — Zenity cites the incidents but doesn't claim they stopped them; opening to say 'these are exactly action-layer API events Salt blocks.'
- [0:37:00](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2220s) Rock Lambros' runtime-dependency-graph claim — Zenity has no API fabric, no MCP-server discovery outside supported SaaS, and no east-west visibility. Their 'live dependency graph' stops at the agent boundary.
- [0:42:50](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2570s) Rock Lambros: 42 instruments / 10 jurisdictions — heavy on mapping, silent on evidence generation. No cryptographically signed audit replay, no deterministic evidence for auditors — our audit defensibility gap for them still holds.
- [0:53:13](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3193s) Ariel: shadow AI 'completely ungoverned' — admission that discovery is still a hard problem; but Zenity's discovery is platform-bound (M365, Salesforce, etc.). Salt's agentless, out-of-band Illuminate sees shadow APIs and rogue MCPs Zenity can't.
- Entire webinar: zero mention of LangChain, CrewAI, Databricks, or custom agent frameworks — confirms platform lock-in gap.
- Entire webinar: no customer names, no deployment metrics, no runtime block/prevention numbers — heavy on taxonomy, light on operational proof. Contrast with our 900% F500 growth and 96% alert reduction.

## Recommended response
- Battle card update: add a 'Standards vs. Security' rebuttal module. When prospects cite Zenity's OWASP Agentic Top 10 authority, respond with: 'Taxonomy is table stakes — Salt Labs contributes to and operationalizes OWASP with runtime detections mapped 1:1 to every category, including the six where injection appears.' Include the Postmark MCP incident as a case where Zenity's taxonomy described the risk while Salt's behavioral baselining would have detected the BCC exfiltration in-flight.
- Blog / POV piece: 'The Live Dependency Graph Stops at the Agent Boundary.' Take Rock's [0:37:12] quote head-on: agree that agents assemble dependencies at runtime, then show that Zenity's graph only sees dependencies inside supported SaaS platforms, while Salt's Agentic Security Graph correlates LLM → MCP → API → identity across LangChain, CrewAI, Databricks, and custom stacks. Publish side-by-side coverage matrix.
- Sales talking point + email sequence for Microsoft-heavy prospects being courted by Zenity: 'Zenity will govern the copilots. Ask them who governs the internal APIs those copilots call, the MCP servers your devs stood up last quarter, and the LangChain pilots in your data team. That's where the wipes, exfils, and prod-DB incidents actually happen — and that's Salt.' Pair with a one-pager listing the 11 head-to-head capability gaps and the Postmark MCP walkthrough.
