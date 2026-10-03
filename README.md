# x4-agent-router

**Intelligent model & tool router** with capability / cost / latency / reliability scoring and secure fallback for agent fleets.

Complements `x4-router-score` with a clean short-name package and fleet-ready API.

## Scoring Dimensions

- Capability match
- Estimated cost
- Latency class
- Historical reliability
- Policy constraints (autonomy level)

## Quick Start

```bash
pip install -e ".[dev]"
python -m x4_agent_router.route --task "summarize PR" --candidates gpt-4o,claude-sonnet,local-llama
```

## License

Apache-2.0
