import sys
import shutil
from datetime import date, timedelta
from pathlib import Path

import frontmatter

CLEANUP_DAYS = 3
INPUT_DIR = Path("A-🔴INPUTS/(C)-🟡RSS/Input")
OUTPUT_DIR = Path("A-🔴INPUTS/(C)-🟡RSS/Output")


def main():
    cutoff = date.today() - timedelta(days=CLEANUP_DAYS)
    moved, deleted = [], []
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for md_file in sorted(INPUT_DIR.glob("*.md")):
        try:
            post = frontmatter.load(str(md_file))
        except Exception:
            continue
        if post.get("archived") is True:
            shutil.move(str(md_file), str(OUTPUT_DIR / md_file.name))
            moved.append(md_file.name)
        elif post.get("read") is True:
            try:
                if date.fromisoformat(str(post.get("fetched", ""))) <= cutoff:
                    md_file.unlink()
                    deleted.append(md_file.name)
            except ValueError:
                pass
    print(f"Moved to Output: {len(moved)}: {moved}")
    print(f"Deleted: {len(deleted)}: {deleted}")
    sys.exit(0)


if __name__ == "__main__":
    main()
