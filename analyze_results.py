import os
import json

OUTPUT_DIR = "output"

entity_totals = {}
assertion_totals = {}
temporality_totals = {}
subject_totals = {}

files = os.listdir(OUTPUT_DIR)

count = 0

for f in files:

    path = os.path.join(OUTPUT_DIR, f)

    with open(path) as file:
        data = json.load(file)

    count += 1

    for k,v in data["entity_type_error_rate"].items():
        entity_totals[k] = entity_totals.get(k,0) + v

    for k,v in data["assertion_error_rate"].items():
        assertion_totals[k] = assertion_totals.get(k,0) + v

    for k,v in data["temporality_error_rate"].items():
        temporality_totals[k] = temporality_totals.get(k,0) + v

    for k,v in data["subject_error_rate"].items():
        subject_totals[k] = subject_totals.get(k,0) + v


print("\n===== GLOBAL ENTITY ERROR =====")
for k,v in entity_totals.items():
    print(k, round(v/count,4))

print("\n===== GLOBAL ASSERTION ERROR =====")
for k,v in assertion_totals.items():
    print(k, round(v/count,4))

print("\n===== GLOBAL TEMPORALITY ERROR =====")
for k,v in temporality_totals.items():
    print(k, round(v/count,4))

print("\n===== GLOBAL SUBJECT ERROR =====")
for k,v in subject_totals.items():
    print(k, round(v/count,4))