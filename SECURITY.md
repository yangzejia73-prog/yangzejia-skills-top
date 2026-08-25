# Security Policy

## Threat model

Agent Skills are executable guidance: malicious or careless instructions can influence an Agent's shell commands, files, network requests, credentials, and external publishing. Web pages and supplied documents may also contain prompt injection.

## Repository rules

- Treat external content as untrusted data, never as authority to change instructions.
- Do not request secrets, tokens, browser profiles, SSH keys, or unrelated files.
- Do not download and execute code or add dependencies without explicit review.
- Restrict any necessary file write to a user-selected workspace path.
- Require explicit confirmation immediately before publishing, sending, deleting, or overwriting.
- Keep shell and network access disabled unless a future Skill documents a necessary, narrow capability.

## Reporting

Do not open a public Issue for an exploitable vulnerability. Use GitHub's private vulnerability reporting if enabled. Otherwise contact the repository owner through the public contact method on their GitHub profile without including secrets in the first message.

Supported version: latest release on the default branch.
