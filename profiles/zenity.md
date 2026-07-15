# Competitor — Zenity

## Who they are

Zenity is a security platform for AI agents and low-code / no-code business apps. They focus on securing agentic AI and the "citizen developer" surface — Copilot Studio, Power Platform, ServiceNow, Salesforce Flow, and custom agents built on top of LLMs.

## Aliases / names to watch for

- Zenity
- Zenity Labs (their research arm)
- "AI agent security" (their category framing)
- "AISPM" (AI Security Posture Management)
- "OWASP Agentic Top 10" (co-authored / promoted)

## Pillars they lean on

- **AI agent security posture management (AISPM)** — inventory + risk scoring for agents.
- **Agent runtime protection** — detect prompt injection, data exfiltration, tool abuse.
- **Low-code/no-code app security** — Power Platform, Copilot Studio, Salesforce.
- **Governance for citizen developers** — guardrails on who can build what.

## Positioning language they use

- "Secure every AI agent."
- "Agentic AI security."
- "From build time to run time."
- "The AI security platform for the enterprise."

## Known claims / customer names to listen for

- Fortune 500 wins in financial services and healthcare.
- Microsoft Copilot Studio partnership.
- Zenity Labs research (public vulnerability disclosures on Copilot, ChatGPT plugins, agent frameworks).

## Where they overlap with us (Salt Security)

- **APIs behind AI agents** — every agent calls APIs; they frame it as "agent behavior", we frame it as "API traffic". Same underlying attack surface, different vantage point.
- **Runtime detection** — their agent runtime protection vs. our behavioral API runtime protection.
- **Shift-left / build-time** — both preach securing before deployment; they for agents, we for APIs.
- **Discovery / inventory** — both start with "you can't secure what you can't see."

## Where they don't overlap

- No API discovery, posture, or runtime protection at the API layer.
- No coverage of traditional REST/GraphQL/gRPC APIs outside the agent context.
- No behavioral ML on API traffic at scale.
- Narrower to the agent / low-code surface; blind to the broader API estate.

## Veiled-attack phrases to flag

- "Legacy API security tools" — likely a swipe at us.
- "Traffic-focused approaches miss the agent" — reframes our strength as a weakness.
- "Signature-based detection" — misrepresents behavioral ML as static rules.
- "Not built for the AI era" — direct dig at incumbents adding AI/agent coverage.
- "Point solutions for APIs" — swipe positioning them as the broader platform.
