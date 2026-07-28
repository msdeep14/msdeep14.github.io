# Implementation Plan: Programmer-Aligned "Wow" Aesthetic

**Phase/Feature:** Global UI/UX overhaul for all tabs (About, Projects, Books, Speaking) to introduce a modern, tech-focused design system.

## Analysis & Rationale
The current website lacks a unified design system. Each tab uses its own inline CSS with varying layouts, fonts (mostly basic Arial), and design paradigms. To make the site "programmer aligned" and create a "wow" factor:
- **Design System Extraction:** All inline styles across `_includes/*.html` will be removed and centralized into SCSS partials (e.g., `_sass/_projects.scss`, `_sass/_about.scss`).
- **Typography:** Introduction of modern web fonts (`Inter` for body, a monospace font like `Fira Code` for tech accents) to immediately signal a developer-centric blog.
- **Layout Modernization:** 
  - The `projects.html` tab currently uses image-hover texts which feel dated. It will be replaced with a CSS Grid of "GitHub-style" project cards featuring tech stack tags.
  - The `about.html` tab will receive a terminal/code-inspired intro block.
  - `books.html` and `speaking.html` will be updated to use sleek glassmorphic or high-contrast modern card styles.

## Actions Planned
- [ ] Create `_sass/_theme.scss` to define global variables and tech fonts.
- [ ] Refactor `_includes/about.html` and extract CSS to `_sass/_about.scss`.
- [ ] Refactor `_includes/projects.html` to a Grid layout and extract CSS to `_sass/_projects.scss`.
- [ ] Refactor `_includes/books.html` and extract CSS to `_sass/_books.scss`.
- [ ] Refactor `_includes/speaking.html` and extract CSS to `_sass/_speaking.scss`.
- [ ] Update `style.scss` to import the new partials.

## Edge Cases / Potential Issues
- **Responsive Layouts:** Ensuring that the newly created Grid layouts for projects and videos collapse correctly on mobile devices without horizontal overflow.
- **Font Loading:** Ensuring that adding web fonts (e.g., Google Fonts) does not significantly impact page load performance.
