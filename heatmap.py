import os
import json
import matplotlib.pyplot as plt

OUTPUT_DIR = "output"

assertion = {"POSITIVE":0,"NEGATIVE":0,"UNCERTAIN":0}
temporality = {"CURRENT":0,"CLINICAL_HISTORY":0,"UPCOMING":0,"UNCERTAIN":0}
subject = {"PATIENT":0,"FAMILY_MEMBER":0}

count = 0

for file in os.listdir(OUTPUT_DIR):

    with open(os.path.join(OUTPUT_DIR,file)) as f:
        data=json.load(f)

    count += 1

    for k,v in data["assertion_error_rate"].items():
        assertion[k]+=v

    for k,v in data["temporality_error_rate"].items():
        temporality[k]+=v

    for k,v in data["subject_error_rate"].items():
        subject[k]+=v


labels = list(assertion.keys())
values = [assertion[k]/count for k in labels]

plt.figure()
plt.bar(labels, values)
plt.title("Assertion Error Distribution")
plt.ylabel("Error Rate")

plt.savefig("assertion_errors.png")
plt.close()


labels = list(temporality.keys())
values = [temporality[k]/count for k in labels]

plt.figure()
plt.bar(labels, values)
plt.title("Temporality Error Distribution")
plt.ylabel("Error Rate")

plt.savefig("temporality_errors.png")
plt.close()


labels = list(subject.keys())
values = [subject[k]/count for k in labels]

plt.figure()
plt.bar(labels, values)
plt.title("Subject Attribution Errors")
plt.ylabel("Error Rate")

plt.savefig("subject_errors.png")
plt.close()

print("✅ Heatmap charts generated")