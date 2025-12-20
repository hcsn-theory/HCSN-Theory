🌀 HCSN Theory
Holographic Computational Spin-Networks
A computational approach to emergent spacetime, gravity, and quantum mechanics
Overview
HCSN (Holographic Computational Spin-Network) is a theoretical and computational framework proposing that:
The universe is not fundamentally geometric — spacetime, gravity, and quantum mechanics emerge from a discrete computational hypergraph governed by simple rewrite rules and information-theoretic principles.
This repository contains:
the formal axioms of HCSN
toy-universe simulations in Python
diagnostic tools to test emergence of time, space, dimensionality, and metric structure
The long-term goal is to identify the minimal rule set capable of producing a universe consistent with:
Lorentz invariance
4D spacetime
holography
quantum probability (Born rule)
Motivation
Modern physics faces several unresolved foundational problems:
Why is spacetime 4-dimensional?
Why does gravity exist and why is it universal?
Why does the universe obey quantum mechanics?
Why is the cosmological constant so small?
What existed before the Big Bang?
HCSN explores the hypothesis that these are not independent mysteries, but consequences of a deeper computational structure.
Rather than quantizing spacetime, HCSN lets spacetime emerge.
Core Principles (Axioms)
Axiom 1 — Discreteness
Reality consists of discrete events represented as vertices in a hypergraph.
There is no fundamental continuum.
Axiom 2 — Causality
Events are partially ordered by a causal relation
Axiom 3 — Minimal Dynamics
The universe evolves via local rewrite rules acting on the hypergraph.
Only two fundamental rules are assumed:
Edge Creation (spatial extension)
Vertex Fusion (coarse-graining / identification)
All complexity arises from repeated application of these rules.
Axiom 4 — Information & Holography
Information content in a region scales with its boundary, not its volume.
This principle constrains graph growth and suppresses unphysical clustering.
Axiom 5 — Geometricity
Stable geometry emerges only if the average coordination number satisfies:
This acts as a dimensional attractor, favoring 4D spacetime.
Axiom 6 — Persistence & Closure
Redundant causal loops and hierarchical stability are favored.
These enforce:
robustness
error correction
scale invariance (RG stability)
Key Emergent Results (So Far)
Simulations demonstrate:
Emergent time from causal chain growth
Dimensional stability when ⟨k⟩ ≈ 8
Suppression of metric collapse using geometricity constraints
Hierarchical closure under coarse-graining
Non-trivial interaction graphs resembling worldlines
These results suggest spacetime-like behavior is not imposed, but dynamically selected.
Repository Structure
Copy code
Text
HCSN-Theory/
├── engine/                # Core simulation engine
│   ├── hypergraph.py      # Vertices, hyperedges, causality
│   ├── rules.py           # Rewrite rules
│   ├── rewrite_engine.py  # Acceptance dynamics
│   └── observables.py     # Physical diagnostics
│
├── experiments/           # Reproducible experiments
│   ├── exp_phase_diagram.py
│   ├── exp_critical_scan.py
│   └── exp_worldline_interactions.py
│
├── notebooks/             # Visualization & exploration
│
├── figures/               # Generated plots
│
├── theory/                # Conceptual documentation
│   └── hcsn_summary.md
│
└── README.md
How to Run a Toy Universe
Requirements
Python ≥ 3.10
No external dependencies required (pure Python)
Basic Run
Copy code
Bash
python3 run_diagnostics.py
This evolves a toy universe and prints diagnostics every N steps:
average coordination ⟨k⟩
causal depth (time)
interaction concentration
closure density
hierarchical stability
Diagnostics Explained
Quantity
Meaning
⟨k⟩
Average coordination (dimension control)
L
Max causal chain length (emergent time)
Φ
Interaction concentration (hub suppression)
Ψ
Closure density (redundancy)
Ω
Hierarchical closure (RG stability)
Stable spacetime-like behavior is associated with:
⟨k⟩ ≈ 7.5–8.5
Φ small
Ω non-zero across scales
Current Research Focus
Preventing metric collapse under coarse-graining
Implementing logarithmic information metrics
Enforcing holographic bounds dynamically
Identifying Lorentz-invariant fixed points
Exploring quantum probability emergence
Negative results are considered valuable — they identify missing axioms.
Who Can Contribute?
You don’t need to be an expert in quantum gravity.
We welcome:
physicists (theory, GR, QFT, QG)
mathematicians (graph theory, category theory)
programmers (simulation, optimization, visualization)
curious thinkers
If you can:
question assumptions
test ideas
improve code clarity
You can contribute meaningfully.
Status
🚧 Active Research
This is not a finished theory.
It is a controlled exploration of what minimal rules can generate a universe.
Philosophy
“The universe may not be described by computation — it may be computation.”
HCSN treats this not as a metaphor, but as a testable hypothesis.