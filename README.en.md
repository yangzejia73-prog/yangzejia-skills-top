# Creator Skills CN

Open-source Agent Skills for Chinese content creators. The repository turns topic research, evidence-aware writing, cross-platform adaptation, and pre-publication review into reusable, auditable workflows.

The project prioritizes source transparency, separation of fact and opinion, least privilege, and final human review. It does not promise viral performance or treat generated claims as verified facts.

## Included Skills

- `topic-research`: develop evidence-aware topic candidates.
- `source-backed-outline`: build an outline from supplied sources.
- `xiaohongshu-draft`: draft a Xiaohongshu post for human editing.
- `wechat-article`: draft a source-transparent WeChat article.
- `content-repurpose`: adapt one source into platform-specific formats.
- `content-risk-review`: flag factual, privacy, compliance, and high-stakes risks.

All six Skills default to no shell execution, network access, credential access, or filesystem writes. See [README.md](README.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [SECURITY.md](SECURITY.md).

Run `python scripts/validate_repository.py` before contributing. Current status: initial public release, `v0.1.0`; no adoption or download claims are made.
