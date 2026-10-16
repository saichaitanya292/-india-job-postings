# India Job Hub

A two-sided job platform concept for job seekers and recruiters, designed with a responsive frontend.

## Job seeker experience
- Search and filter published jobs by keyword, location, category, work type, and experience.
- Save jobs in the browser.
- Apply through the employer's official application link.
- See recruiter/listing review status on job cards.

## Recruiter experience
- Submit recruiter and company details for verification review.
- Submit jobs with title, description, location, experience, salary, work type, and official application URL.
- Keep job submissions pending until review.
- A local demo review queue illustrates the intended admin approval flow.

## Important: current implementation is a frontend prototype
This repository is hosted as a static GitHub Pages site. The recruiter forms and approval queue currently use browser localStorage only. This means submissions are visible only in the same browser, and the demo approval controls are **not real identity verification or secure admin controls**. Do not use it for real recruiter verification or production job publishing yet.

To launch this as a real multi-user platform, add a secure backend and database, user authentication, role-based access control, an admin-only verification workflow, email verification, and server-side validation. Never trust a verification status or admin action stored in the browser. A real backend must enforce that only approved recruiters can publish listings.

## Publish with GitHub Pages
1. Open Settings → Pages in this repository.
2. Under Build and deployment, choose Deploy from a branch.
3. Select branch `main` and folder `/(root)`, then Save.
4. Expected URL: https://saichaitanya292.github.io/-india-job-postings/

## Job data
The frontend loads `data/jobs.json`. Demo placeholders are intentionally not presented as live jobs. Publish only genuine opportunities with accurate descriptions and official application links. The existing feed collector may be used to import permitted employer career-board feeds, but listings should be validated before publication.

## Safety and trust
- Do not charge job seekers to apply.
- Do not publish a recruiter as verified until the company and recruiter have been checked by an authorized reviewer.
- Keep an audit trail for approvals and job edits.
- Provide a way to report suspicious job listings.
- India Job Hub is an independent project and is not affiliated with Naukri or any employer listed.
