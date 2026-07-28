# AI Agent Instructions

This document contains guidelines on AI agent response generation, coding standards, and execution mandates for all the work done in this repository. **All AI coding agents MUST read and adhere to these guidelines when responding to queries or making changes or additions in the codebase.**

## 1. Project Architecture
This repository hosts a personal portfolio and blog built using **Jekyll**, a static site generator. It is hosted on **GitHub Pages**.
- **Theme**: Based on the Jekyll Now theme (fork-first workflow).
- **Configuration**: `_config.yml` at the root directory contains site-wide settings (name, description, social links, analytics, etc.).
- **Content**: 
  - Blog posts are written in Markdown and stored in the `_posts/` directory. Files must follow the `YYYY-MM-DD-title.md` naming convention.
  - Pages (e.g., `about.md`, `projects.md`, `system_design.md`) are stored at the root directory and rendered based on their front-matter.
- **Layouts & Includes**: HTML templates are located in `_layouts/` (e.g., `default.html`, `page.html`, `post.html`), and reusable HTML snippets are in `_includes/`.
- **Styling**: SCSS is used for styling. The main entry point is `style.scss` at the root, which imports partials from the `_sass/` directory.
- **Assets**: Static assets such as images and media are stored in `images/`, `media/`, and `assets/`.

## 2. Building the Project Locally with Jekyll
To preview changes locally before pushing to GitHub:

1. **Install Dependencies**: 
   Ensure Ruby is installed. Then install the `github-pages` gem which mirrors the GitHub Pages environment:
   ```bash
   gem install github-pages
   ```
2. **Serve the Site**:
   Run the Jekyll development server from the root of the repository:
   ```bash
   jekyll build
   jekyll serve --incremental
   ```
   *Note: If you have a Gemfile configured with bundler later, you may need to run `bundle exec jekyll serve` instead.*
3. **View**: 
   Open `http://127.0.0.1:4000/` in your browser.
4. **Deploy**:
   Commit and push changes to the `master` or `main` branch. GitHub Pages will automatically rebuild and serve the website.

## 3. General Guidelines & Coding Standards
- **Markdown & Front-Matter**: All posts and pages must include valid YAML front-matter. Use GitHub Flavored Markdown (GFM) for content.
- **Keep it Simple**: Prioritize minimalism in design and code, adhering to the "Jekyll Now" philosophy of avoiding unnecessary runtime dependencies.
- **Self-Documenting Code**: HTML layouts and SCSS styles should be clean and readable. Use descriptive class names and avoid deep nesting in SCSS.
- **Asset Management**: Optimize images before adding them to the repository to keep the site fast and responsive.
- **No Over-Engineering**: Avoid introducing heavy JavaScript frameworks or complex build pipelines unless explicitly requested. Rely on static generation and basic Vanilla JS/CSS when possible.
