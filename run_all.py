import os

input_root = "test_data/workshop_test_data"
output_root = "output"

os.makedirs(output_root, exist_ok=True)

for folder in os.listdir(input_root):

    folder_path = os.path.join(input_root, folder)

    if not os.path.isdir(folder_path):
        continue

    json_file = os.path.join(folder_path, f"{folder}.json")

    if not os.path.exists(json_file):
        continue

    output_file = os.path.join(output_root, f"{folder}.json")

    cmd = f"python3 test.py {json_file} {output_file}"

    print("Running:", cmd)

    os.system(cmd)

print("\n✅ All charts processed successfully!")