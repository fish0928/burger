import qrcode
import os

# 定义页面映射：键为文件名，值为页面 URL
pages = {
    'index': 'https://fish0928.github.io/burger/index.html',
    'fridge': 'https://fish0928.github.io/burger/fridge.html',
    'cook': 'https://fish0928.github.io/burger/cook.html',
    'sauce': 'https://fish0928.github.io/burger/sauce.html',
    'plate': 'https://fish0928.github.io/burger/plate.html',
}
os.makedirs(r'.\out', exist_ok=True)
# 生成并保存二维码图片
for name, url in pages.items():
    img = qrcode.make(url)
    img.save(rf'.\out\{name}.png')
    print(f"Saved QR code for {url} as {name}.png")