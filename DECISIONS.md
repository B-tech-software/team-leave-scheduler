## Decision 1: 30% capacity rule

I use `max(1, floor(team_size * 0.3))`.

Why: it is simple, strict, and easy to explain.

Alternative considered: round up. Rejected because it would allow too much leave on small teams.

## Decision 2: Apply the rule per working day

I check every working day in the requested range.

Why: each day is a separate capacity decision.

Alternative considered: check the whole range as one block. Rejected because it hides the actual overloaded day.

## Decision 3: Pending requests do not block overlap or capacity

I only count approved requests when checking overlap and team capacity.

Why: approved leave is the final state, while pending requests can still be rejected later.

Alternative considered: count pending requests too. Rejected because it would make normal review harder and more restrictive.
