#!/usr/bin/env python
"""Met à jour .env avec FLOWISE_* et N8N_BASIC_AUTH_*. Variables : FLOWISE_USERNAME, FLOWISE_PASSWORD, N8N_BASIC_AUTH_USER, N8N_BASIC_AUTH_PASSWORD."""
import os
import re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(root, ".env")
env_example = os.path.join(root, ".env.example")
keys = {
    "FLOWISE_USERNAME": os.environ.get("FLOWISE_USERNAME", ""),
    "FLOWISE_PASSWORD": os.environ.get("FLOWISE_PASSWORD", ""),
    "N8N_BASIC_AUTH_ACTIVE": "true" if os.environ.get("N8N_BASIC_AUTH_USER") else "false",
    "N8N_BASIC_AUTH_USER": os.environ.get("N8N_BASIC_AUTH_USER", ""),
    "N8N_BASIC_AUTH_PASSWORD": os.environ.get("N8N_BASIC_AUTH_PASSWORD", ""),
}
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
else:
    with open(env_example, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not os.path.exists(env_path):
        with open(env_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        lines = lines[:]
seen = {k: False for k in keys}
out = []
for line in lines:
    for k in keys:
        if re.match(rf"^{re.escape(k)}\s*=", line):
            out.append(f"{k}={keys[k]}\n")
            seen[k] = True
            break
    else:
        out.append(line)
for k in keys:
    if not seen[k]:
        out.append(f"{k}={keys[k]}\n")
with open(env_path, "w", encoding="utf-8") as f:
    f.writelines(out)
print(" .env mis à jour : FLOWISE_USERNAME, FLOWISE_PASSWORD, N8N_BASIC_AUTH_*")
