import json
import sys
import os

ENTITY_TYPES = [
"MEDICINE","PROBLEM","PROCEDURE","TEST","VITAL_NAME",
"IMMUNIZATION","MEDICAL_DEVICE","MENTAL_STATUS","SDOH","SOCIAL_HISTORY"
]

ASSERTIONS = ["POSITIVE","NEGATIVE","UNCERTAIN"]
TEMPORALITY = ["CURRENT","CLINICAL_HISTORY","UPCOMING","UNCERTAIN"]
SUBJECT = ["PATIENT","FAMILY_MEMBER"]


def evaluate_entities(entities):

    total = len(entities)
    if total == 0:
        total = 1

    entity_errors = {k:0 for k in ENTITY_TYPES}
    assertion_errors = {k:0 for k in ASSERTIONS}
    temporality_errors = {k:0 for k in TEMPORALITY}
    subject_errors = {k:0 for k in SUBJECT}

    attribute_count = 0
    date_count = 0

    for e in entities:

        etype = e.get("entity_type","")

        if etype in ENTITY_TYPES:
            if e.get("entity","") == "":
                entity_errors[etype] += 1

        if e.get("assertion","") not in ASSERTIONS:
            assertion_errors["UNCERTAIN"] += 1

        if e.get("temporality","") not in TEMPORALITY:
            temporality_errors["UNCERTAIN"] += 1

        if e.get("subject","") not in SUBJECT:
            subject_errors["PATIENT"] += 1

        metadata = e.get("metadata_from_qa",{})

        if metadata:
            attribute_count += 1

            for r in metadata.get("relations",[]):
                if r.get("entity_type") in ["exact_date","derived_date"]:
                    date_count += 1


    result = {
        "entity_type_error_rate": {k:v/total for k,v in entity_errors.items()},
        "assertion_error_rate": {k:v/total for k,v in assertion_errors.items()},
        "temporality_error_rate": {k:v/total for k,v in temporality_errors.items()},
        "subject_error_rate": {k:v/total for k,v in subject_errors.items()},
        "event_date_accuracy": date_count/total,
        "attribute_completeness": attribute_count/total
    }

    return result


def main():

    if len(sys.argv) != 3:
        print("Usage: python test.py input.json output.json")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print("Reading:", input_file)

    with open(input_file) as f:
        data = json.load(f)

    if isinstance(data, dict) and "entities" in data:
        entities = data["entities"]
    else:
        entities = data

    result = evaluate_entities(entities)
    result["file_name"] = os.path.basename(input_file)

    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)

    print("✅ Output written to:", output_file)


if __name__ == "__main__":
    main()