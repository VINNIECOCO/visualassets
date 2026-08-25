# 🎨 AI 素材生成提示词库（Prompt Library）

> 用途：在 Midjourney / Flux / ChatGPT-Image / Ideogram / 即梦 / 可灵 中生成高质量素材，生成后上传到 vibe-assets。
> 用法：复制英文提示词 → AI 图像工具生成 → 保存 → `./scripts/upload.sh <文件> <标签> <描述>`
> 技巧：加 `--ar 9:16`（Midjourney）或指定 1080x1920（竖屏）。

---

## 一、产品图（工业品/包装材料）

### 1.1 瓶装产品主图
```
Premium product photography of a glossy liquid coating bottle, deep navy blue glass, cyan neon rim light, dark studio background with subtle teal gradient, reflective surface, professional commercial lighting, ultra realistic, 8k, centered composition --ar 9:16
```
中文场景：UV 光油/水性涂料瓶装产品主图

### 1.2 桶装产品
```
Industrial 20L drum container product shot, metallic silver with blue label, warehouse setting bokeh background, dramatic studio lighting, clean commercial photography, high detail --ar 9:16
```
中文场景：工业桶装化学品（油墨/胶水）

### 1.3 包装盒特写
```
Luxury packaging box mockup, embossed logo, soft golden light, dark premium background, macro photography, shallow depth of field, commercial product shot --ar 9:16
```
中文场景：彩盒包装特写

### 1.4 液体质地（流动感）
```
Macro shot of glossy varnish liquid flowing in slow motion, vibrant cyan and deep blue tones, dark background, dramatic backlighting, ultra detailed texture, premium feel --ar 9:16
```
中文场景：光油/涂料流动质感（适合产品卖点背景）

### 1.5 抽象产品概念
```
Futuristic abstract industrial product render, glossy dark material with glowing cyan edges, floating on dark gradient background, 3D octane render style, minimal, premium tech aesthetic --ar 9:16
```
中文场景：科技感产品概念图（建站 Hero 背景）

---

## 二、工厂/生产场景

### 2.1 现代化车间
```
Modern industrial factory interior, automated production line running, clean bright workshop, workers in uniform, cinematic lighting, photorealistic, wide angle --ar 16:9
```
中文场景：现代化车间全景（横屏，可用于视频 B-roll）

### 2.2 机器特写
```
Close-up of precision machinery operating, metal gears and robotic arms, sparks of light, dark industrial atmosphere, cinematic depth of field, photorealistic --ar 16:9
```
中文场景：机器运行特写

### 2.3 质检实验室
```
Clean quality control laboratory, scientist in white coat testing materials with precision instruments, bright sterile environment, blue accents, professional photography --ar 16:9
```
中文场景：质检/实验室场景

### 2.4 发货场景
```
Shipping containers being loaded at factory dock, forklift moving pallets, golden hour lighting, logistics atmosphere, photorealistic commercial photography --ar 16:9
```
中文场景：发货/物流场景

---

## 三、B-roll 背景（视频空镜）

### 3.1 科技流体
```
Abstract flowing liquid metal waves, dark background with cyan and purple neon reflections, smooth motion, cinematic 4k loop, ultra smooth --ar 9:16
```
中文场景：科技流体空镜（视频背景）

### 3.2 粒子光效
```
Floating glowing particles in dark space, cyan and purple light trails, bokeh depth, premium tech background loop, smooth animation --ar 9:16
```
中文场景：粒子光效背景

### 3.3 城市夜景霓虹
```
Futuristic city skyline at night, neon cyan and purple lights, rain reflections, cyberpunk atmosphere, cinematic b-roll --ar 9:16
```
中文场景：科技感城市夜景

### 3.4 动态渐变
```
Smooth flowing gradient waves, deep blue to cyan to purple, silky motion, elegant premium background loop, minimal --ar 9:16
```
中文场景：动态渐变背景

---

## 四、图标 / Logo / 品牌元素

### 4.1 现代 Logo 概念
```
Minimal modern logo concept for industrial company, geometric hexagon with letter V, cyan on dark background, vector style, flat design, premium --ar 1:1
```
中文场景：工业品牌 Logo 概念（V 开头）

### 4.2 品质认证图标
```
Minimal shield icon with checkmark, cyan gradient on dark, flat vector style, premium tech feel, centered --ar 1:1
```
中文场景：品质/认证图标

### 4.3 品牌字母组合
```
Elegant letter V monogram logo, thin line style, glowing cyan accent, dark background, luxury minimal branding --ar 1:1
```
中文场景：品牌字母组合

---

## 五、纹理 / 背景

### 5.1 深色科技纹理
```
Dark tech texture, subtle circuit board patterns, faint cyan glow lines, matte black background, seamless tile, minimal --ar 9:16
```
中文场景：深色科技纹理（网页背景）

### 5.2 渐变霓虹
```
Smooth neon gradient background, deep navy to vibrant cyan to magenta, soft glow, premium modern web background, no text --ar 9:16
```
中文场景：霓虹渐变背景（Hero 区）

### 5.3 磨砂玻璃
```
Frosted glass texture with subtle gradient, soft light refraction, dark mode UI background, premium minimal --ar 9:16
```
中文场景：磨砂玻璃质感背景

---

## 六、完整提示词模板（品牌视觉系统）

```
[A 产品主图类]
    [B 场景类] + [C 风格类] + [D 技术参数] + [E 画幅]
示例：
    "UV varnish bottle" +
    "in dark studio with cyan neon lighting" +
    "premium commercial photography, ultra realistic" +
    "8k, high detail, centered composition" +
    "--ar 9:16"
```

**可替换模块：**
- A：UV varnish bottle / ink container / adhesive drum / packaging box / coating sample
- B：dark studio / factory line / warehouse / laboratory / on white background / on gradient background
- C：premium commercial photography / cinematic / minimal tech / industrial realistic / luxury brand
- D：8k / ultra detailed / professional lighting / shallow depth of field / photorealistic
- E：--ar 9:16（竖屏）/ --ar 16:9（横屏）/ --ar 1:1（图标）

---

## 上传流程

```bash
# 生成图片后
cd ~/projects/vibe-assets
./scripts/upload.sh ~/Downloads/generated-image.png "product,uv-varnish,hero" "UV 光油产品主图（AI 生成）"
git add -A && git commit -m "添加素材: UV 光油产品主图" && git push
```

> AI 建站/剪辑时读 index.json 即可发现新素材。
