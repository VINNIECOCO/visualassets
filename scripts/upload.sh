#!/usr/bin/env bash
# 上传素材到 vibe-assets 仓库并自动更新 index.json
# 用法: ./upload.sh <素材文件> [标签,逗号分隔] [描述]
set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

FILE="$1"
TAGS="${2:-}"
DESC="${3:-}"

if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  echo "用法: ./upload.sh <素材文件> [标签] [描述]"
  exit 1
fi

# 判断素材类型 → 目标目录
EXT="${FILE##*.}"
TYPE="image"
DEST_DIR="b-roll"
case "$EXT" in
  mp4|mov|webm|avi) TYPE="video"; DEST_DIR="b-roll" ;;
  jpg|jpeg|png|webp|gif|svg) TYPE="image"; DEST_DIR="textures" ;;
esac

# 询问/默认目录（简单规则：按文件名前缀）
case "$(basename "$FILE")" in
  *uv*|*varnish*|*ink*) DEST_DIR="products/uv-varnish" ;;
  *glue*|*wood*|*adhesive*) DEST_DIR="products/wood-glue" ;;
  *factory*|*line*|*workshop*|*plant*) DEST_DIR="factory" ;;
  *test*|*drop*|*quality*) DEST_DIR="factory" ;;
esac

mkdir -p "assets/$DEST_DIR"
cp "$FILE" "assets/$DEST_DIR/"
FILENAME="$(basename "$FILE")"
FULL_PATH="assets/$DEST_DIR/$FILENAME"

echo "📦 $TYPE → $FULL_PATH"

# 更新 index.json（用 python 保证 JSON 正确）
python3 - "$FULL_PATH" "$TYPE" "$TAGS" "$DESC" <<'EOF'
import json, sys, os
path, typ, tags, desc = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
idx = json.load(open('index.json'))
aid = os.path.splitext(os.path.basename(path))[0].replace('/', '-')
entry = {
    "id": aid,
    "path": path,
    "type": typ,
    "tags": [t.strip() for t in tags.split(',') if t.strip()],
    "description": desc,
}
# 去重（同 id 覆盖）
idx['assets'] = [a for a in idx['assets'] if a['id'] != aid]
idx['assets'].append(entry)
json.dump(idx, open('index.json', 'w'), ensure_ascii=False, indent=2)
print(f"✅ index.json 已更新: {aid}")
EOF

echo "下一步: git add + commit + push"
