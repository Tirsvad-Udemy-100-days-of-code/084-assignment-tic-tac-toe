#!/usr/bin/env bash
# Scan the tracked files with opengrep before pushing.
# Usage:  bash scripts/scan.sh
# Env:    OPENGREP        path to the binary (default ~/.opengrep/cli/latest/opengrep.exe)
#         OPENGREP_RULES  a checkout of github.com/opengrep/opengrep-rules; when set, its
#                         python and generic rules are used too (the pull request check
#                         runs these, so a finding shows before the push)
# Note:   opengrep scans files that git tracks, so `git add` new files first.
# Exit:   0 no finding; non-zero a finding or a tool error
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
opengrep="${OPENGREP:-$HOME/.opengrep/cli/latest/opengrep.exe}"
paths=()
for path in src tests scripts docs notebooks; do
  [[ -d "$path" ]] && paths+=("$path")
done
configs=(--config p/python --config p/secrets)
if [[ -n "${OPENGREP_RULES:-}" ]]; then
  configs+=(--config "$OPENGREP_RULES/python" --config "$OPENGREP_RULES/generic")
fi
exec "$opengrep" scan "${configs[@]}" --error "${paths[@]}"
