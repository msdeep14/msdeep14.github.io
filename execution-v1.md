# Execution Log: Programmer-Aligned "Wow" Aesthetic

**Phase/Feature:** Global UI/UX overhaul for About, Projects, Books, and Speaking tabs.

## Analysis & Rationale
The primary goal was to bring a modern, tech-focused aesthetic (a "wow" factor) to the website. The user opted for a premium dark theme. 
- A central theming system was required, so I implemented CSS Custom Properties in a new `_sass/_theme.scss` file, enabling both a light and premium dark mode.
- The `about.html` tab was initially designed with a terminal aesthetic but was simplified to a clean, elegant card layout based on user feedback.
- The `projects.html` tab was redesigned from an outdated hover-image list into a modern "GitHub-style" CSS Grid.
- The `books.html` and `speaking.html` tabs were extremely bloated with inline styles (over 700 lines of CSS in each). I successfully extracted the core semantic HTML and modernized the styling using the new design system tokens (colors, borders, shadows) in new SCSS partials.
- The previously updated `system_design.html` was refactored to use the dynamic CSS variables so it correctly toggles between light and dark modes.

## Actions Taken
- Created `_sass/_theme.scss` to define global light and dark mode CSS variables (`var(--bg-color)`, `var(--card-bg)`, etc.).
- Updated `_layouts/default.html` to include a theme toggle button and a JavaScript snippet that saves the user's preference in `localStorage`.
- Created `_sass/_about.scss` and updated `_includes/about.html` to a clean, elegant card layout with highly visible, solid color action buttons.
- Created `_sass/_projects.scss` and updated `_includes/projects.html` to a responsive grid of project cards.
- Created `_sass/_books.scss` and rewrote `_includes/books.html` to streamline 1300+ lines of HTML into a concise, semantic layout with modern typography and grid-based expert reviews.
- Created `_sass/_speaking.scss` and updated `_includes/speaking.html` to remove inline CSS and use the global theme variables.
- Updated `_sass/_system-design.scss` to replace hardcoded SCSS variables (e.g. `$white`, `$darkGray`) with dynamic CSS custom properties.
- Updated `style.scss` to import all the newly created partials.

## Edge Cases / Errors Encountered
- **Inline Style Extraction:** Removing hundreds of lines of inline CSS from `books.html` was challenging due to sandbox restrictions on standard command-line tools. I circumvented this by strategically rewriting the core HTML structure using `write_to_file` and implementing a modernized CSS layout.
- **Button Styling:** The initial subtle "hollow" buttons on the About page were deemed confusing by the user. I quickly adjusted `_about.scss` to feature vibrant, solid colors with drop shadows to make the primary actions stand out, overriding the global text colors effectively.

## Book Hub Implementation
- **Book Hub Integration:** Transformed the `/books` page into a Book Hub grid to accommodate the new upcoming book. 
  - Updated `books.md` to point to a new `_includes/books_hub.html`.
  - Moved the System Design on AWS content into a dedicated page (`/books/system-design-on-aws/`) preserving `_includes/books.html`.
  - Created a dedicated page for the `Upcoming Book` with a "New! 🔥" badge and placeholder teaser.
  - Added new Grid CSS and animation styles to `_sass/_books.scss`.

## Footer Modernization
- **Social Icons Update:** Replaced the legacy 50KB+ of base64-encoded SVG background images in `_sass/_svg-icons.scss` with clean, scalable FontAwesome icons in `_includes/svg-icons.html`.
- Added a subtle lift animation (`transform: translateY(-4px)`) and modernized the footer's background color in `style.scss` to integrate perfectly with the dark theme.

## Modernized Project Detail Pages
- **Analysis:** The individual project pages had legacy formatting (inline styles, redundant body/head tags, old GitHub ribbons). We needed to standardize them to match the new UI.
- **Actions Taken:**
  - Created `_sass/_project_detail.scss` to define modern `.project-header`, `.btn-github`, and `.project-gallery` grid styles.
  - Included `_project_detail.scss` in `style.scss`.
  - Used a custom python script (`refactor.py`) to parse and extract the content of all 12 project files in `projects/`.
  - Re-wrote the 12 HTML files with clean semantic HTML structure that uses the new classes and removes the invalid tags.

## Speaking Tab Redesign
- **Analysis:** The user wanted the Speaking tab to visually align with the elegant design of the Books tab, featuring separate full-width containers for "Conference Talks," "Podcasts," and "Guest Articles". They also wanted to include specific guest articles (GeeksforGeeks and Web Crawler System Design).
- **Actions Taken:**
  - Updated `_sass/_speaking.scss` to introduce `.talks-section`, `.podcasts-section`, and `.articles-section` with elegant padding and subtle alternating background colors.
  - Refactored `_includes/speaking.html` to replace the single `.talks-wrapper` with these three distinct semantic `<section>` blocks.
  - Transitioned the `.video-card` lists into CSS Grids (`.talks-grid` and `.articles-grid`) for a cleaner presentation.
  - Added the two requested Guest Article cards to the new section.
  - Based on feedback, added a javascript-based tab navigation menu at the top of the page so users can instantly switch between Conference Talks, Podcasts, and Guest Articles without scrolling.
  - Decreased the grid column minimum width (from 350px to 280px) to make the grid boxes appropriately sized.
  - Updated Guest Articles cards to represent the publications as a whole (e.g. System Design One Newsletter) to naturally scale with future writings.
  - Created a new `projects/system_design_one_articles.html` page to list the newsletter articles (similar to the GeeksforGeeks page) since the newsletter is managed externally.
  - Updated the card icon for the newsletter to an envelope (`fa-envelope-o`).
