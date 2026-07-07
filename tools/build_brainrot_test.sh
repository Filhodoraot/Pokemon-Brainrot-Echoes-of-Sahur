#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 tools/apply_brainrot_test_build.py
python3 tools/patch_brainrot_trainers.py
make

echo ""
echo "Done. Open pokefirered.gba in mGBA."
