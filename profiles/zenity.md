# Competitor — Zenity

## Who they are

Zenity is a security platform for AI agents and low-code / no-code business apps. They focus on securing agentic AI and the "citizen developer" surface — Copilot Studio, Power Platform, ServiceNow, Salesforce Flow, and custom agents built on top of LLMs.

## Aliases / names to watch for

- Zenity
- Zenity Labs (their research arm)
- "AI agent security" (their category framing)

## Pillars they lean on

- **AI agent security posture management (AISPM)** — inventory + risk scoring for agents.
- **Agent runtime protection** — detect prompt injection, data exfil, tool abuse.
- **Low-code/no-code app security** — Power Platform, Copilot Studio, Salesforce.
- **Governance for citizen developers** — guardrails on who can build what.

## Positioning language they use

- "Secure every AI agent."
- "Agentic AI security."
- "AI security for the enterprise."
- "From build time to run time."

## Known claims / customer names to listen for

- Fortune 500 wins in financial services and healthcare.
- Microsoft Copilot Studio partnership.
- Zenity Labs research (public vulnerability disclosures on Copilot, ChatGPT plugins, etc.).

## Where they overlap with us

- **AI agent identity** — they secure the agent behavior; we secure the agent's non-human identity (credentials, tokens, permissions).
- **Runtime detection** — their agent runtime protection vs. our AIDR.
- **Governance** — both talk lifecycle governance, but for different objects (them: the agent; us: the identity the agent uses).

## Where they don't overlap

- No secret scanning across code/cloud/SaaS.
- No broad NHI inventory (service accounts, API keys, OAuth tokens outside agents).
- No IAM fabric integration at SailPoint's scale.

## Veiled-attack phrases to flag

- "Legacy identity vendors" — likely us / SailPoint.
- "Vault-centric approaches" — swipe at secret managers, indirectly at NHI vendors.
- "Human identity tools bolted on" — direct dig at IAM incumbents adding NHI.
- "Point solutions for secrets" — swipe at pure-play secret scanners.
