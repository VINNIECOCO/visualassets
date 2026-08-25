#!/usr/bin/env python3
"""vibe-assets 素材生成器 — 程序化生成基础视觉素材（无需外部 API）。
用法: python gen_assets.py [输出目录]
"""
import os, sys, math, random
from PIL import Image, ImageDraw, ImageFilter

OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"
W, H = 1080, 1920  # 竖屏为主（TikTok/移动端），部分横屏

def ensure(d):
    os.makedirs(d, exist_ok=True)

def neon_grid():
    img = Image.new("RGB", (W, H), (5, 8, 20))
    d = ImageDraw.Draw(img)
    for x in range(0, W, 60):
        d.line([(x, 0), (x, H)], fill=(15, 30, 70), width=1)
    for y in range(0, H, 60):
        d.line([(0, y), (W, y)], fill=(15, 30, 70), width=1)
    # 发光节点
    for _ in range(30):
        x, y = random.randint(0, W), random.randint(0, H)
        d.ellipse([x-3, y-3, x+3, y+3], fill=(34, 211, 238))
    return img.filter(ImageFilter.GaussianBlur(0.5))

def gradient(c1, c2, diagonal=True):
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    steps = 200
    for i in range(steps):
        t = i / steps
        r = int(c1[0] + (c2[0]-c1[0])*t)
        g = int(c1[1] + (c2[1]-c1[1])*t)
        b = int(c1[2] + (c2[2]-c1[2])*t)
        if diagonal:
            d.line([(0, int(i*H/steps)), (W, int(i*H/steps))], fill=(r, g, b))
        else:
            d.line([(int(i*W/steps), 0), (int(i*W/steps), H)], fill=(r, g, b))
    return img

def glow_orb(color=(34, 211, 238), center=None):
    img = Image.new("RGB", (W, H), (8, 10, 24))
    d = ImageDraw.Draw(img)
    cx, cy = center or (W//2, H//3)
    layers = 12
    for i in range(layers, 0, -1):
        r = i * 90
        alpha_r = int(255 - i * 18)
        c = tuple(max(0, int(x*alpha_r/255)) for x in color)
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=c)
    img = img.filter(ImageFilter.GaussianBlur(25))
    # 叠加亮心
    d2 = ImageDraw.Draw(img)
    d2.ellipse([cx-60, cy-60, cx+60, cy+60], fill=color)
    return img.filter(ImageFilter.GaussianBlur(8))

def noise_texture():
    img = Image.new("RGB", (W, H), (10, 12, 28))
    d = ImageDraw.Draw(img)
    for _ in range(8000):
        x, y = random.randint(0, W-1), random.randint(0, H-1)
        v = random.randint(0, 60)
        d.point((x, y), fill=(v, v, v+10))
    return img

def particles(color=(168, 85, 247)):
    img = Image.new("RGB", (W, H), (8, 8, 16))
    d = ImageDraw.Draw(img)
    for _ in range(200):
        x, y = random.randint(0, W), random.randint(0, H)
        r = random.randint(2, 10)
        c = tuple(max(0, min(255, int(v*random.uniform(0.4, 1)))) for v in color)
        d.ellipse([x-r, y-r, x+r, y+r], fill=c)
    img = img.filter(ImageFilter.GaussianBlur(2))
    d2 = ImageDraw.Draw(img)
    for _ in range(80):
        x, y = random.randint(0, W), random.randint(0, H)
        d2.ellipse([x-2, y-2, x+2, y+2], fill=(255, 255, 255))
    return img

