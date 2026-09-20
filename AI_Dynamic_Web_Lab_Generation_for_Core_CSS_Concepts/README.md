# AI: Dynamic Web Lab Generation for Core CSS Concepts

**Course**: SE 203 / SE 300 - High Level Programming & Artificial Intelligence in Software Engineering  
**Module**: W3 | Web Static & AI Interactive Lab Generation  
**Author**: Yonas Leykun ([@yonasleykun27](https://github.com/yonasleykun27))  
**AI Tool Used**: Gemini with Canvas / Antigravity Agentic Assistant  

---

## Overview

This project demonstrates the application of sequential and contextual AI prompting to rapidly construct interactive, single-file web applications (HTML5/CSS3/JavaScript) designed to visualize core CSS principles. Specifically, it provides dedicated interactive sandboxes for exploring:
1. **The CSS Box Model & `display` property dynamics** (Initial Box Model Lab)
2. **Side-specific margin, padding, border controls, and corner radii** (Refined Box Model Lab)
3. **Modern CSS Flexbox and Grid layout systems** (Flexbox & Grid Interactive Playground)

---

## File Index

| File | Type | Description |
| :--- | :--- | :--- |
| [`box_model_initial.html`](./box_model_initial.html) | Single-File HTML/CSS/JS | Initial interactive lab visualizing margin, border, padding, and content using `background-clip: content-box` alongside `display` property toggling (`block`, `inline-block`, `inline`). |
| [`box_model_refined.html`](./box_model_refined.html) | Single-File HTML/CSS/JS | Enhanced lab featuring individual side-specific sliders (top, right, bottom, left) for margin, padding, and border-width, plus a corner radius slider and computed CSS output. |
| [`flexbox_grid_playground.html`](./flexbox_grid_playground.html) | Single-File HTML/CSS/JS | Layout sandbox with 5 items supporting container switches between `block`, `flex`, and `grid`, live alignment controls, flex-direction, and grid template columns. |
| [`screenshots/1_initial_box_model.png`](./screenshots/1_initial_box_model.png) | Image (PNG) | High-resolution capture of the Initial Box Model Lab application. |
| [`screenshots/2_refined_box_model.png`](./screenshots/2_refined_box_model.png) | Image (PNG) | High-resolution capture of the Refined Box Model Lab application. |
| [`screenshots/3_flexbox_grid_playground.png`](./screenshots/3_flexbox_grid_playground.png) | Image (PNG) | High-resolution capture of the Flexbox and Grid Playground application. |
| [`Yonas_AI: Dynamic Web Lab Generation for Core CSS Concepts.md`](./Yonas_AI:%20Dynamic%20Web%20Lab%20Generation%20for%20Core%20CSS%20Concepts.md) | Deliverable Document | Complete prose submission containing full prompt texts, embedded screenshots, and the 2–3 paragraph reflection & synthesis. |

---

## Prompts Formulated & Executed

### Prompt 1: Initial Box Model Lab
```text
Act as a frontend web developer. Using your Canvas tool, Generate an interactive website that can be used for understanding the CSS Box Model and its relationship with the display property.

The page must have:

1. Two div elements, 'Box 1' and 'Box 2', so I can see how they interact. 'Box 1' will be the one we control.
2. The CSS must use different background colors for the content area, the padding area, and the margin area of 'Box 1' (e.g., using background-clip: content-box). The border should be a solid line.
3. A control panel with:
- Sliders to control the padding, margin, border-width, and width of 'Box 1'.
- Labels next to the sliders that show the current pixel value.
- A Dropdown (select) to change the display property of 'Box 1' to: block, inline-block, and inline.
4. JavaScript that listens to all sliders and the dropdown, and updates the CSS properties of 'Box 1' in real-time.
```

### Prompt 2: Refinement Prompt (Side-Specific Controls & Radius)
```text
Implement sliders to adjust the margin, padding, and border for each side (top, right, bottom, left) individually, and add a separate slider for the corner radius.
```

### Prompt 3: Flexbox and Grid Playground
```text
Act as a frontend web developer. Using your Canvas tool, generate an interactive website that can be used as a playground for CSS Flexbox and Grid.

The page should have:

1. A `div` element acting as the container.
2. Several `div` elements inside acting as the items (e.g., 5 items).
3. Dropdown menus (selects) that allow me to change the CSS properties of the container.
4. I need to be able to change:
- display (to switch between block, flex, and grid)
- flex-direction (row, column)
- justify-content (flex-start, center, space-between, etc.)
- align-items (flex-start, center, stretch, etc.)
- grid-template-columns (e.g., 1fr 1fr, 1fr 1fr 1fr)
5. The JavaScript must update the container's CSS in real-time when I change a dropdown.
```

---

## Reflection and Synthesis

### 1. Learning Efficacy: Interactive Visual Feedback vs. Static Documentation
Traditional web development learning materials typically illustrate the CSS Box Model through isolated two-dimensional concentric diagrams or abstract specification tables. While these diagrams accurately depict the relationship between content, padding, border, and margin, they inherently conceal runtime flow dynamics and edge-case rendering behaviors. The interactive labs generated here fundamentally accelerate conceptual retention through immediate experiential feedback. 

A quintessential demonstration occurs when switching the `display` property of 'Box 1' to `inline`. In static documentation, one must read and synthesize abstract rules stating that inline non-replaced elements do not respect explicit `width` declarations and ignore vertical margins in line-height calculations. In this interactive lab, shifting to `inline` immediately forces the box width to shrink-wrap its text, renders vertical margin sliders ineffective, and causes 'Box 2' to sit directly beside 'Box 1' within the same line-flow. Witnessing this collapse visually and manipulating the sliders in real time replaces rote memorization with an instinctive mechanical understanding of the CSS layout engine.

### 2. AI Workflow: Agile Incremental Refinement vs. Monolithic Prompting
Employing a sequential refinement workflow—initiating with a functional baseline Box Model tool before issuing a follow-up prompt for side-specific controls—demonstrates substantial engineering advantages over monolithic, all-in-one prompting. In the initial prompt, the model concentrated on foundational architectural decisions: generating semantic HTML containers, structuring a clean grid-based control panel, implementing `background-clip: content-box` for visual separation, and wiring up core DOM event listeners. 

Once this functional foundation was validated, the refinement prompt introduced targeted complexity: expanding single numeric values into distinct quad-directional dimensions (`top`, `right`, `bottom`, `left`) and introducing corner radius mathematics. This iterative paradigm directly parallels the Agile software development lifecycle, where teams build a working Minimum Viable Product (MVP), verify its core mechanics, and iteratively enhance its capability. Attempting to formulate a single massive prompt encompassing every individual slider, state variable, and edge case frequently overwhelms context alignment, leading to hallucinated syntax, broken layout grids, or omitted event bindings. Incremental refinement yields higher precision, cleaner code separation, and superior software reliability.
