# Public Release Checklist

Complete this checklist before making the repository public or publishing a versioned release.

## Safety and privacy of repository contents

- [ ] Confirm every dataset row is fictional, synthetic, or fully sanitized.
- [ ] Confirm no content reveals non-public vehicle behavior, architecture, validation results, supplier information, customer information, or internal release gates.
- [ ] Confirm no user utterance logs, telemetry, location data, VINs, account identifiers, or personal data are present.
- [ ] Confirm no model prompts, routing logic, endpoints, credentials, or configuration secrets are present.

## GitHub surfaces

- [ ] Inspect all branches and complete git history for material that must not become public.
- [ ] Inspect issues, pull requests, review comments, discussions, wiki pages, releases, tags, and project boards.
- [ ] Inspect Actions logs, workflow artifacts, caches, screenshots, and attachments.
- [ ] Check repository description, topics, social preview image, homepage, and contributor metadata.

## Quality baseline

- [ ] The current README, `METHODOLOGY.md`, and `DATASET_CARD.md` accurately describe the implementation.
- [ ] Tests and CI pass on the intended release commit.
- [ ] Sample data validates with the CLI.
- [ ] Any reported result includes dataset/rubric/evaluator versions and known limitations.
- [ ] No public material claims safety certification, regulatory approval, or production readiness.

## Release decision

- [ ] Create the release as a draft, verify its notes and assets, then publish.
- [ ] Record the release commit SHA, reviewer, date, and CI run in the release notes.
- [ ] Publish a new patch version for corrections rather than changing a published release artifact.
