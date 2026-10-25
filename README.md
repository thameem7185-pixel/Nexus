# NEXUS

A single-file AI chat app with a liquid-glass interface, a live WebGL wave background, an in-chat HTML runner and voice input and output.

**Author:** Muhammed Thameem KT

## Features

- **Liquid-glass UI.** Every surface (header, bubbles, composer, side panel, menus, runner) uses translucent blurred glass over a fully dark theme.
- **GradientASCII background.** A WebGL2 shader that draws a glowing horizon out of ASCII characters. Characters scramble under the cursor and ripple outward on click. It falls back to a plain gradient if WebGL2 is unavailable.
- **Crystal loader.** While Nexus is thinking, six spinning crystals (a Uiverse.io loader by Z4drus) are shown.
- **LatticeLoader.** A 3x3 round-cell orbit loader shows while Nexus thinks, then leaves a "Done in 2.4s" (green) or "Failed after" (red) footer on each reply.
- **Strands voice overlay.** Turning on the mic opens a full-screen strands animation driven by your microphone level.
- **HTML runner.** A panel on the right side of the chat runs HTML in a sandboxed iframe. It can reload, open in a new tab, and close with the X button.
- **Auto-run.** When you paste HTML, Nexus prints it back exactly as sent in one code block, and the app runs it automatically. Any `html` code block in a reply also has a **Run** button.
- **Long-press message actions.** Press and hold (or right-click) a message to copy, select text, edit and resend (your messages), speak, or run its HTML (Nexus messages).
- **Prompt bar.** Ported from the React Bits PromptBar. Type `@` for sources, `/` for commands, or use the + button. Attached files show as chips. The effort slider (Low to Max) is sent to the model as a reasoning-effort hint, and Max adds drifting sparks that react to your typing. The send arrow morphs into a stop square while Nexus is thinking, and stops the request when pressed.
- **Side panel.** The hamburger button opens it. Close it with the X button or by tapping outside.
- **Modes.** General AI, Code gen and Deep think, each with its own system prompt.
- **VoicePill mic.** Tap or hold the mic: the pill expands with a timer and a live waveform, and you can slide left to cancel. The Strands overlay plays behind the chat while you speak.
- **File attachments.** Text and code files are read in the browser and sent with your message.
- **Voice.** Auto voice (Jarvis) is on by default and can be switched off in the side panel. Speech recognition for input. Output uses ElevenLabs when you add a key, and falls back to the browser voice.
- **Chat tools.** Clear chat, export as `.txt`, copy and download code blocks.

## Project structure

```
index.html   the whole app (HTML, CSS and JavaScript)
README.md    this file
```

## Setup

1. Deploy a Cloudflare Worker that accepts `POST { message, systemPrompt }` and returns JSON with a `text` (or `message`) field. Keep your model API key inside the Worker, never in the page.
2. Open `index.html` and set `WORKER_URL` to your Worker address.
3. Optional: set `ELEVENLABS_API_KEY` for a custom voice. Without it, Nexus uses the browser voice. A key placed in client-side code is visible to visitors, so route it through your Worker if you publish the page.
4. Host `index.html` anywhere static (GitHub Pages, Cloudflare Pages, Netlify), or open it locally.

## Using the HTML runner

1. Paste any HTML into the chat and send it.
2. Nexus replies with the same HTML in a single code block, and the runner opens on the right and runs it. On phones it opens full screen.
3. Use the runner header to reload, open in a new tab, or close.

The preview is sandboxed (scripts, forms, modals and popups allowed; no access to the parent page).

## Voice input

Tap the mic. The strands overlay appears while you speak, and your message is sent when you stop. Speech recognition works in Chrome, Edge and Safari. Allow microphone access when asked.

## Browser notes

- WebGL2 is needed for the animated background. Without it, a static gradient is shown.
- `backdrop-filter` (the glass effect) is supported in all current browsers.
- Motion is switched off for users who prefer reduced motion.

## Credits

Designed and built by **Muhammed Thameem KT**. Background, loader and voice visuals are re-implemented in plain JavaScript from the React Bits GradientASCII and the LatticeLoader and Strands component designs.

## Responsive layout

- **Phones:** the composer sits at the very bottom, above the keyboard while you type. On touch devices the keyboard closes when you send, so the bar settles at the bottom. The HTML runner opens full screen.
- **Tablets:** the runner slides in from the right as a panel. Landscape iPads get the runner beside the chat.
- **Laptops and monitors:** content is centered in a comfortable reading width, and text scales up on large screens.
- **Notches and landscape phones:** safe-area insets and a compact header are applied.
- **Attach menu:** + opens an "Add to chat" sheet with Camera, Photos and Files tiles. Attachments show as small cards with a thumbnail for images and an X badge to remove. Only text files are read by the AI; images and videos attach by name.
