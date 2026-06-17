from __future__ import annotations

import math
import random
from pathlib import Path
from typing import Callable, Sequence, TypeAlias

from PIL import Image, ImageDraw, ImageFont


Point: TypeAlias = tuple[int, int]
Box: TypeAlias = tuple[int, int, int, int]
Color: TypeAlias = tuple[int, int, int]


WIDTH: int = 1600
HEIGHT: int = 900
INK: Color = (20, 20, 18)
ORANGE: Color = (235, 116, 28)
RED: Color = (203, 39, 32)
BLUE: Color = (43, 106, 190)
LULU: Color = (245, 190, 72)
LULU_LIGHT: Color = (252, 216, 127)
WHITE: Color = (255, 255, 255)
PALE_BLUE: Color = (232, 241, 255)
PALE_ORANGE: Color = (255, 239, 207)
PALE_RED: Color = (255, 229, 225)
FONT_PATH: Path = Path("/System/Library/Fonts/STHeiti Light.ttc")


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size)


def create_canvas() -> Image.Image:
    return Image.new("RGB", (WIDTH, HEIGHT), WHITE)


def jitter_point(point: Point, rng: random.Random, amount: int) -> Point:
    x, y = point
    return (x + rng.randint(-amount, amount), y + rng.randint(-amount, amount))


def hand_line(draw: ImageDraw.ImageDraw, points: Sequence[Point], color: Color, width: int, rng: random.Random) -> None:
    for start, end in zip(points, points[1:]):
        draw.line((jitter_point(start, rng, 2), jitter_point(end, rng, 2)), fill=color, width=width)


def hand_arrow(draw: ImageDraw.ImageDraw, start: Point, end: Point, color: Color, width: int, rng: random.Random) -> None:
    hand_line(draw, (start, end), color, width, rng)
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    angle = math.atan2(dy, dx)
    length = 22
    left = (
        int(end[0] - length * math.cos(angle - math.pi / 6)),
        int(end[1] - length * math.sin(angle - math.pi / 6)),
    )
    right = (
        int(end[0] - length * math.cos(angle + math.pi / 6)),
        int(end[1] - length * math.sin(angle + math.pi / 6)),
    )
    hand_line(draw, (left, end, right), color, width, rng)


def label(draw: ImageDraw.ImageDraw, text: str, point: Point, color: Color, size: int) -> None:
    draw.text(point, text, fill=color, font=font(size))


