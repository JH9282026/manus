# Code Audit Methodology

Structured approach for conducting formal code quality audits.

---

## Audit Process

### Phase 1: Preparation

1. Define audit scope (repository, directories, languages)
2. Gather context (architecture docs, known issues, recent changes)
3. Set up analysis tools and configure rulesets
4. Establish severity definitions and scoring criteria
5. Schedule interviews with development team

### Phase 2: Automated Analysis

Run automated tools in sequence:

| Tool Category | Examples | Detects |
|---|---|---|
| Static analysis | SonarQube, ESLint, pylint | Code smells, bugs, complexity |
| Security scanner | Snyk, Bandit, npm audit | Vulnerabilities, insecure patterns |
| Dependency checker | OWASP Dependency-Check, Dependabot | Known CVEs in dependencies |
| Test coverage | Istanbul, Coverage.py, JaCoCo | Untested code paths |
| Complexity analyzer | Lizard, radon | Function/file complexity |
| Duplication detector | jscpd, CPD | Copy-paste code |

### Phase 3: Manual Review

Focus manual review on areas automated tools miss:
- Business logic correctness
- Architecture and design patterns
- Authentication and authorization flows
- Data flow and trust boundaries
- Error handling completeness
- Race conditions and concurrency issues
- API design consistency

### Phase 4: Reporting

Structure the audit report:

**Executive Summary**
- Overall health grade (A-F)
- Critical issues requiring immediate action
- Key strengths and areas for improvement
- Risk assessment summary

**Detailed Findings**
- Each finding includes: description, severity, location, evidence, recommendation, effort estimate
- Group by category (security, performance, maintainability, style)
- Include code examples (before/after) for clarity

**Metrics Summary**
- Code coverage percentage
- Complexity distribution
- Duplication percentage
- Dependency vulnerability counts
- Trend analysis (if previous audit exists)

**Remediation Roadmap**
- Prioritized action items with timelines
- Quick wins (low effort, high impact)
- Strategic improvements (high effort, high impact)
- Ongoing practices to prevent regression

---

## Review Process Best Practices

### Pull Request Review Checklist

- [ ] Code compiles and passes all tests
- [ ] New code has corresponding tests
- [ ] No security vulnerabilities introduced
- [ ] Error handling is comprehensive
- [ ] Logging is appropriate (not excessive, not missing)
- [ ] Performance implications considered
- [ ] Documentation updated if needed
- [ ] Naming conventions followed
- [ ] No unnecessary dependencies added
- [ ] Backward compatibility maintained

### Review Culture Guidelines

- Review code, not the coder — keep feedback objective
- Praise good patterns alongside identifying issues
- Distinguish between blocking issues and suggestions
- Respond to reviews within one business day
- Keep PR size manageable (< 400 lines changed)
- Use automated checks for style — reserve human review for logic
