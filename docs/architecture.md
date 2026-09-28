# Architecture

Bounded children + multi-probe (2–3 centroids) can keep candidate count flat as a project grows from 200 to 2000 in this generator. Recall held at 4/5; one gold stays outside the probed set. Parent-wide fallback is not required for the flat-size part.
