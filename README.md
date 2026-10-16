# India Job Hub

A responsive static job board for discovering opportunities across India. Designed for GitHub Pages and automated job-feed refreshes.

## Features
- Responsive search and filters for keyword, location, category, work type and recency.
- Save jobs locally in the browser.
- Direct links to original job application pages.
- JSON feed at data/jobs.json.
- Scheduled feed collection via GitHub Actions when configured.

## Publish with GitHub Pages
1. Open Settings → Pages in this repository.
2. Under Build and deployment, choose Deploy from a branch.
3. Select branch main and folder / (root), then Save.
4. The site should appear at https://saichaitanya292.github.io/-india-job-postings/ after Pages is enabled.

## Real job feeds
The initial data/jobs.json entries are demo placeholders, not verified vacancies. The feed collector will use explicitly configured employer board identifiers. Greenhouse and Lever public board endpoints are supported for participating employers. Add repository Actions variables GREENHOUSE_BOARDS and LEVER_SITES as comma-separated board identifiers. Do not scrape restricted sites or bypass access controls. Respect terms, rate limits and attribution.

## Disclaimer
India Job Hub is an independent job discovery project and is not affiliated with Naukri or the employers listed. Verify openings and application details on the employer's own website.
