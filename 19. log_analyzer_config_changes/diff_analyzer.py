"""
Log Analyzer for Config Changes
"""

import difflib

old_config = "19. log_analyzer_config_changes/config_old.txt"
new_config = "19. log_analyzer_config_changes/config_new.txt"
diff_output_file = "diff_output.txt"

def load_file(filename):
    with open(filename, "r") as f:
        return f.readlines()

def generate_diff(old_lines, new_lines):
    diff = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=old_config,
        tofile=new_config,
        lineterm=''
    )
    return list(diff)

def main():
    old_lines = load_file(old_config)
    new_lines = load_file(new_config)
    diff = generate_diff(old_lines, new_lines)

    print("\n".join(diff))

    with open(diff_output_file, "w") as f:
        f.write("\n".join(diff))

    print(f"\n✅ Diff saved to {diff_output_file}")

if __name__ == "__main__":
    main()
