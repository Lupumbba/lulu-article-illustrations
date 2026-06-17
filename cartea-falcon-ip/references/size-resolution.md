# Size And Resolution

## Parse User Requests

Support these forms:

- Exact pixel size: `1600x900`, `1080x1350`, `3840x2160`.
- Aspect ratio: `16:9`, `4:5`, `1:1`, `9:16`.
- Resolution level: `draft`, `standard`, `2K`, `4K`.
- Platform use: article body, article hero, website banner, Xiaohongshu cover, LinkedIn post, Instagram story.

## Sensible Sizes

Use these only when the user does not give exact pixels:

- Article body: `1600x900`.
- Article hero: `1920x1080`.
- Website banner: `2400x1000`.
- Xiaohongshu cover: `1080x1440`.
- LinkedIn post: `1200x627`.
- Square social post: `1080x1080`.
- Vertical story: `1080x1920`.
- 2K landscape: `2048x1152`.
- 4K landscape: `3840x2160`.

## Generation Size Versus Final Size

Image generators may return a nearby size. Treat the requested size as the final file requirement.

After generation:

1. Inspect width and height.
2. If they do not match the requested size, run `scripts/normalize_image_size.py`.
3. Prefer `cover` for image-like scenes.
4. Prefer `contain` for dense labels, UI-like cards, or diagrams where cropping would remove text.
5. Re-check final dimensions.

## Resolution Labels

- `draft`: generate quickly, final max edge around 1024 px.
- `standard`: final max edge around 1600-1920 px.
- `2K`: final landscape size around `2048x1152`.
- `4K`: final landscape size around `3840x2160`.

If the user gives both a label and exact pixels, exact pixels win.
