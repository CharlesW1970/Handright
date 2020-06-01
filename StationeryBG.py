﻿# coding: utf-8
from PIL import Image, ImageFont

from handright import Template, handwrite

text = """
    这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。
    这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。
    这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。
    这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。
    这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。这是一段自动生成的笔迹，这是一段自动生成的笔迹。

"""

imagex = Image.open("./pic/stationeryBackground.jpg")
width, height = imagex.size
imagex = imagex.resize((width * 2, height * 2), resample=Image.LANCZOS)


template = Template(background=imagex,
    font_size=140,
    font=ImageFont.truetype("./fonts/whx_2nd.ttf"),
    line_spacing=220,
    fill=0,  # 字体“颜色”
    left_margin=380,
    top_margin=370,
    right_margin=340,
    bottom_margin=340,
    word_spacing=12,
    line_spacing_sigma=7,  # 行间距随机扰动
    font_size_sigma=3,  # 字体大小随机扰动
    word_spacing_sigma=6,  # 字间距随机扰动
    end_chars=", 。",  # 防止特定字符因排版算法的自动换行而出现在行首
    perturb_x_sigma=2,  # 笔画横向偏移随机扰动
    perturb_y_sigma=2,  # 笔画纵向偏移随机扰动
    perturb_theta_sigma=0.05,  # 笔画旋转偏移随机扰动
)
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.show()
    im.save("./output/{}.png".format(i))