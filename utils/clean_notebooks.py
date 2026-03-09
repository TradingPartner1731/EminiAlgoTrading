import os
import subprocess
import sys

def clean_notebooks():
    # Define directories to exclude (using relative paths from project root)
    excluded_dirs = ['research', '.ipynb_checkpoints', 'venv', '.venv']
    
    print("🚀 Starting Jupyter Notebook cleanup...")
    
    cleaned_count = 0
    skipped_count = 0

    for root, dirs, files in os.walk('.'):
        # Skip excluded directories and their subfolders
        if any(excl in root for excl in excluded_dirs):
            skipped_count += len([f for f in files if f.endswith('.ipynb')])
            continue

        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                print(f"🧹 Cleaning: {file_path}")
                try:
                    # Executes nbstripout to remove output and metadata
                    subprocess.run(["nbstripout", file_path], check=True)
                    cleaned_count += 1
                except FileNotFoundError:
                    print("❌ Error: 'nbstripout' not found. Install with: pip install nbstripout")
                    sys.exit(1)
                except subprocess.CalledProcessError as e:
                    print(f"⚠️ Failed to clean {file_path}: {e}")

    print(f"\n✅ Done! Cleaned: {cleaned_count} | Preserved (Skipped): {skipped_count}")

if __name__ == "__main__":
    clean_notebooks()
