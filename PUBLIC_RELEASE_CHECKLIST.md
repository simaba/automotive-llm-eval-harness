# Public Release Checklist

Use this checklist before changing the repository visibility to public.

## Required before publishing

- [ ] Confirm all datasets are fictional, synthetic, or fully sanitized.
- [ ] Confirm no real vehicle logs, customer utterances, test traces, or production examples are committed.
- [ ] Confirm no employer, supplier, vendor, customer, or internal project names appear in examples.
- [ ] Confirm no unreleased product behavior, routing rules, architecture, launch gates, or acceptance criteria are included.
- [ ] Confirm no API keys, tokens, credentials, connector details, or account identifiers are present.
- [ ] Confirm benchmark results are clearly labeled as sample or exploratory.
- [ ] Confirm the README does not imply safety certification, production validation, regulatory approval, or endorsement by any automaker or supplier.
- [ ] Confirm the license, README, and quick-start commands are accurate.

## Recommended before promotion

- [ ] Add at least one fully synthetic multilingual benchmark pack.
- [ ] Add schema validation for dataset rows.
- [ ] Add a scoring-methodology note explaining weights and limitations.
- [ ] Add sample CLI output.
- [ ] Run tests locally after a fresh clone.

## Final manual review

Before publishing, search the repo for sensitive terms such as company names, project names, internal acronyms, vehicle programs, vendor names, emails, tokens, keys, and private paths.

This checklist is a publication aid, not a security guarantee.
