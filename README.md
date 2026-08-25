# 🎨 Vibe Assets — 视觉素材库（vibe coding / AI 剪辑随时调取）

> 用途：建站 + AI 剪辑视频时的视觉素材源。GitHub 仓库托管，通过 URL 随时调取。
> AI 调用方式：读 `index.json` 找到素材 → 用 raw/jsDelivr URL 直接引用。

## 📁 目录结构

```
vibe-assets/
├── README.md          # 本文件
├── index.json         # AI 可读素材清单（核心！）
├── assets/
│   ├── products/      # 产品素材（按产品子目录）
│   │   ├── uv-varnish/    # 例：UV 光油
│   │   ├── wood-glue/     # 例：木工胶
│   │   └── ...
│   ├── factory/       # 工厂实拍（车间/产线/质检/发货）
│   ├── b-roll/        # 通用 B-roll（转场/背景/空镜）
│   ├── textures/      # 纹理/背景图（科技/渐变/噪点）
│   └── icons/         # 图标/Logo/图形元素
└── scripts/
    └── upload.sh      # 上传新素材脚本（自动更新 index.json）
```

## 🔗 URL 调用规范（AI 直接引用）

### 图片（直接可用）
```
Raw:    https://raw.githubusercontent.com/VINNIECOCO/vibe-assets/main/assets/products/uv-varnish/hero.jpg
CDN:    https://cdn.jsdelivr.net/gh/VINNIECOCO/vibe-assets@main/assets/products/uv-varnish/hero.jpg
```

### 视频（建站/剪辑用）
```
Raw:    https://raw.githubusercontent.com/VINNIECOCO/vibe-assets/main/assets/factory/line-01.mp4
CDN:    https://cdn.jsdelivr.net/gh/VINNIECOCO/vibe-assets@main/assets/factory/line-01.mp4
```

### 在 HTML/代码中引用
```html
<img src="https://cdn.jsdelivr.net/gh/VINNIECOCO/vibe-assets@main/assets/products/uv-varnish/hero.jpg">
<video src="https://raw.githubusercontent.com/VINNIECOCO/vibe-assets/main/assets/factory/line-01.mp4"></video>
```

## 📝 素材命名规范（AI 可读）

```
格式：<场景>-<内容>-<序号>.<ext>
例：  hero.jpg / detail-01.jpg / demo.mp4 / line-01.mp4 / test-drop-01.mp4

命名规则：
- 小写 + 连字符，无空格
- 文件名即描述（AI 读文件名即可匹配素材）
- 同场景多张用 -01, -02 递增
```

## 📊 index.json 格式（AI 素材索引）

```json
{
  "repository": "vibe-assets",
  "base_url_raw": "https://raw.githubusercontent.com/VINNIECOCO/vibe-assets/main",
  "base_url_cdn": "https://cdn.jsdelivr.net/gh/VINNIECOCO/vibe-assets@main",
  "assets": [
    {
      "id": "uv-varnish-hero",
      "path": "assets/products/uv-varnish/hero.jpg",
      "type": "image",
      "tags": ["uv-varnish", "product", "hero"],
      "description": "UV 光油产品主图"
    },
    {
      "id": "factory-line-01",
      "path": "assets/factory/line-01.mp4",
      "type": "video",
      "tags": ["factory", "production-line"],
      "description": "产线运行实拍"
    }
  ]
}
```

AI 建站/剪辑时的调用流程：
1. 读取 index.json → 了解有哪些素材
2. 按需拼 URL（base_url + path）
3. 图片直接用，视频用 raw URL 或转码后使用

## ⚠️ 限制

- 单文件 ≤100MB（GitHub 限制），视频先压缩再传（建议 <50MB，1080p 30s）
- 仓库建议总大小 <1GB
- 私有仓库时 URL 需要认证；建议用**公开仓库**（素材非机密时）
- 版权：只放自己有权限的素材（自拍/自产/授权）
