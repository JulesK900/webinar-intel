# Webinar briefs

Full competitive briefs from every run, newest first. Individual briefs also live in `briefs/`.

## 2026-07-18 — AMA: Inside the OWASP State of Agentic AI Security & Governance (vs zenity)

- **Channel:** Zenity
- **URL:** https://www.youtube.com/watch?v=jK1Z7Z6zlW0

### Overview
This webinar presented the second version of the "State of Agentic AI" report, released by OASP (Open Worldwide Application Security Project). The panelists discussed major updates to the report including a rebuilt threat analysis based on documented incidents, new taxonomy for classifying agents, and practical guidance for enterprise adoption of agentic systems.

### Speakers
- Karen Katz — Director for AI Security and OASP Agentic Top 10, Zenity ([search](https://www.google.com/search?q=Karen+Katz+Director+for+AI+Security+and+OASP+Agentic+Top+10+Zenity+linkedin))
- Rock Lamros — Director of AI Standards and Governance, Zenity ([search](https://www.google.com/search?q=Rock+Lamros+Director+of+AI+Standards+and+Governance+Zenity+linkedin))
- Ariel — Founding Engineer and AI Security Researcher, Office of the CTO at Pillar Security ([search](https://www.google.com/search?q=Ariel+Founding+Engineer+and+AI+Security+Researcher+Office+of+the+CTO+at+Pillar+Security+linkedin))
- Genei — AI Security Research, ITMO University and Hive Trace ([search](https://www.google.com/search?q=Genei+AI+Security+Research+ITMO+University+and+Hive+Trace+linkedin))

### What was covered
- Updated agent taxonomy with focus on agent types, domains, construction methods, and autonomy levels to help CISOs evaluate risk
- Threat analysis grounded in real documented incidents and CVEs, showing that prompt injection is a delivery mechanism rather than a standalone vulnerability
- Supply chain risks including poisoning of agent dependencies, tool descriptions, and emerging threats from MCP (Model Context Protocol) and skill registries
- AI SBOM (Software Bill of Materials) requirements adapted for agentic systems that dynamically assemble dependencies at runtime rather than at build time
- Regulatory landscape covering 42 instruments across 10 jurisdictions, with focus on incident reporting timelines (DORA 4 hours, NIS2 24 hours, California 15 days)
- Enterprise adoption maturity model mapping organizational tiers (shadow AI, platforms, citizen developers, in-house agents) to appropriate governance levels
- Key industry trends including the shift from forecastable threats to documented real-world incidents, increased adoption of agentic protocols, and the gap between current deployments and regulatory requirements

### Direct competitor mentions
- [9:53](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=593s) Karen Katz: 'I'm Karen Katz. I'm Zenity director for I security and OASPLET for the Agentic top 10' — direct self-identification as Zenity representative.
- [10:22](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=622s) Karen Katz: 'my day-to-day role is the director of AI standards and governance at Zenity and I'm also on the core team of the OASP Genai security project' — reinforces Zenity brand and positions speaker as an authority on agentic AI standards.

### Indirect mentions
_None._

### Where they touched our territory
- [9:56](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=596s) Karen Katz: 'director for I security and OASPLET for the Agentic top 10' — signals Zenity is claiming thought leadership in the agentic AI security category, which directly overlaps our Agentic Security Platform positioning.
- [10:20](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=620s) Karen Katz: 'director of AI standards and governance at Zenity' — governance framing overlaps our AG-SPM (Posture Management & Compliance Governance) pillar.

### Where they contradicted us
_None._

### Where they left an opening
- [9:56](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=596s) Karen Katz: No mention of API-layer security, MCP servers, or downstream action-layer coverage in the opening framing — reinforces our angle that Zenity's story stops at the agent/governance boundary.
- [10:26](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=626s) Karen Katz: Positioning is centered on 'AI standards and governance' and OWASP agentic top 10 — no reference to runtime behavioral threat protection at the API fabric, leaving our AG-DR and Agentic Security Graph story unchallenged.
- [10:22](https://www.youtube.com/watch?v=jK1Z7Z6zlW0&t=622s) Karen Katz: Emphasis on standards/governance credentials rather than technical depth or scale metrics — opening to contrast with Salt's big-data baselining, 20K+ RPS scale, and Salt Labs research pedigree.

### Recommended response
- Battle card update: Add a 'standards-vs-security' talking point noting Zenity leans heavily on OWASP/agentic governance credentials — sales should pivot to 'standards inform, Salt enforces at the API/MCP action layer.'
- Blog / short-form content: Publish a piece titled 'Governing Agent Intent Is Not Securing Agent Action' contrasting Zenity's governance/observability framing with Salt's LLM→MCP→API Agentic Security Graph, and tie it to the OWASP Agentic Top 10 to intercept their SEO/thought-leadership footprint.
- Sales talking point: When a prospect cites Zenity's OWASP/agentic-standards leadership, respond with 'Salt Labs uncovered the OAuth Pass-The-Token flaws and processes tens of millions of API calls daily at zero latency — we operationalize those standards at the action layer Zenity never reaches.'
