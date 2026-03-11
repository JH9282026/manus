# Security Analysis

Detailed security review methodologies and vulnerability detection patterns.

---

## Vulnerability Detection by Language

### JavaScript/TypeScript

| Vulnerability | Pattern to Detect | Fix |
|---|---|---|
| XSS | `innerHTML`, `dangerouslySetInnerHTML`, unescaped template literals | Sanitize with DOMPurify, use textContent |
| Prototype pollution | Deep merge without safeguard, `__proto__` access | Validate keys, use Object.create(null) |
| Path traversal | User input in `fs.readFile`, `path.join` without validation | Validate paths, use allowlists |
| ReDoS | Complex regex with nested quantifiers | Simplify regex, use RE2, add timeout |
| SSRF | User-controlled URLs in fetch/axios | URL allowlisting, disable redirects |
| Hardcoded secrets | API keys, tokens in source code | Environment variables, secret managers |

### Python

| Vulnerability | Pattern to Detect | Fix |
|---|---|---|
| SQL injection | f-strings in SQL queries, string concatenation | Parameterized queries, ORM |
| Command injection | `os.system()`, `subprocess.call(shell=True)` | `subprocess.run()` with list args, no shell |
| Deserialization | `pickle.loads()` on untrusted data | Use JSON, validate before deserialize |
| Path traversal | User input in `open()`, `os.path.join` | Validate paths, chroot |
| SSTI | User input in Jinja2 `Template()` | Use `render_template()`, sandbox |

### SQL

| Vulnerability | Pattern to Detect | Fix |
|---|---|---|
| SQL injection | String concatenation in queries | Parameterized queries, stored procedures |
| Privilege escalation | Excessive GRANT permissions | Principle of least privilege |
| Data exposure | SELECT * without column filtering | Explicit column selection |
| Missing encryption | Sensitive data stored unencrypted | Column-level encryption, TDE |

---

## Dependency Security

### Vulnerability Scanning

- Run `npm audit` / `pip audit` / `cargo audit` in CI pipeline
- Monitor with Snyk, Dependabot, or Renovate
- Set severity thresholds: block deployment for Critical/High
- Establish SLA for vulnerability remediation (Critical: 24h, High: 7d, Medium: 30d)

### Supply Chain Security

- Verify package integrity (checksums, signatures)
- Pin dependency versions in production
- Review new dependencies before adoption (maintainers, history, downloads)
- Use lockfiles and reproducible builds
- Audit transitive dependencies, not just direct
