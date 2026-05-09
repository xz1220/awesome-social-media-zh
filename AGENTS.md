# AGENTS

This repository is a public awesome list for AI Native creators and AI Agent
users who want to build content creation workflows for Chinese social media.

## Role

Maintain the project as a useful, verifiable resource list:

- Keep the README focused on practical resources for AI Agent users, AI Native
  creators, indie developers, and small teams.
- Prefer workflow-oriented categories over generic tool piles.
- Prioritize resources that can become agent tools, data sources, context,
  templates, review rubrics, or automation nodes.
- Do not add private facts, screenshots, account backend data, chat records, or
  user/customer information.
- Do not invent tool capabilities, platform rules, pricing, traffic numbers, or
  case-study performance.

## Resource Entries

Use the recommended format unless a section has a clear reason to differ:

```markdown
- [Resource name](https://example.com) - What problem it solves and who it fits; key limitation or risk; observed: YYYY-MM-DD.
```

Chinese entries should use:

```markdown
- [资源名](https://example.com) - 解决什么问题，适合谁；主要限制或风险；观察日期：YYYY-MM-DD。
```

When adding resources:

- Prefer official pages, public docs, public repositories, or otherwise stable
  sources.
- Verify links before claiming that a resource is available.
- Use `null`-style uncertainty in prose such as "待验证" instead of guessing.
- Keep notes concise; longer reviews should become separate documents only after
  the list outgrows the README.
- Avoid generic social media tools unless they clearly fit an AI Native content
  workflow.

## Validation

Run the smallest relevant check after edits:

```bash
make validate
```

If validation fails because a rule is too strict for a legitimate entry, update
the rule and explain why in the change.
