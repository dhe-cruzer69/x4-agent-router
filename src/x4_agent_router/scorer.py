"""Simple multi-dimension scorer."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict


@dataclass
class Candidate:
    name: str
    capability: float  # 0-1
    cost: float        # lower better
    latency: float     # lower better
    reliability: float # 0-1


def score(c: Candidate, weights: Dict[str, float] | None = None) -> float:
    w = weights or {"capability": 0.4, "cost": 0.2, "latency": 0.2, "reliability": 0.2}
    # normalize cost/latency as inverse
    return (
        w["capability"] * c.capability
        + w["reliability"] * c.reliability
        - w["cost"] * c.cost
        - w["latency"] * c.latency
    )
