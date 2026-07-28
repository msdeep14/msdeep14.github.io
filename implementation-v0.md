# Implementation Plan: System Design Page Modernization

**Phase/Feature:** Modernization of the System Design Resources Page (`_includes/system_design.html`).

## Analysis & Rationale
The current `system_design.html` include relies on inline styling, basic flexbox layouts, and flat design principles that look somewhat dated and lack visual engagement. To make it more premium, user-interactive, and maintainable, the styles need to be moved to SCSS and enhanced with modern CSS capabilities. 

Key technical decisions:
- **Separation of Concerns:** Extract all inline `<style>` tags from the HTML into a new `_sass/_system-design.scss` file.
- **Design System Integration:** Reuse existing SCSS variables (`$helveticaNeue`, `$blue`, `$lightGray`) to ensure the page feels cohesive with the rest of the Jekyll Now theme.
- **Modern UI Patterns:** Utilize CSS Grid for better responsiveness, implement subtle drop shadows for depth, and add micro-animations on hover (`transform: translateY(-5px)`) to make elements feel "alive" and encourage exploration.

## Actions Planned
- [ ] Create `_sass/_system-design.scss` with modernized styles.
- [ ] Update `style.scss` to import the new `_system-design.scss` partial.
- [ ] Refactor `_includes/system_design.html` to remove inline styles, apply semantic HTML (`<section>`), and update class names for the new Grid layout.

## Edge Cases / Potential Issues
- **Responsiveness of YouTube Iframes:** Ensure that the embedded YouTube videos maintain their aspect ratios (`aspect-ratio: 16/9`) on smaller viewports.
- **Inherited Styles:** Ensure that the generic Jekyll Now theme styles do not override the specific card styles we implement.
