# Clinical AI Evaluation Framework

This repository implements an evaluation framework for assessing the reliability of a clinical NLP pipeline.

## Metrics

- Entity type error rate
- Assertion error rate
- Temporality error rate
- Subject attribution error
- Event date accuracy
- Attribute completeness

## Run

Single file:

python3 test.py input.json output.json

Full dataset:

python3 run_all.py