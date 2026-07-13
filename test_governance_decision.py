from models.governance_decision import GovernanceDecision

decision = GovernanceDecision(
    allowed=True,
    risk="LOW",
    reason="Read operations are permitted."
)

print(decision)