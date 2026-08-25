# Visual Media Library 视觉素材库

> 团队共享视觉素材库——vibe coding 建站 + AI 视频剪辑时随时调取。
> 本仓库是 **AI 友好的素材索引系统**：AI agent 读 manifest.json 即可知道有什么、怎么用。

## 快速使用（AI Agent 指引）

1. **先读 `manifest.json`** —— 机器可读索引，包含全部素材的分类/标签/许可/用途
2. **按需取用**：
   - 建站：`images/`（产品图、背景、AI 生成视觉）
   - 视频剪辑：`videos/`（B-roll、产品演示）+ `audio/`（BGM、音效）
   - UI 设计：`ui-assets/`（图标、logo、字体）
3. **素材命名规则**：`分类-产品-场景-序号.扩展名`（如 `factory-line-uvcoating-01.mp4`）

## 目录结构

```
media-library/
├── README.md            # 本文件（人类/AI 入口）
├── manifest.json        # 机器可读索引（AI 主入口）
├── images/
│   ├── products/        # 产品图（按产品线分子目录）
│   │   ├── leadchem/    #   LeadChem UV/水性材料
│   │   └── lisheng/     #   力圣木工胶
│   ├── factory/         # 工厂/车间实拍
│   ├── backgrounds/     # 背景/纹理/渐变
│   └── ai-generated/    # AI 生成素材（产品渲染/概念图）
├── videos/
│   ├── broll/           # B-roll 素材（机器运转/生产/测试/发货）
│   └── product-demos/   # 产品演示片段
├── audio/
│   ├── bgm/             # 免版权背景音乐（标注许可）
│   └── sfx/             # 音效（转场/提示音）
└── ui-assets/
    ├── icons/           # 图标（SVG/PNG）
    ├── logos/           # 品牌 logo
    └── fonts/           # 字体（标注许可）
```

## 素材许可规范（重要）

| 类型 | 来源 | 许可要求 |
|---|---|---|
| 自有实拍 | 团队拍摄 | ✅ 自由使用 |
| 免费素材库 | Pexels/Pixabay | 免费商业使用，标注来源 |
| AI 生成 | DALL-E/即梦/Midjourney | 标注生成工具 |
| BGM/音效 | 免版权库 | 标注许可（CC0/CC BY） |
| 字体 | Google Fonts 等 | 标注许可（OFL 等） |

**每个素材文件旁可放 `来源.txt` 或文件名加 `-src` 后缀标注来源。**

## 调取场景对照

| 你要做什么 | 去这里找 |
|---|---|
| 产品落地页 hero 图 | images/products/ + images/ai-generated/ |
| 工厂信任感视频 | videos/broll/factory* |
| TikTok 视频 B-roll | videos/broll/（机器/测试/发货） |
| TikTok 背景音乐 | audio/bgm/ |
| 网站 UI 图标 | ui-assets/icons/ |
| 品牌 logo | ui-assets/logos/ |

## 维护规则

- 新增素材：放入对应目录 + **更新 manifest.json**（AI 才能发现）
- 命名要语义化：`产品-场景-序号`，不用 `IMG_2026.jpg`
- 删素材：同步从 manifest.json 移除
- manifest 结构见下方示例

## manifest.json 格式示例

```json
{
  "version": "1.0",
  "updated": "2026-08-18",
  "assets": [
    {
      "id": "img-leadchem-uvcoating-01",
      "path": "images/products/leadchem/uvcoating-demo-01.jpg",
      "type": "image",
      "category": "product",
      "tags": ["uv-varnish", "leadchem", "coating", "demo"],
      "description": "UV 光油涂抹演示，高光泽效果",
      "license": "own",
      "usage": "product-page, video-broll"
    }
  ]
}
```

---

*由 AI 团队维护 · 用途：建站 + 视频剪辑视觉素材中枢*
