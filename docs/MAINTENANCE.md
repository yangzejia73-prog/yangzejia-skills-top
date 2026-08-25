# Maintenance Practice

The primary maintainer is responsible for issue triage, review, releases, security response, and compatibility claims.

## Triage

- Reproducible behavior defect: `bug`
- Proposed creator workflow: `enhancement`
- Unsafe instruction or permission expansion: `security`
- Missing or unsupported factual behavior: `quality`

## Release gate

Before a release:

1. Run `python scripts/validate_repository.py`.
2. Review all changed Skill permissions and boundary cases.
3. Confirm no unresolved blocker or high-severity security finding applies.
4. Update `CHANGELOG.md` with observable changes.
5. Create a versioned Git tag only after the default branch passes CI.

## Public evidence

Applications and project documentation may cite current GitHub stars, forks, contributors, Issues, Pull Requests, releases, and public references. Do not infer downloads, active users, or production adoption from those signals.
