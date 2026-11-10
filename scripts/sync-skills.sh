#!/usr/bin/env bash
set -euo pipefail

# Pin repository URLs and skill subdirectories. This script copies upstream source
# files without executing any untrusted code from those repositories.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/.agents/skills"
mkdir -p "$OUT"
TEMP="$(mktemp -d)"
trap 'rm -rf "$TEMP"' EXIT

sync_skill() {
  local repo="$1" subdir="$2" name="$3" lic="$4"
  local work="$TEMP/$name"
  echo "::group::Sync $name from $repo"
  git clone -q --depth 1 --filter=blob:none --sparse "https://github.com/$repo.git" "$work"
  if [[ "$subdir" == "." ]]; then
    git -C "$work" sparse-checkout disable
  else
    git -C "$work" sparse-checkout set "$subdir"
  fi
  local source="$work"
  [[ "$subdir" != "." ]] && source="$work/$subdir"
  test -f "$source/SKILL.md" || { echo "::error::Missing SKILL.md for $name"; exit 1; }
  local dest="$OUT/$name"
  mkdir -p "$dest"
  rsync -a --delete --exclude '.git' "$source/" "$dest/"
  if [[ -n "$lic" && ! -e "$dest/LICENSE" && ! -e "$dest/LICENSE.md" && ! -e "$dest/LICENSE.txt" ]]; then
    # Retrieve upstream license only. It is never executed.
    curl -fsSL --retry 3 "https://raw.githubusercontent.com/$repo/main/$lic" -o "$dest/LICENSE.UPSTREAM.txt"
  fi
  echo "$repo @ $(git -C "$work" rev-parse HEAD)" >> "$TEMP/upstream-versions.txt"
  echo "::endgroup::"
}

sync_skill "jiji262/humanizer-chinese" "." "humanizer-chinese" ""
sync_skill "nothing0here/humanizer-zh" "." "humanizer-zh" ""
sync_skill "msimchowitz/writing-skills" "for-agents/general-writing" "general-writing" ""
sync_skill "msimchowitz/writing-skills" "for-agents/academic-voice" "academic-voice" "LICENSE"
sync_skill "sickn33/agentic-awesome-skills" "skills/professional-proofreader" "professional-proofreader" "LICENSE"
sync_skill "K-Dense-AI/scientific-agent-skills" "skills/scientific-writing" "scientific-writing" "LICENSE.md"
sync_skill "docwriter-org/plain-writing-skill" "skills/plain-writing" "plain-writing" "LICENSE"
sync_skill "anthropics/skills" "skills/docx" "docx" ""

cp "$TEMP/upstream-versions.txt" "$ROOT/UPSTREAM_VERSIONS.txt"
for name in humanizer-chinese humanizer-zh general-writing academic-voice professional-proofreader scientific-writing plain-writing docx; do
  test -s "$OUT/$name/SKILL.md" || exit 1
done

echo "Synced all 8 skills successfully."
