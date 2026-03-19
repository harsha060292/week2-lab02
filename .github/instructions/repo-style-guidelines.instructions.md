---
name: repo-style-guidelines
applyTo: "**/*"
description: "Use these repository conventions when making edits in week2-lab02. Apply to HTML, CSS, JS, and Python files unless the user request explicitly overrides scope."
---

# Week2 Lab02 Agent Instructions

This instruction set captures project-level conventions for contributors and the coding assistant.

1. Keep changes minimal and focused to the user request.
2. Preserve existing folder structure and naming conventions under `assets/`, `assignments/`, and `templates/`.
3. Apply whitespace style consistent with existing files (2-space indentation for CSS/JS/HTML; 4 spaces for Python unless project config says otherwise).
4. Use plain JavaScript and native browser APIs for frontend code unless an explicit dependency request is made.
5. Write concise comments and maintain README/assignment docs clarity in English.
6. For new behavior, include a short Usage/or example block in the same file or adjacent markdown.

## Clarification questions (needed to finalize)
- Should this rule apply globally (`**/*`) or only to specific subpaths (e.g., `assets/js/**`, `assignments/**`)?
- Which language/file types should have highest priority (HTML/CSS/JS vs. Python)?
- Are there any strict linting or formatting requirements already expected (Prettier, ESLint, Black, etc.)?

## Example prompt to use this instruction
- "Implement missing form validation in `assets/js/script.js` and follow repo style conventions."
- "Fix the Python starter code in `assignments/data-analysis/starter-code.py` and keep behavior minimal."
