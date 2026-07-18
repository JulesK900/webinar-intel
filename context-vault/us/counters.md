# Our differentiators and known attack surfaces

## Differentiators

* **Technical / architectural edge:** Salt utilizes a zero-latency, out-of-band deployment via its API Context Engine (ACE), while uniquely deploying the Agentic Security Graph to correlate the full sequence of intent from the LLM (the brain) to the MCP server (the hands) to the API (the action layer).
* **Data or scale advantage:** Built on a cloud-scale big data architecture trained across thousands of enterprise environments, the platform effortlessly handles massive traffic volumes (e.g., 20,000+ requests per second) while reducing SOC alert fatigue by up to 96%.
* **Ecosystem or integration edge:** Deep, certified native integrations with major cloud and security platforms, including frictionless API discovery via CrowdStrike Falcon Next-Gen SIEM and bidirectional toxic-combination mapping with the Wiz WIN platform.
* **Category leadership / brand credibility:** Salt is the most heavily funded pure-play API security vendor ($281M raised, $1.4B valuation) and maintains Salt Labs, the industry's premier dedicated threat research division known for uncovering massive global vulnerabilities like the OAuth "Pass-The-Token" flaws.

## Sore spots / where competitors love to attack

* **Price / packaging:** Often perceived as a premium, enterprise-focused solution, creating a potential pricing disadvantage when competing for smaller teams or startups against bundled WAFs or basic gateway protections.
* **Coverage gaps:** Lacks native, inline blocking capabilities within the initial request path; the platform relies on out-of-band analysis and integrations with third-party firewalls or API gateways to execute blocking commands.
* **"Legacy" or "first-generation" framing:** Competitors focused strictly on shift-left testing (like APIsec or 42Crunch) or deep eBPF tracing (like Traceable AI) frequently frame Salt's traditional runtime strength as trailing in pre-production design testing, though the recent launch of Salt Code is positioned to mitigate this.
* **Emerging areas where you're still catching up:** Customer reviews occasionally note friction and a steep learning curve when integrating Salt with complex, non-standard authentication frameworks (such as Okta with DPoP).
