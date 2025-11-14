
# File renamer program


from pathlib import Path

user_input = input("Enter the path: ")
folder = Path(user_input)
base_name = input("Enter the base name: ")
rename_plan = []

if folder.is_dir():

    print("\n--- PREVIEW ---")
    for i, item in enumerate(folder.iterdir(), start=1):
        if item.is_file():
            ext = item.suffix
            new_name = f"{base_name}_{i}{ext}"
            print(f"  {item.name} -> {new_name}")
            rename_plan.append((item, new_name))

    if not rename_plan:
        print("No files found to rename.")
        exit()

    print("-----------------")
    ques = input("Are you sure you want to rename these files? (y/n): ")

    if ques.strip().lower() == "y":
        for original_file, new_name_str in rename_plan:
            new_path = folder / new_name_str
            original_file.rename(new_path)

        print(f"\nSUCCESS: Renamed {len(rename_plan)} files.")

    elif ques.strip().lower() == "n":
        print("Operation cancelled.")

    else:
        print("Invalid input. Operation cancelled.")

else:
    print("Error: Folder not found or is not a directory.")
