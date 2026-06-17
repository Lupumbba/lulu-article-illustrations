# Prompt Template

## Single Image Generation

```text
Generate one standalone automotive article illustration.

Final output target: [WIDTH]x[HEIGHT] px, [ASPECT], [RESOLUTION].
Reference images: use `assets/reference/front.png`, `assets/reference/back.png`, `assets/reference/side.png`, and `assets/reference/side-alt.png` as strict identity references.
Style: premium white-background editorial illustration with light hand-drawn environment elements, clean black ink lines, large whitespace, white mechanical character rendering, Cartea green #00a600 highlights and annotations.
IP character: Cartea falcon robot. Preserve the exact reference design: white glossy armor, black glass visor, green glowing visor rings, angular white beak, black textured neck, wing-like mechanical arms with mint-green panels, black articulated hands, wheel-based legs, large-head compact-body proportions. Do not redesign or deform the character.
Article context: [ARTICLE CONTEXT].
Scene: [SCENE].
Falcon action: [ACTION].
Key objects: [OBJECTS].
Short labels only: [LABELS].
Composition: [COMPOSITION].
Brand color: use Cartea green #00a600 for routes, highlights, labels, buttons, interface glow, and brand emphasis.
Avoid: orange as Cartea brand color, natural bird feathers, generic bird mascot, altered robot silhouette, changed head/visor/beak/wings/wheel-feet, photorealistic dealership ad, official logo imitation, crowded PPT charts, complex UI, watermark, long paragraphs of text.
```

## Edit Or Regenerate

Use this when an image is close but not good enough:

```text
Keep the same core concept and Cartea falcon robot IP. Improve only [ISSUE].
Preserve: [GOOD PARTS].
Fix: [BAD PARTS].
Final output target: [WIDTH]x[HEIGHT] px.
Avoid: changing the article meaning, changing the robot's reference-locked appearance, removing the falcon robot's main action, adding long text, cropping key labels.
```
