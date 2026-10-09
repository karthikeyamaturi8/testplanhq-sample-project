# TestPlanHQ Sample Project

A small sample repository showing example content for the main TestPlanHQ test types.

## Suggested structure

```text
testplanhq-sample-project/
├── tests/
│   ├── hurl/
│   ├── tavern/
│   ├── bruno/
│   ├── playwright/
│   ├── playwright-lite/
│   ├── adhoc/
│   ├── sql/
│   └── ai-conversation/
├── environments/
└── README.md
```

## Example environment variables

Create these in TestPlanHQ's Environment screen, not as real secrets in Git:

- `BASE_URL`
- `SQL_TARGET_URL`
- `AI_CONVERSATION_TARGET_URL`

Example values can be found in `environments/example.env`.
