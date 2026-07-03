AI Usage

This repository was developed by a human developer with assistance from AI tools. The notes below document which tools were used, how they were used, where they were helpful, and how outputs were verified before being accepted into the codebase.

## AI Tools Used

- ChatGPT (OpenAI): used interactively to generate and explain code snippets, design approaches, and unit tests.
- GitHub Copilot: used in-editor for completion and small refactors where it sped up routine code entry.

All AI-generated content was reviewed and edited by a human developer before inclusion.

## How AI Was Used

- Suggested application architecture and file structure (models, services, routes, templates).
- Implemented and refined business-rule validation in `services.py` (30% capacity rule, overlap checks).
- Wrote and iterated unit tests (see `tests/test_rules.py`) to verify core rules.
- Bootstrapped Jinja templates and form handlers in `templates/index.html`.
- Wrote `seed.py` to import `employees.csv` and `public_holidays.json` into the demo database.
- Helped draft commit messages and repository documentation.

## Two Most Useful Prompts

### Prompt 1
"Design a Flask application for a leave management system with a clean project structure, separating routes, business logic, database models, and templates."

Why it was useful:

This prompt established a modular architecture (models, services, routes, templates) that made the code easier to test and maintain.

### Prompt 2
"Implement the business rule that no more than 30% of a team may be on leave on the same working day, taking weekends, public holidays, and overlapping leave requests into account."

Why it was useful:

Provided a concrete starting point for the core validator logic, which was adapted and hardened to meet project requirements.

## Example Where AI Was Wrong

AI suggested mixing direct route registration with Blueprints at an intermediate stage. That would have introduced circular imports and maintainability issues. The developer standardized on a Blueprint-based structure and refactored code to avoid import cycles.

## Verification Process

AI outputs were not accepted blindly. Verification steps included:

- Running the application after major changes and validating UI flows.
- Running unit tests against an in-memory SQLite DB (`python -m unittest discover`).
- Manual inspection of generated code and adjusting for style, correctness, and edge cases.
- Ensuring `seed.py` correctly populates the demo DB from `employees.csv` and `public_holidays.json`.

## Reproducibility and Review Guidance

- To reproduce the seeded demo data run:

```powershell
python seed.py
python app.py
# then open http://127.0.0.1:5000
```

- The unit tests are independent of `seed.py` and use an isolated in-memory database.
- If requested, a per-commit annotation can be added to indicate which commits were AI-assisted.

If you want further detail (for example, a per-commit breakdown of AI assistance or the exact prompts used), tell me and I will add it.
