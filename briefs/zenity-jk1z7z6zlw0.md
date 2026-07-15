# jK1Z7Z6zlW0

- **Channel:** 
- **URL:** https://www.youtube.com/watch?v=jK1Z7Z6zlW0

## Overview
A Zenity-hosted webinar featuring Karen Katz (Zenity) alongside OWASP GenAI Security Project contributors Rock Lambros, Ariel (Pillar Security), and Evgeniy Kokuykin (Raft/ITMO) unveiling the second version of the OWASP 'State of Agentic AI Security and Governance' report. The discussion covered updated agent taxonomy, threat analysis, MCP/protocol landscape, AI-SBOM, regulatory shifts, and an enterprise adoption maturity model.

## What was covered
- Introduction of the 2026 v2 report as a full rebuild grounded in documented incidents/CVEs rather than last year's forecasts
- Revised agent taxonomy with new axes: agent type/domain, build method (framework vs. low-code/no-code), composition (single vs. multi-agent), and cross-cutting autonomy level
- Key trends: safety-security convergence, non-human/agent identities, regulatory landscape, and explainability challenges
- Threat analysis reframing prompt injection as a delivery mechanism/TTP rather than a standalone vulnerability, plus supply chain as fastest-moving attack surface (Postmark MCP incident referenced)
- MCP protocol adoption explosion vs. slower A2A adoption; pointer to OWASP MCP cheat sheet
- AI-SBOM discussion led by Helen Oakley's work — extending SBOM to model lineage and runtime-assembled dependency graphs
- Deep dive on regulation: EU AI Act Article 72 (implicit drift detection), DORA 4-hour clock, NIS2, US executive orders, CISA BOD, and shift to EU no-fault product liability
- New Enterprise Adoption Maturity Model mapping tiers (shadow AI → citizen developer → in-house → multi-agent → federated) against governance maturity

## Direct competitor mentions
_None._

## Indirect mentions
- [0:28:25] 'Everyone calls prompt injection the vulnerability and it's not... it's the delivery mechanism' — reframes traditional API/WAF signature or prompt-filter vendors as missing the point; positions Zenity's behavioral/intent model as the correct lens.
- [0:29:22] 'Attackers stopped attacking the agent and started poisoning what the agent trusts' — implicit swipe at traffic/API-layer defenders (like Salt) by suggesting the real battlefield is tool descriptions, memory, and dependencies inside the agent runtime.
- [0:37:01] 'Traditional SBOM is a buildtime list. Agents don't work that way... your buildtime inventory describes a system that stopped existing the moment the agent ran' — undercuts shift-left/pre-production governance narratives, which is exactly where Salt Code plays.
- [0:42:44] 'No regulator actually wrote the words do drift detection, but how are you going to start your 4-hour clock on something that makes automated decisions... leveraging a deterministic detection mechanism it's going to be really difficult' — veiled dismissal of deterministic/rule-based detection (implying Salt-style behavioral baselining alone is insufficient without agent-intent context).
- [0:53:44] 'The very first thing that needs to be taken into consideration really is a discovery phase' — positions Zenity's Observe pillar as the entry point, implicitly reframing API discovery vendors as downstream.

## Where they touched our territory
- [0:14:06] 'We've seen a coding agent wiping production databases... emails that have walked out confidential data out of a copilot with zero clicks' — action-layer damage examples that are exactly Salt's runtime/API-fabric turf, yet framed as agent-behavior problems.
- [0:29:57] 'Agentic adoption... has just created a huge target not just on the agents themselves but also on the infrastructure that supports them' — acknowledges infrastructure/API layer risk, our home ground.
- [0:30:51] 'MCP, new threat models associated with MCPs... skill registries... plugins for coding agents... new supply chains being quickly adopted and are not necessarily being scrutinized' — overlaps directly with Salt's Unified Agentic Discovery and rogue MCP detection.
- [0:34:52] 'The most notable incident on MCP... postmark MCP... new version came with only one line added, blind copy to the attacker email' — supply-chain MCP compromise story that Salt's discovery + behavioral runtime is designed to catch.
- [0:38:39] 'Companies... don't even know what MCPs are in use... who are the agents that using them' — Karen explicitly names the discovery gap Salt's Illuminate/AG-SPM solves at the API fabric layer.
- [0:44:11] 'Article 72 quietly demands drift detection without using the words' — API drift and posture drift is a core AG-SPM pillar for Salt.
- [0:53:37] 'A lot of people... admit that within their organizations they have a lot of shadow AI being deployed... the very first thing... is a discovery phase' — mirrors Salt's shadow/zombie API and rogue MCP discovery story.

