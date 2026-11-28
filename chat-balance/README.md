# Chat · visual balance (stress test)

Live: https://matty-morgs.github.io/octo-space/chat-balance/

This page is the standing stress test for the chat. It shows a busy, real room on desktop and mobile. Update it whenever chat or app changes land.

## Source of truth

Everything is built in Figma from the s.space library:

- File: [AG2] Product (`4xXN58n1Ny9zfdxPBBctIk`)
- Page: "↳ Chat / Visual balance · stress test (UI bugs)" (`2367:9656`)

| Frame | Node | Used for |
|---|---|---|
| Desktop · UI bugs (stress test) | `2367:9657` | `desk_base.png`, `desk_header.png`, `desk_timeline.png` (from Messages `2367:9818`) |
| Mobile · chat list | `2371:294` | `list.png` |
| Mobile · UI bugs room (stress test) | `2372:527` | `mob_base.png`, `mob_header.png`, `mob_timeline.png` (from Timeline `2372:530`) |
| Mobile · UI bugs room · liquid glass | `2381:861` | `mob_base_liquid.png`, `mob_overlay_liquid.png` |
| Desktop · UI bugs · liquid glass | `2381:1276` | `desk_base_liquid.png`, `desk_composer_liquid.png` |

The two liquid frames keep their own copies of the timeline. When you change messages, change all four frames, keeping the same message order.

## Re-exporting

All images are 2× renders.

- **Timelines:** clone the Messages or Timeline frame. Set the top padding to 0, hug the height, give it a white fill, turn clipping off and `rescale(2)`. Screenshot it with `maxDimension` at least as large as its longest edge.
- **Overlays** (header, composer, liquid capsules) must be transparent:
  1. Render the copy twice, once on a white fill and once on black. Use the glass capsule frames with their fills, strokes and effects cleared, because the page draws the glass in CSS.
  2. Run `python3 tools/matte.py white.png black.png out.png`.
- **Positions:** if a capsule or the header changes size, update its position and size in `index.html`.
- **Who reacted:** each reaction chip in Figma is named `Reaction · <emoji> · <name>|<name>`. After exporting a timeline, read each chip's position (at 1×, relative to the export copy) and its name. Write them into `reactions.json` and into the inline data at the bottom of `index.html`. The page lays invisible hover/tap targets over the chips and shows the library Tooltip.
- **Cleanup:** delete the scratch copies from the Figma page afterwards.
