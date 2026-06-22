---
name: facebook-headed-screenshot
description: Launches a headed Chrome browser inside Codespaces, navigates to Facebook, takes a root-level screenshot, and closes cleanly.
platform: linux
tools:
  - playwright-mcp
---

# Skill: Headed Facebook Explorer & Screenshot

## 1. Context & Prerequisites
GitHub Codespaces runs on headless Linux containers. Attempting to open a browser in headed mode directly will result in a `Missing X server or $DISPLAY` crash. To bypass this, all browser-automation tools inside this workspace must be wrapped inside a virtual framebuffer using `xvfb-run`.

## 2. AI Execution Workflow

Follow these sequence steps exactly to execute this skill successfully:

### Step 1: Initialize the Headed Browser via Virtual Display
Instead of a raw launch, execute your Playwright browser context initialization wrapped with `xvfb-run`. 
* **Action**: Invoke the Playwright MCP `browser_navigate` or launch sequence.
* **Headless Configuration**: Ensure `headless: false` (Headed Mode) is active.
* **Display Command Injection**: Wrap the background runner context using:
  ```bash
  xvfb-run -s "-screen 0 1280x1024x24"
  ```

### Step 2: Navigate to Facebook
Direct the active browser tab to the targeted social authentication landing page.
* **Target URL**: `https://facebook.com`
* **Tool**: Call `browser_navigate(url="https://facebook.com")`.
* **Wait Condition**: Wait until the network status reaches `networkidle` or `load` to allow the login forms, logos, and language selectors to fully render.

### Step 3: Capture Root Screenshot
Store a visual state of the rendered page safely inside the project workspace root directory.
* **Output Path**: `./facebook_snapshot.png` (or any descriptive name at the absolute root `/workspaces/<repo-name>/`).
* **Tool**: Call `browser_screenshot(path="./facebook_snapshot.png", fullPage=true)`. 

### Step 4: Clean Session Termination
Do not leak resources or keep hanging browser processes open inside the Codespace memory profile.
* **Action**: Explicitly invoke the tool to destroy the context.
* **Tool**: Call `browser_close` (or `playwright-cli close`).

## 3. Error Handling Guardrails

* **If $DISPLAY errors occur**: Re-verify that `xvfb-run` is active and that the `xvfb` apt package is installed in the baseline Codespace configuration.
* **If Facebook blocks the request (Captchas/Bot Detection)**: Proceed with taking the screenshot of whatever is currently on-screen (e.g., the security check page), save it to the root folder, and log a diagnostic note for the user before terminating the session.