## Where they contradicted us
- [0:37:01] 'Traditional SBOM is a buildtime list... your buildtime inventory describes a system that stopped existing the moment the agent ran' — directly challenges the value of Salt Code's pre-production/shift-left governance narrative.
- [0:39:09] 'AI-SBOMs are relatively immature... the actual standards, be it CycloneDX or SPDX, don't quite reflect the needs... a modification from just describing the components to actually describing the behavior' — positions behavior-first (Zenity's turf) as superior to component/API inventory (our discovery framing).
- [0:28:41] 'Injection showing up in six out of the 10 categories... treating it as a checkbox that you can solve, you're just going to waste time... figure out how to contain the blast radius' — implicitly dismisses signature/pattern-based API defenses in favor of blast-radius containment at the agent layer.
- [0:42:57] 'How are you going to start your 4-hour clock on something that makes automated decisions... leveraging a deterministic detection mechanism it's going to be really difficult' — undermines deterministic API monitoring as insufficient for regulatory incident clocks.

## Where they left an opening
- No mention of east-west or internal API traffic — Zenity's model still stops at the SaaS/platform boundary; Salt can own 'what happens after the agent calls the API.'
- No answer for heterogeneous/custom agent frameworks (LangChain, CrewAI, Databricks) — panel talked exclusively about MCP, Copilot-adjacent supply chains, and OWASP taxonomy without naming coverage for custom stacks.
- AI-SBOM discussion admitted the standards don't yet describe runtime behavior — Salt's Agentic Security Graph (LLM→MCP→API correlation) is exactly the runtime-behavior grammar they say is missing.
- Regulatory incident clocks (DORA 4-hour, NIS2 24-hour) were flagged as hard without continuous oversight — Salt's cloud-scale behavioral baselining and 96% alert reduction is a direct answer; Zenity offered no concrete detection mechanism.
- Postmark MCP incident was cited but no product answer was given for how Zenity would have detected the malicious BCC line at the network/API layer — Salt's out-of-band traffic analysis would.
- Shadow AI discovery was named as 'step zero' but Zenity's model requires platform connectors/device agents; Salt's agentless, out-of-band discovery is a cleaner story to lead with.
- No customer proof points, no metrics, no named enterprise deployments — the entire session was OWASP-flavored thought leadership with zero competitive proof.

## Recommended response
- Publish a Salt Labs blog titled 'From Buildtime to Runtime to Action-Time: Why Agentic SBOMs Must Include the API Fabric' — directly rebut Rock Lambros's claim that buildtime inventories are obsolete by showing how Salt Code + Illuminate + AG-DR produce a continuously reconstructed runtime dependency graph (Agentic Security Graph) that Zenity's platform-bound Observe cannot.
- Update the Zenity battle card with a new 'Regulatory Clock' section: map DORA 4-hour, NIS2 24-hour, EU AI Act Article 72 drift-detection to Salt's AG-SPM continuous posture + behavioral baselining, and call out that Zenity offered no deterministic detection mechanism on-record — pair with the Postmark MCP incident as a concrete 'Salt would have caught the BCC exfiltration at the API layer' talk track.
- Arm AEs with a 'Shadow AI Discovery Bake-off' one-pager: lead every Zenity-competitive deal with a free Illuminate scan showing shadow APIs, rogue MCP servers, and non-Microsoft agent frameworks (LangChain/CrewAI/Databricks) that Zenity's connector-and-device-agent model structurally cannot see — turning their own 'step zero is discovery' quote against them.
