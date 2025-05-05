# Auto Negative Prompt
An extension for Stable Diffusion Web UI to automatically insert a user-defined keyword(s) into **negative prompts**, with customizable positioning.

Author: Albert Griscti-Soler

Date: 2025-05-05

## Features

- Automatically adds a keyword to negative prompts.
- Optionally insert the keyword at the **beginning** OR **end** of the prompt.
- Fully configurable via the Web UI Settings.

## Installation

1. Clone this folder into your `stable-diffusion-webui/extensions` directory.
2. Restart the Web UI.
3. Go to `Settings` → **Negative Prompt Insert** section.
4. Enter your desired keyword(s) and choose whether to prepend *OR* append it.

## Settings

- **Enable extension** — toggle extension
- **Insert keyword(s) at beginning (instead of end)** — toggle position of keyword in the prompt
- **Keyword(s) to insert into negative prompts** — the keyword(s) (e.g., `blurry`, `low quality`, etc.)

## Example

**Before:**  

negative_prompt: "lowres, bad anatomy"

**After (with keyword = "blurry"):**  

- Appended: `lowres, bad anatomy, blurry`  
- Prepended: `blurry, lowres, bad anatomy`

---

Enjoy faster and more consistent prompt tuning!
