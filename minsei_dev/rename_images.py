# -*- coding: utf-8 -*-
import os

folder = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(folder, "image")

# リネームする画像
renames = {
    "Gemini_Generated_Image_4222dq4222dq4222.jpg": "entaku.jpg",
    "Gemini_Generated_Image_j589i8j589i8j589.jpg": "gaikan.jpg",
}

for old_name, new_name in renames.items():
    old_path = os.path.join(image_folder, old_name)
    new_path = os.path.join(image_folder, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"✅ {old_name} → {new_name}")
    else:
        print(f"❌ {old_name} が見つかりません")

print("完了！")
input("Enterキーを押して閉じる...")