def note_box(draw: ImageDraw.ImageDraw, text: str, box: Box, fill: Color, outline: Color, size: int) -> None:
    draw.rounded_rectangle(box, radius=14, fill=fill, outline=outline, width=3)
    text_box = draw.textbbox((0, 0), text, font=font(size))
    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]
    x1, y1, x2, y2 = box
    draw.text((x1 + (x2 - x1 - text_width) // 2, y1 + (y2 - y1 - text_height) // 2 - 2), text, fill=INK, font=font(size))


def draw_lulu(draw: ImageDraw.ImageDraw, center: Point, scale: float, pose: str) -> None:
    cx, cy = center
    body_w = int(150 * scale)
    body_h = int(115 * scale)
    box = (cx - body_w // 2, cy - body_h // 2, cx + body_w // 2, cy + body_h // 2)
    draw.ellipse(box, fill=LULU_LIGHT, outline=INK, width=max(2, int(3 * scale)))
    face = (cx + int(15 * scale), cy - int(22 * scale), cx + int(68 * scale), cy + int(28 * scale))
    draw.ellipse(face, fill=ORANGE, outline=INK, width=max(1, int(2 * scale)))
    draw.ellipse((cx - int(28 * scale), cy - int(20 * scale), cx - int(17 * scale), cy - int(9 * scale)), fill=INK)
    draw.ellipse((cx + int(8 * scale), cy - int(20 * scale), cx + int(19 * scale), cy - int(9 * scale)), fill=INK)
    fruit = (cx - int(22 * scale), cy - body_h // 2 - int(34 * scale), cx + int(18 * scale), cy - body_h // 2 + int(4 * scale))
    draw.ellipse(fruit, fill=ORANGE, outline=INK, width=max(1, int(2 * scale)))
    draw.line((cx - int(2 * scale), cy - body_h // 2 - int(32 * scale), cx + int(12 * scale), cy - body_h // 2 - int(42 * scale)), fill=INK, width=max(1, int(2 * scale)))
    draw.arc((cx + int(25 * scale), cy - int(4 * scale), cx + int(50 * scale), cy + int(22 * scale)), 200, 320, fill=INK, width=max(1, int(2 * scale)))
    leg_y = cy + body_h // 2 - int(4 * scale)
    draw.line((cx - int(35 * scale), leg_y, cx - int(48 * scale), leg_y + int(36 * scale)), fill=INK, width=max(2, int(3 * scale)))
    draw.line((cx + int(22 * scale), leg_y, cx + int(34 * scale), leg_y + int(36 * scale)), fill=INK, width=max(2, int(3 * scale)))
    if pose == "push":
        draw.line((cx - int(70 * scale), cy, cx - int(115 * scale), cy - int(25 * scale)), fill=INK, width=max(2, int(3 * scale)))
        draw.line((cx - int(70 * scale), cy + int(18 * scale), cx - int(115 * scale), cy + int(8 * scale)), fill=INK, width=max(2, int(3 * scale)))
    elif pose == "hold":
        draw.line((cx - int(70 * scale), cy - int(5 * scale), cx - int(115 * scale), cy - int(45 * scale)), fill=INK, width=max(2, int(3 * scale)))
        draw.line((cx + int(70 * scale), cy - int(5 * scale), cx + int(116 * scale), cy - int(45 * scale)), fill=INK, width=max(2, int(3 * scale)))
    elif pose == "crank":
        draw.line((cx + int(70 * scale), cy, cx + int(120 * scale), cy - int(15 * scale)), fill=INK, width=max(2, int(3 * scale)))
        draw.ellipse((cx + int(118 * scale), cy - int(28 * scale), cx + int(138 * scale), cy - int(8 * scale)), outline=INK, width=max(2, int(3 * scale)))
    else:
        draw.line((cx - int(65 * scale), cy, cx - int(110 * scale), cy), fill=INK, width=max(2, int(3 * scale)))
        draw.line((cx + int(65 * scale), cy, cx + int(110 * scale), cy), fill=INK, width=max(2, int(3 * scale)))


def save_image(image: Image.Image, output_path: Path) -> None:
    image.save(output_path, format="PNG", optimize=True)


def draw_entry_shift(output_path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    rng = random.Random(11)
    old_boxes = [("搜索", 140, 370), ("筛选", 300, 430), ("浏览", 460, 375), ("留资", 610, 455)]
    for text, x, y in old_boxes:
        note_box(draw, text, (x, y, x + 105, y + 55), WHITE, INK, 28)
    hand_line(draw, ((105, 520), (250, 520), (380, 535), (520, 510), (680, 532)), INK, 3, rng)
    label(draw, "旧路径", (210, 300), BLUE, 36)
    label(draw, "太绕", (548, 330), RED, 32)
    draw_lulu(draw, (800, 500), 1.08, "hold")
    draw.rounded_rectangle((690, 430, 910, 500), radius=26, fill=PALE_ORANGE, outline=ORANGE, width=4)
    label(draw, "对话入口", (722, 447), ORANGE, 35)
    hand_arrow(draw, (905, 485), (1060, 485), ORANGE, 5, rng)
    new_boxes = [("理解需求", 1080, 345), ("推荐车", 1235, 430), ("直接留资", 1375, 345)]
    for text, x, y in new_boxes:
        note_box(draw, text, (x, y, x + 130, y + 60), WHITE, INK, 26)
    label(draw, "新入口", (1180, 285), BLUE, 36)
    save_image(image, output_path)


def draw_need_clarification(output_path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    rng = random.Random(22)
    draw.rounded_rectangle((95, 260, 405, 395), radius=34, fill=WHITE, outline=INK, width=3)
    label(draw, "family car?", (135, 300), INK, 38)
    label(draw, "模糊需求", (145, 205), BLUE, 36)
    for point in ((450, 320), (485, 260), (505, 385)):
        label(draw, "?", point, RED, 42)
    draw.ellipse((560, 360, 1030, 665), fill=(245, 251, 255), outline=BLUE, width=3)
    label(draw, "追问", (735, 330), BLUE, 34)
    draw_lulu(draw, (785, 515), 1.0, "hold")
    cards = [("预算", 640, 430), ("座位", 805, 405), ("新旧", 660, 565), ("能源", 840, 560)]
    for text, x, y in cards:
        note_box(draw, text, (x, y, x + 92, y + 46), WHITE, INK, 25)
    hand_arrow(draw, (420, 505), (555, 505), ORANGE, 5, rng)
    hand_arrow(draw, (1030, 505), (1165, 505), ORANGE, 5, rng)
    for idx, x in enumerate((1190, 1335, 1480)):
        draw.rounded_rectangle((x, 430, x + 86, 74 + 430), radius=12, fill=WHITE, outline=INK, width=3)
        draw.arc((x + 15, 455, x + 72, 505), 180, 360, fill=INK, width=3)
        label(draw, f"车{idx + 1}", (x + 22, 510), INK, 23)
    label(draw, "推荐车", (1280, 365), ORANGE, 34)
    save_image(image, output_path)


def draw_price_intelligence(output_path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    rng = random.Random(33)
    label(draw, "市场区间", (430, 185), BLUE, 36)
    hand_line(draw, ((470, 545), (780, 545), (1120, 545)), INK, 5, rng)
    hand_line(draw, ((800, 275), (800, 650)), INK, 5, rng)
    draw.ellipse((700, 632, 900, 690), outline=INK, width=4)
    draw.line((600, 285, 1000, 285), fill=INK, width=4)
    draw.line((625, 285, 520, 430), fill=INK, width=3)
    draw.line((975, 285, 1080, 430), fill=INK, width=3)
    draw.ellipse((430, 420, 610, 475), outline=INK, width=3)
    draw.ellipse((990, 420, 1170, 475), outline=INK, width=3)
    price_tags = [("过高", 210, 335, RED), ("过低", 300, 455, RED), ("可疑", 175, 520, RED)]
    for text, x, y, color in price_tags:
        note_box(draw, text, (x, y, x + 86, y + 50), PALE_RED, color, 24)
    label(draw, "车商报价", (230, 275), INK, 32)
    draw_lulu(draw, (790, 430), 0.92, "hold")
    draw.rounded_rectangle((980, 345, 1320, 470), radius=18, fill=WHITE, outline=INK, width=3)
    label(draw, "Cartea建议价", (1010, 382), INK, 31)
    label(draw, "信任感", (1135, 500), BLUE, 33)
    hand_arrow(draw, (1250, 505), (1340, 505), ORANGE, 5, rng)
    draw.ellipse((1350, 450, 1460, 560), outline=ORANGE, width=4)
    label(draw, "OK", (1385, 485), ORANGE, 33)
    label(draw, "异常价格", (280, 600), RED, 32)
    save_image(image, output_path)


def draw_lead_scoring(output_path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    rng = random.Random(44)
    label(draw, "行为信号", (170, 210), BLUE, 36)
    tokens = [("浏览", 115, 320), ("停留", 220, 420), ("聊天", 120, 525), ("搜索", 300, 545), ("预算", 340, 335)]
    for text, x, y in tokens:
        draw.ellipse((x, y, x + 82, y + 58), fill=WHITE, outline=INK, width=3)
        label(draw, text, (x + 13, y + 12), INK, 24)
    hand_arrow(draw, (435, 450), (585, 450), ORANGE, 5, rng)
    draw.rounded_rectangle((585, 320, 920, 585), radius=32, fill=PALE_ORANGE, outline=INK, width=4)
    label(draw, "评分机", (705, 355), INK, 34)
    draw_lulu(draw, (725, 520), 0.86, "crank")
    draw.ellipse((820, 405, 885, 470), outline=INK, width=4)
    hand_arrow(draw, (925, 450), (1055, 450), ORANGE, 5, rng)
    baskets = [("Hot", 1080, 320, PALE_RED, RED), ("Warm", 1240, 420, PALE_ORANGE, ORANGE), ("Cold", 1400, 520, PALE_BLUE, BLUE)]
    for text, x, y, fill, color in baskets:
        draw.rounded_rectangle((x, y, x + 125, y + 78), radius=14, fill=fill, outline=color, width=4)
        label(draw, text, (x + 28, y + 20), color, 30)
    label(draw, "优先跟进", (1110, 250), RED, 34)
    draw.line((1135, 625, 1185, 590), fill=INK, width=3)
    draw.ellipse((1120, 615, 1170, 665), outline=INK, width=3)
    draw.arc((1162, 585, 1215, 642), 280, 80, fill=INK, width=3)
    save_image(image, output_path)


def draw_operations_engine(output_path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    rng = random.Random(55)
    draw_lulu(draw, (315, 570), 0.95, "push")
    draw.rounded_rectangle((95, 545, 300, 665), radius=18, fill=WHITE, outline=INK, width=3)
    draw.ellipse((130, 650, 165, 685), outline=INK, width=4)
    draw.ellipse((235, 650, 270, 685), outline=INK, width=4)
    for text, y in (("车型参数", 430), ("图片", 470), ("库存", 510), ("数据", 550), ("语言", 590)):
        note_box(draw, text, (120, y, 250, y + 38), WHITE, INK, 21)
    label(draw, "输入素材", (130, 360), BLUE, 36)
    hand_arrow(draw, (455, 545), (585, 545), ORANGE, 5, rng)
    draw.rounded_rectangle((585, 330, 960, 650), radius=38, fill=PALE_ORANGE, outline=INK, width=4)
    label(draw, "自动生成", (700, 380), ORANGE, 36)
    draw.rounded_rectangle((665, 450, 880, 545), radius=14, fill=WHITE, outline=INK, width=3)
    draw.line((690, 480, 855, 480), fill=INK, width=3)
    draw.line((690, 515, 810, 515), fill=INK, width=3)
    hand_arrow(draw, (965, 520), (1095, 520), ORANGE, 5, rng)
    outputs = [("车型卡片", 1110, 310), ("SEO页", 1285, 390), ("车商描述", 1115, 520), ("本地化", 1295, 610)]
    for text, x, y in outputs:
        note_box(draw, text, (x, y, x + 145, y + 58), WHITE, INK, 25)
    draw.rounded_rectangle((1035, 665, 1195, 735), radius=14, fill=PALE_BLUE, outline=BLUE, width=3)
    label(draw, "数据分析", (1058, 684), BLUE, 25)
    label(draw, "降低成本", (1260, 735), RED, 34)
    save_image(image, output_path)


def main() -> None:
    output_dir = Path("/Users/archerabbit/Desktop/噜噜skill/assets/ai-cartea-ai-illustrations")
    output_dir.mkdir(parents=True, exist_ok=True)
    renderers: Sequence[tuple[str, Callable[[Path], None]]] = (
        ("01-ai-agent-entry-shift.png", draw_entry_shift),
        ("02-ai-need-clarification.png", draw_need_clarification),
        ("03-ai-price-intelligence.png", draw_price_intelligence),
        ("04-ai-lead-scoring.png", draw_lead_scoring),
        ("05-ai-operations-engine.png", draw_operations_engine),
    )
    for filename, renderer in renderers:
        renderer(output_dir / filename)


if __name__ == "__main__":
    main()