def product_bottle(label="VIBE"):
    img = Image.new("RGB", (W, H), (16, 18, 40))
    d = ImageDraw.Draw(img)
    # 背景光
    orb = glow_orb((34, 211, 238), (W//2, H//2))
    img = Image.blend(img, orb, 0.35)
    d = ImageDraw.Draw(img)
    # 瓶身（矩形+圆角）
    bw, bh = 320, 720
    bx, by = (W-bw)//2, (H-bh)//2
    d.rounded_rectangle([bx, by, bx+bw, by+bh], radius=40, fill=(30, 60, 90), outline=(80, 200, 230), width=4)
    # 高光
    d.rounded_rectangle([bx+30, by+40, bx+60, by+bh-40], radius=20, fill=(140, 220, 250))
    # 瓶盖
    d.rounded_rectangle([bx+60, by-60, bx+bw-60, by], radius=12, fill=(90, 100, 130))
    # 标签
    d.rounded_rectangle([bx+50, by+220, bx+bw-50, by+420], radius=10, fill=(20, 30, 50))
    d.rectangle([bx+60, by+240, bx+bw-60, by+252], fill=(34, 211, 238))
    return img

def product_box():
    img = Image.new("RGB", (W, H), (14, 16, 36))
    orb = glow_orb((250, 204, 21), (W//2, H//3))
    img = Image.blend(img, orb, 0.3)
    d = ImageDraw.Draw(img)
    bw, bh = 560, 560
    bx, by = (W-bw)//2, (H-bh)//2 - 60
    d.rectangle([bx, by, bx+bw, by+bh], fill=(28, 32, 60), outline=(80, 160, 230), width=3)
    # 盒盖
    d.rectangle([bx-20, by-20, bx+bw+20, by+10], fill=(22, 26, 50), outline=(80, 160, 230), width=3)
    # 标签
    d.rectangle([bx+80, by+150, bx+bw-80, by+420], fill=(10, 12, 28))
    d.rectangle([bx+90, by+170, bx+bw-90, by+182], fill=(250, 204, 21))
    # 波纹装饰
    for i in range(5):
        y = by + 260 + i*30
        d.line([(bx+80, y), (bx+bw-80, y)], fill=(34, 211, 238), width=2)
    return img

def product_drum():
    img = Image.new("RGB", (W, H), (12, 14, 30))
    orb = glow_orb((74, 222, 128), (W//2, H//2))
    img = Image.blend(img, orb, 0.3)
    d = ImageDraw.Draw(img)
    dw, dh = 620, 520
    dx, dy = (W-dw)//2, (H-dh)//2
    d.rounded_rectangle([dx, dy, dx+dw, dy+dh], radius=60, fill=(26, 34, 44), outline=(74, 222, 128), width=4)
    d.rounded_rectangle([dx+40, dy+80, dx+dw-40, dy+dh-80], radius=40, fill=(34, 42, 54), outline=(60, 140, 110), width=2)
    d.ellipse([dx-20, dy+dh-60, dx+dw+20, dy+dh+60], fill=(18, 24, 34), outline=(74, 222, 128), width=3)
    return img

def icon(name, color=(34, 211, 238)):
    img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = cy = 256
    if name == "gear":
        for i in range(8):
            a = i * 45
            d.polygon([
                (cx + 150*math.cos(math.radians(a-10)), cy + 150*math.sin(math.radians(a-10))),
                (cx + 220*math.cos(math.radians(a)), cy + 220*math.sin(math.radians(a))),
                (cx + 150*math.cos(math.radians(a+10)), cy + 150*math.sin(math.radians(a+10))),
            ], fill=color)
        d.ellipse([cx-90, cy-90, cx+90, cy+90], fill=color)
        d.ellipse([cx-40, cy-40, cx+40, cy+40], fill=(20, 20, 40))
    elif name == "factory":
        d.rectangle([60, 190, 452, 430], fill=color)
        d.rectangle([100, 100, 200, 190], fill=color)
        d.rectangle([310, 60, 410, 190], fill=color)
        for x in range(150, 420, 80):
            d.rectangle([x, 260, x+30, 430], fill=(20, 20, 40))
    elif name == "bottle":
        d.rounded_rectangle([156, 100, 356, 440], radius=30, fill=color)
        d.rounded_rectangle([186, 40, 326, 110], radius=10, fill=color)
    elif name == "shield":
        d.polygon([(256, 60), (420, 140), (420, 300), (256, 440), (92, 300), (92, 140)], fill=color)
        d.polygon([(256, 120), (370, 180), (370, 290), (256, 400), (142, 290), (142, 180)], fill=(20, 20, 40))
    elif name == "bolt":
        d.polygon([(300, 60), (150, 300), (230, 300), (180, 452), (370, 220), (280, 220)], fill=color)
    return img

def save(img, path):
    img.save(path, quality=92)
    print(f"  ✅ {path}")

def main():
    ensure(f"{OUT}/textures")
    ensure(f"{OUT}/products/placeholder")
    ensure(f"{OUT}/icons")

    print("生成纹理/背景...")
    save(neon_grid(), f"{OUT}/textures/neon-grid-dark.png")
    save(gradient((10, 15, 40), (34, 211, 238)), f"{OUT}/textures/gradient-cyan.png")
    save(gradient((20, 8, 40), (168, 85, 247)), f"{OUT}/textures/gradient-purple.png")
    save(gradient((8, 24, 16), (74, 222, 128)), f"{OUT}/textures/gradient-green.png")
    save(gradient((40, 8, 8), (250, 204, 21)), f"{OUT}/textures/gradient-amber.png")
    save(noise_texture(), f"{OUT}/textures/noise-dark.png")
    save(glow_orb(), f"{OUT}/textures/glow-cyan.png")
    save(glow_orb((168, 85, 247)), f"{OUT}/textures/glow-purple.png")
    save(particles(), f"{OUT}/textures/particles-purple.png")

    print("生成产品概念图...")
    save(product_bottle("VIBE"), f"{OUT}/products/placeholder/product-bottle.png")
    save(product_box(), f"{OUT}/products/placeholder/product-box.png")
    save(product_drum(), f"{OUT}/products/placeholder/product-drum.png")

    print("生成图标...")
    for name, c in [("gear", (34, 211, 238)), ("factory", (74, 222, 128)), ("bottle", (250, 204, 21)), ("shield", (168, 85, 247)), ("bolt", (255, 90, 90))]:
        img = icon(name, c)
        img.convert("RGB").save(f"{OUT}/icons/icon-{name}.png")
        print(f"  ✅ {OUT}/icons/icon-{name}.png")

    print("\n完成！素材已生成。")

if __name__ == "__main__":
    main()
