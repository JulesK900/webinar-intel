# AMA: Inside the OWASP State of Agentic AI Security & Governance

- **Channel:** Zenity
- **URL:** https://www.youtube.com/watch?v=jK1Z7Z6zlW0

## Overview
This webinar was a launch discussion for the second version of the OWASP 'State of Agentic AI Security and Governance' report, hosted by Zenity's Karen Katz with co-leads Rock Lambros (Zenity), Ariel Fung (Pillar Security), and Evgeniy Kokuykin (Raft/ITMO). The panel walked through updates to the agent taxonomy, threat analysis, MCP/protocol landscape, AI SBOMs, regulatory shifts, and a new enterprise adoption maturity model, framing agentic AI risk as an urgent, fast-moving governance problem.

## Speakers
- Karen Katz — Director for AI Security, Zenity (and OWASP Agentic Top 10 lead) ([LinkedIn](https://www.linkedin.com/search/results/people/?keywords=Karen+Katz+Director+for+AI+Security+Zenity+%28and+OWASP+Agentic+Top+10+lead%29))
- Rock Lambros — Director of AI Standards and Governance, Zenity (co-lead OWASP GenAI Security Project Agentic Security Initiative) ([LinkedIn](https://www.linkedin.com/search/results/people/?keywords=Rock+Lambros+Director+of+AI+Standards+and+Governance+Zenity+%28co-lead+OWASP+GenAI+Security+Project+Agentic+Security+Initiative%29))
- Ariel Fung — Founding Engineer & AI Security Researcher, Office of the CTO, Pillar Security ([LinkedIn](https://www.linkedin.com/search/results/people/?keywords=Ariel+Fung+Founding+Engineer+%26+AI+Security+Researcher+Office+of+the+CTO+Pillar+Security))
- Evgeniy Kokuykin — AI Security Research Lead, ITMO University / Hive Trace ([LinkedIn](https://www.linkedin.com/search/results/people/?keywords=Evgeniy+Kokuykin+AI+Security+Research+Lead+ITMO+University+%2F+Hive+Trace))

## What was covered
- Why a v2 of the State of Agentic AI report was needed — shift from forecasts to documented CVEs and real incidents (e.g., coding agent wiping prod DB, zero-click Copilot data exfiltration).
- Updated agent taxonomy along axes of agent type, build method (code vs low/no-code), composition (single vs multi-agent), and crosscutting autonomy level as a risk lens.
- Threat analysis: prompt injection reframed as a delivery mechanism / TTP, not a vulnerability, mapping to 6 of 10 categories; supply chain elevated as fastest-moving attack surface.
- Agentic protocol landscape: MCP adoption exploded in a year while A2A remains largely theoretical; Postmark MCP incident highlighted as canonical supply chain compromise.
- AI SBOM / AIBOM discussion led by referencing Helen Oakley's work — argues buildtime SBOMs are insufficient because agents assemble dependencies at runtime.
- Regulatory update: 42 instruments across 10 jurisdictions mapped, EU AI Act Article 72 implicit drift-detection requirement, DORA/NIS2/state incident clocks, and EU no-fault product liability.
- New Enterprise Adoption Maturity Model — tiers from shadow AI up through federated multi-agent systems, mapped against governance maturity.
- Discovery of shadow AI framed as the mandatory first step before any governance can be applied.

## Direct competitor mentions
- [0:34:52](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2092s) 'The most notable incident on MCP is we widely reference is the postmark MCP when this server was legitimate for many releases... at some point the new version came with only one line added, blind copy to the attacker email.' — Zenity/panel citing Postmark MCP compromise as canonical supply chain risk.
- [0:36:11](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2171s) 'This is all about calling our friend Helen Oakley who is leading the OWASP GenAI security project AI SBOM / AIBOM initiative.' — direct namedrop of OWASP AIBOM leader.
- [0:28:37](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1717s) 'The LLM Top 10 update that I'm co-leading with Steve Wilson' — Rock positioning Zenity leadership across OWASP LLM Top 10.

## Indirect mentions
- [0:28:26](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1706s) 'Everyone calls prompt injection the vulnerability and it's not... it's the delivery mechanism.' — implicit swipe at prompt-firewall / content-moderation vendors and, by extension, traffic-inspection tools that treat injection as a signature to filter.
- [0:29:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1752s) 'Attackers stopped attacking the agent and started poisoning what the agent trusts — tool descriptions, memory files, dependencies.' — reframes the attack surface away from API/traffic layers (Salt's strength) toward the agent's trust graph (Zenity's turf).
- [0:37:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2232s) 'Your buildtime inventory describes a system that stopped existing the moment the agent ran.' — indirect shot at shift-left / SBOM-style and API-inventory approaches, implying static discovery (a Salt Illuminate value prop) is obsolete.
- [0:30:31](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1831s) 'MCP... skill registries... plugins for coding agents. These are all new supply chains that are being quickly adopted and are not necessarily being scrutinized.' — positions Zenity's platform-native discovery as the answer, implicitly dismissing API-centric discovery tools.
- [0:43:44](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2624s) 'Article 72 quietly demands drift detection without using the words.' — frames continuous agent behavioral oversight (Zenity's AIDR pitch) as the regulatory imperative, sidelining API posture drift (AG-SPM).

## Where they touched our territory
- [0:14:06](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=846s) 'A coding agent wiping production databases after being told repeatedly not to touch anything... emails that have walked out confidential data out of a copilot with zero clicks.' — these are exactly action-layer / API-fabric outcomes that Salt AG-DR is built to detect; Zenity claims them as their incident narrative.
- [0:29:57](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1797s) 'Agentic adoption has just created a huge target not just on the agents themselves but also on the infrastructure that supports them.' — 'infrastructure' = APIs/MCP, which is Salt's Agentic Security Graph territory.
- [0:37:25](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2245s) 'The shift has to be from what components are present to what can get assembled at runtime and under whose authority.' — directly overlaps Salt's Unified Agentic Discovery (Illuminate) and runtime correlation claim.
- [0:39:47](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2387s) 'A modification from just describing the components to actually describing the behavior of these systems... the grammar that allows you to describe how [agents] behave in production.' — overlaps Salt's runtime behavioral baselining pillar (AG-DR).
- [0:53:35](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3215s) 'The very first thing that needs to be taken into consideration really is a discovery phase where you're able to identify what's going on, how is it being deployed, what's it connected to.' — Salt Illuminate's exact pitch; Zenity is planting a flag on discovery.

## Where they contradicted us
- [0:28:26](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1706s) 'Prompt injection... it's the delivery mechanism... the damage maps to the categories we already had.' — implicitly argues that focusing on the API/action layer where damage occurs is insufficient without agent-intent context, softening our 'behavior becomes damage at the API' framing.
- [0:37:04](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2224s) 'Traditional SBOM is a buildtime list. Agents don't work that way — they discover tools, load skills, spawn sub-agents at runtime.' — challenges any static-inventory positioning, including how Salt discovery is sometimes perceived.
- [0:42:38](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2558s) 'No regulator actually wrote the words do drift detection, but how are you going to start your 4-hour clock on something that makes automated decisions?' — positions agent-behavior drift (Zenity's step-level monitoring) as the compliance-critical capability, not API posture drift.
- [0:53:16](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3196s) 'A lot of people... admit that within their organizations they have a lot of shadow AI being deployed.' — Zenity claiming the shadow-AI discovery narrative, which competes directly with Salt's shadow/zombie API discovery story.

## Where they left an opening
- Zero mention of the API layer, business logic abuse, or east-west API traffic — every example (Copilot exfil, coding agent wiping DBs, Postmark MCP) actually executes damage at the API/action layer Salt owns.
- MCP discussion stayed at the protocol/supply-chain narrative; no story about how Zenity monitors MCP servers at runtime or discovers rogue MCPs outside their supported SaaS platforms.
- No coverage of LangChain, CrewAI, Databricks, or custom agent frameworks — reinforces Zenity's platform-bound coverage gap.
- Heavy reliance on OWASP thought leadership and 'research' branding, but no customer proof points, scale metrics, or deployment numbers cited during the hour.
- Regulatory section leaned on EU AI Act Article 72 drift detection but never explained how Zenity actually satisfies it operationally — opening for Salt AG-SPM to claim the concrete compliance mapping (PCI, GDPR, EU AI Act).
- AIBOM discussion admitted the standards (CycloneDX, SPDX) don't yet describe agent behavior — Salt can claim the Agentic Security Graph already provides that runtime behavioral grammar.
- No mention of inline enforcement or blocking — Zenity's own gap (device-agent dependency, SaaS boundary) went unaddressed.

## Recommended response
- Publish a Salt Labs blog titled 'When Agent Intent Becomes API Damage: A Post-Mortem of the 2025 Agentic Incidents' — walk through the exact examples the panel cited (Copilot zero-click exfil, coding agent DB wipe, Postmark MCP) and show how each was consummated at the API/MCP layer Zenity doesn't cover; anchor to Salt's Agentic Security Graph (LLM → MCP → API).
- Update the Zenity battle card with two new objection-handlers: (1) 'Prompt injection is a delivery mechanism' — response: agree, and note the payload lands at the API, which is where Salt detects business-logic abuse Zenity cannot see; (2) 'Buildtime SBOM is dead' — response: Salt Illuminate + ACE do runtime dependency assembly discovery continuously, no device agent required.
- Arm the field with an EU AI Act Article 72 talking point: position AG-SPM as the concrete drift-detection and evidence layer regulators will actually ask for (cryptographically signed audit trail, PCI/GDPR/EU AI Act mapping), contrasted against Zenity's platform-bound behavioral monitoring that goes dark outside M365/Azure/Salesforce.
