# AMA: Inside the OWASP State of Agentic AI Security & Governance

- **Channel:** Zenity
- **URL:** https://www.youtube.com/watch?v=jK1Z7Z6zlW0

## Overview
This webinar was a launch discussion for the second version of the OWASP 'State of Agentic AI Security and Governance' report. Zenity's Karen Katz moderated a panel with co-authors from OWASP working groups, Pillar Security, and Hive Trace covering taxonomy updates, threat analysis, MCP/supply chain risks, AI-BOMs, regulatory shifts, and a new enterprise adoption maturity model.

## Speakers
- Karen Katz — Director for AI Security, Zenity (and OWASP lead for Agentic Top 10) ([search](https://www.google.com/search?q=Karen+Katz+Director+for+AI+Security+Zenity+linkedin))
- Rock Lambros — Director of AI Standards and Governance, Zenity (OWASP GenAI Security Project core team) ([search](https://www.google.com/search?q=Rock+Lambros+Director+of+AI+Standards+and+Governance+Zenity+linkedin))
- Ariel — Founding Engineer & AI Security Researcher, Office of the CTO, Pillar Security ([search](https://www.google.com/search?q=Ariel+Founding+Engineer+%26+AI+Security+Researcher+Office+of+the+CTO+Pillar+Security+linkedin))
- Evgeniy (Gani) — AI Security Research lead at ITMO University; Founder, Hive Trace ([search](https://www.google.com/search?q=Evgeniy+AI+Security+Research+lead+at+ITMO+University%3B+Founder+Hive+Trace+linkedin))

## What was covered
- Why a second version of the OWASP State of Agentic AI report was needed — shift from forecasted risks to documented CVEs and real incidents
- Updated agent taxonomy with new axes: agent type/domain, build method (framework vs. low-code/no-code), composition (single vs. multi-agent), and crosscutting autonomy level
- Threat analysis update — prompt injection reframed as a delivery mechanism/TTP rather than a vulnerability, showing up across 6 of 10 categories
- Supply chain as the fastest-moving attack surface, with tool descriptions, memory files, MCP servers, skills registries, and plugin marketplaces as new attack vectors
- MCP protocol adoption explosion vs. A2A's slower uptake; Postmark MCP incident as canonical example
- AI-BOM / AISBOM discussion — need to shift from buildtime component inventories to runtime behavioral descriptions of what agents assemble
- Regulatory landscape: EU AI Act Article 72 (drift detection), DORA/NIS2/state incident clocks, EU no-fault product liability, and CISA BOD on AI vuln patching
- New Enterprise Adoption Maturity Model — tiers from Shadow AI through multi-agent and federated deployments, mapped to governance maturity

## Direct competitor mentions
_None._

## Indirect mentions
- [0:28:25](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1705s) 'Everyone calls prompt injection the vulnerability and it's not... it's the delivery mechanism.' — Reframes the traditional API/WAF/prompt-filter market (including Salt-adjacent runtime tools) as misunderstanding the real threat, positioning Zenity's agent-behavior lens as more sophisticated.
- [0:29:12](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1752s) 'Attackers stopped attacking the agent and started poisoning what the agent trusts... the agent's own capability became the weapon.' — Implicit swipe at traffic/API-layer defenders (Salt's territory) as looking in the wrong place; positions the agent-trust boundary (Zenity's turf) as the real battlefield.
- [0:30:38](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1838s) 'MCP... skill registries... plugins for coding agents... these are all new supply chains... not necessarily being scrutinized well.' — Reframes API security as insufficient for the agentic supply chain, hinting that incumbents (Salt) miss these new surfaces.
- [0:37:00](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2220s) 'Traditional SBOM is a buildtime list. Agents don't work that way... the dependency graph assembles itself live with every execution.' — Undercuts static/shift-left tooling and any pre-production-only view; indirectly targets legacy API discovery approaches.
- [0:42:44](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2564s) 'How are you going to start your 4-hour clock on something that makes automated decisions... leveraging a deterministic detection mechanism it's going to be really difficult.' — Positions deterministic/rule-based detection (framed as legacy runtime security) as unfit for regulatory incident clocks; favors Zenity's behavioral/intent story.
- [0:53:44](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3224s) 'The very first thing that needs to be taken into consideration really is a discovery phase.' — Frames discovery as Zenity's opening move, implicitly claiming the discovery narrative Salt owns for APIs.

## Where they touched our territory
- [0:30:57](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1857s) 'MCP... new threat models associated with MCPs, whether it be skill registrations, skill registries and how skills can be malicious themselves.' — Directly overlaps Salt's Unified Agentic Discovery (Illuminate) and rogue MCP discovery pillar.
- [0:36:11](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2171s) 'AI-BOMs extends it to model versions and lineage... you need that baseline.' — Overlaps Salt's posture management and inventory story (AG-SPM).
- [0:38:00](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2280s) 'Companies... don't even know what MCPs are in use... who are the agents that using them.' — Precisely the problem Salt's Agentic Security Graph and Illuminate are built to solve, but framed as a Zenity/OWASP problem statement.
- [0:42:00](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2520s) 'Article 72 quietly demands drift detection without using the words.' — Directly maps to Salt's AG-SPM compliance-governance pillar (PCI, GDPR, EU AI Act drift detection).
- [0:53:39](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=3219s) 'Discovery phase where you're able to identify what's going on, how is it being deployed, what's it connected to.' — Squarely Salt Illuminate territory, reclaimed under Zenity's Observe pillar.

## Where they contradicted us
- [0:28:41](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1721s) 'Treating it [prompt injection] as a checkbox that you can solve... you're just going to waste time but instead figure out how to contain the blast radius around it.' — Implicitly argues that behavioral runtime detection at the API layer (Salt) is insufficient without agent-level blast-radius containment.
- [0:37:14](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2234s) 'Your buildtime inventory describes a system that stopped existing kind of the moment that the agent ran.' — Undercuts pre-production/shift-left narratives including Salt Code's positioning as a design-time control.
- [0:42:56](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2576s) 'How are you going to start your 4-hour clock on something that makes automated decisions... leveraging a deterministic detection mechanism it's going to be really difficult.' — Frames Salt-style baseline/behavioral runtime as too slow or too deterministic for modern regulatory clocks.

## Where they left an opening
- [0:32:00](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=1920s) The panel admits A2A and multi-agent systems are barely deployed in practice — Salt can own the future-proof, platform-agnostic multi-agent correlation story (Agentic Security Graph) that Zenity concedes it doesn't yet see in production.
- [0:35:00](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2100s) Postmark MCP incident cited as canonical — Zenity has no answer for detecting a malicious MCP outside its supported SaaS platforms; Salt Illuminate + AG-DR can catch a rogue MCP anywhere it talks to APIs.
- [0:38:20](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2300s) Panel admits enterprises 'don't even know what MCPs are in use' — direct opening for Salt's Unified Agentic Discovery (agentless, out-of-band) vs. Zenity's platform-connector/device-agent model.
- [0:40:11](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2411s) Ariel notes SBOM/AIBOM standards need to describe runtime behavior, not just components — Salt's runtime behavioral baselining (AG-DR) and Agentic Security Graph are literally that runtime grammar; Zenity has no equivalent action-layer view.
- [0:42:11](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2531s) EU AI Act Article 72 drift detection called out but no vendor solution offered — Salt AG-SPM maps live configs to EU AI Act, a concrete regulatory hook Zenity doesn't own.
- [0:47:56](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=2876s) Discussion of insurance and contractual requirements driving AI security — Salt's Fortune 500 proof points and 96% alert reduction are stronger enterprise-procurement ammunition than Zenity's mostly Microsoft-stack story.
- The entire conversation stayed above the API/action layer — no discussion of what happens when an agent's action reaches a downstream API, business logic, or east-west traffic. This is Salt's entire product.

## Recommended response
- Publish a Salt Labs blog titled 'From Buildtime to Runtime to Action-Layer: Why Agentic SBOMs Must Include the API Fabric' — anchor to the OWASP report's own admission that dependency graphs assemble live at runtime, and show how Salt's Agentic Security Graph is the missing runtime grammar Ariel described.
- Update the Zenity battle card with a new 'Postmark MCP test' section: ask prospects whether Zenity would have caught the malicious MCP if it lived outside a supported SaaS platform — pair with Salt's rogue-MCP discovery demo and the '11 capabilities Zenity lacks' table.
- Arm the field with a regulator-driven talk track built around EU AI Act Article 72 + DORA 4-hour clock: position Salt AG-SPM (drift detection mapped to frameworks) and AG-DR (behavioral baselining with cryptographically signed audit replay) as the only stack that answers the incident-clock question the OWASP panel raised but did not solve.
