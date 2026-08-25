# Contributing

Contributions should solve a demonstrated creator problem and remain reviewable.

1. Open an Issue describing the user scenario, expected output, and known risks.
2. Keep each Pull Request focused on one Skill or one infrastructure change.
3. Declare any requested shell, network, filesystem, credential, or publishing capability.
4. Include at least one normal case and one failure or boundary case under the Skill's `tests/` folder.
5. Run `python scripts/validate_repository.py` and include the result in the PR.

Do not contribute copied prompts, private material, unlicensed datasets, tracking code, secret collection, download-and-execute commands, or instructions that bypass user consent. Maintainers may reject changes whose provenance or safety cannot be established.
