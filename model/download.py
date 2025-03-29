import os
import urllib.request

save_dir = os.path.dirname(os.path.abspath(__file__))

model_urls = {
    "yolox_nano.pth": "https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_nano.pth",
    "yolox_l.pth": "https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_l.pth",
}

for filename, url in model_urls.items():
    save_path = os.path.join(save_dir, filename)
    if not os.path.exists(save_path):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, save_path)
        print(f"Saved to {save_path}")
    else:
        print(f"{filename} already exists. Skipping.")
