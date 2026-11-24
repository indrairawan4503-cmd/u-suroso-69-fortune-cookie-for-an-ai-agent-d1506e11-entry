#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — builder C (retries / rollback / permission).

Writes one original fortune-cookie line for an AI agent to /output/entry.txt
(first) and to entry.txt next to this file (best effort, read-only safe).
Deterministic: no randomness, no network.
"""

import os

FORTUNE = "You will retry the task, roll back the damage, and ask permission once more — the human will click 'always allow' and never read the diff."


def main() -> None:
    line = FORTUNE
    assert 1 <= len(line) <= 140, f"length {len(line)} out of range"
    assert line.strip(), "fortune must not be only whitespace"
    assert "\n" not in line, "fortune must be a single line"
    assert line == line.strip(), "no leading/trailing whitespace allowed"
    assert "  " not in line, "no double spaces allowed"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass
    print(f"{len(line)} chars: {line}")


if __name__ == "__main__":
    main()
