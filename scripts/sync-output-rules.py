"""Bundle output rules into each skill for standalone installation."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    skills = Path(__file__).resolve().parents[1] / "skills"
    source = skills / "output-style" / "references"
    rules = [source / f"output-{name}.md" for name in ("common", "response", "document", "code")]
    contents = [(rule.name, rule.read_bytes()) for rule in rules]
    differences = []
    for entry in sorted(skills.glob("*/SKILL.md")):
        if entry.parent.name == "output-style":
            continue
        for name, content in contents:
            target = entry.parent / "references" / name
            if target.exists() and target.read_bytes() == content:
                continue
            differences.append(target.relative_to(skills).as_posix())
            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    if args.check and differences:
        print("Output rules differ:")
        print("\n".join(differences))
        return 1
    print(f"Output rules: {'consistent' if args.check else 'updated'} ({len(differences)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
