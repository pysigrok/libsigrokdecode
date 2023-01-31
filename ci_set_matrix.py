import json
import os
import pathlib

def set_output(name: str, value):
    print(f"Setting GitHub actions output {name} to '{value}'")
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "at") as f:
            print(f"{name}={value}", file=f)
    else:
        print("No output file")

decoders = []
for p in pathlib.Path("decoders").iterdir():
    if p.is_dir() and not p.name.startswith("__"):
        decoders.append(p.name)

print(decoders)
set_output("decoders", json.dumps(sorted(decoders)))
