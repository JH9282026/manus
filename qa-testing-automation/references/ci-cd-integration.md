# CI/CD Integration for Test Automation

Best practices for integrating automated tests into continuous integration and deployment pipelines.

---

## CI/CD Testing Strategy

### Test Pyramid in CI/CD

```
        /\
       /  \    E2E Tests (10%)
      /    \   - Run on staging
     /------\  - Critical user journeys only
    /        \ Integration Tests (20%)
   /          \ - API tests
  /            \ - Service layer validation
 /--------------\ Unit Tests (70%)
                  - Fast, isolated
                  - Run on every commit
```

### Pipeline Stages

1. **Commit Stage** (Fast feedback: <5 min)
   - Unit tests
   - Linting
   - Static analysis

2. **Acceptance Stage** (Medium: 10-20 min)
   - Integration tests
   - API tests
   - Smoke tests

3. **Deployment Stage** (Slower: 20-40 min)
   - Full E2E test suite
   - Performance tests
   - Security scans

---

## GitHub Actions

### Playwright Example

```yaml
name: Playwright Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight

jobs:
  test:
    timeout-minutes: 60
    runs-on: ubuntu-latest
    strategy:
      matrix:
        browser: [chromium, firefox, webkit]
    steps:
    - uses: actions/checkout@v3
    
    - uses: actions/setup-node@v3
      with:
        node-version: 18
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Install Playwright Browsers
      run: npx playwright install --with-deps ${{ matrix.browser }}
    
    - name: Run Playwright tests
      run: npx playwright test --project=${{ matrix.browser }}
      env:
        BASE_URL: ${{ secrets.STAGING_URL }}
    
    - uses: actions/upload-artifact@v3
      if: always()
      with:
        name: playwright-report-${{ matrix.browser }}
        path: playwright-report/
        retention-days: 30
    
    - name: Publish Test Results
      uses: EnricoMi/publish-unit-test-result-action@v2
      if: always()
      with:
        files: test-results/**/*.xml
```

### Parallel Execution with Sharding

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        shard: [1, 2, 3, 4]
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-node@v3
    - run: npm ci
    - run: npx playwright install --with-deps
    - run: npx playwright test --shard=${{ matrix.shard }}/4
```

---

## GitLab CI

### Complete Pipeline

```yaml
stages:
  - build
  - test
  - deploy

variables:
  SELENIUM_HOST: selenium__standalone-chrome
  SELENIUM_PORT: 4444

build:
  stage: build
  image: node:18
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour

unit-tests:
  stage: test
  image: node:18
  script:
    - npm ci
    - npm run test:unit
  coverage: '/Statements\s+:\s+(\d+\.\d+)%/'
  artifacts:
    reports:
      junit: junit.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

api-tests:
  stage: test
  image: node:18
  script:
    - npm ci
    - npm run test:api
  artifacts:
    when: always
    reports:
      junit: api-test-results.xml

e2e-tests:
  stage: test
  image: mcr.microsoft.com/playwright:v1.40.0-focal
  services:
    - name: selenium/standalone-chrome:latest
      alias: selenium
  script:
    - npm ci
    - npx playwright test
  artifacts:
    when: always
    paths:
      - playwright-report/
      - test-results/
    expire_in: 7 days
  only:
    - main
    - develop

deploy-staging:
  stage: deploy
  script:
    - echo "Deploying to staging"
  environment:
    name: staging
  only:
    - develop
```

---

## Jenkins

### Declarative Pipeline

```groovy
pipeline {
    agent any
    
    tools {
        nodejs 'NodeJS 18'
    }
    
    parameters {
        choice(name: 'BROWSER', choices: ['chrome', 'firefox', 'edge'], description: 'Browser to run tests')
        choice(name: 'ENVIRONMENT', choices: ['staging', 'production'], description: 'Environment')
    }
    
    environment {
        BASE_URL = credentials('staging-url')
        API_KEY = credentials('api-key')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'npm ci'
            }
        }
        
        stage('Unit Tests') {
            steps {
                sh 'npm run test:unit'
            }
            post {
                always {
                    junit 'junit.xml'
                }
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm run build'
            }
        }
        
        stage('E2E Tests') {
            parallel {
                stage('Chrome') {
                    steps {
                        sh 'npx playwright test --project=chromium'
                    }
                }
                stage('Firefox') {
                    steps {
                        sh 'npx playwright test --project=firefox'
                    }
                }
            }
            post {
                always {
                    publishHTML([
                        reportDir: 'playwright-report',
                        reportFiles: 'index.html',
                        reportName: 'Playwright Report'
                    ])
                    archiveArtifacts artifacts: 'test-results/**/*', allowEmptyArchive: true
                }
            }
        }
    }
    
    post {
        failure {
            emailext(
                subject: "Test Failure: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: """Test execution failed. Check console output at ${env.BUILD_URL}""",
                to: 'qa-team@example.com'
            )
        }
    }
}
```

---

## CircleCI

```yaml
version: 2.1

orbs:
  node: circleci/node@5.0

jobs:
  test:
    docker:
      - image: mcr.microsoft.com/playwright:v1.40.0-focal
    parallelism: 4
    steps:
      - checkout
      - node/install-packages:
          pkg-manager: npm
      - run:
          name: Install Playwright Browsers
          command: npx playwright install
      - run:
          name: Run tests
          command: |
            SHARD="$((${CIRCLE_NODE_INDEX} + 1))"
            npx playwright test --shard=${SHARD}/${CIRCLE_NODE_TOTAL}
      - store_test_results:
          path: test-results
      - store_artifacts:
          path: playwright-report

workflows:
  test-workflow:
    jobs:
      - test
```

---

## Azure DevOps

```yaml
trigger:
  - main
  - develop

pool:
  vmImage: 'ubuntu-latest'

variables:
  - group: test-secrets

stages:
- stage: Test
  jobs:
  - job: E2E_Tests
    strategy:
      matrix:
        Chrome:
          browserName: 'chromium'
        Firefox:
          browserName: 'firefox'
        Safari:
          browserName: 'webkit'
    steps:
    - task: NodeTool@0
      inputs:
        versionSpec: '18.x'
    
    - script: npm ci
      displayName: 'Install dependencies'
    
    - script: npx playwright install --with-deps $(browserName)
      displayName: 'Install Playwright browsers'
    
    - script: npx playwright test --project=$(browserName)
      displayName: 'Run Playwright tests'
      env:
        BASE_URL: $(STAGING_URL)
    
    - task: PublishTestResults@2
      condition: always()
      inputs:
        testResultsFormat: 'JUnit'
        testResultsFiles: 'test-results/**/*.xml'
    
    - task: PublishPipelineArtifact@1
      condition: always()
      inputs:
        targetPath: 'playwright-report'
        artifact: 'playwright-report-$(browserName)'
```

---

## Quality Gates

### Fail Pipeline on Test Failures

```yaml
# GitHub Actions
- name: Run tests
  run: npx playwright test
  # Pipeline fails if tests fail (default behavior)

# Allow specific failure threshold
- name: Run tests with threshold
  run: |
    npx playwright test || EXIT_CODE=$?
    if [ $EXIT_CODE -gt 5 ]; then
      echo "More than 5 tests failed"
      exit 1
    fi
```

### Code Coverage Gates

```yaml
- name: Check coverage
  run: |
    npm run test:coverage
    COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
    if (( $(echo "$COVERAGE < 80" | bc -l) )); then
      echo "Coverage $COVERAGE% is below 80%"
      exit 1
    fi
```

---

## Test Result Reporting

### Slack Notifications

```yaml
# GitHub Actions
- name: Slack Notification
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    text: 'Test Results'
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
    fields: repo,message,commit,author,action,eventName,ref,workflow
```

### Custom HTML Reports

```javascript
// reporter.js
class CustomReporter {
  onEnd(result) {
    const html = `
      <!DOCTYPE html>
      <html>
        <head><title>Test Report</title></head>
        <body>
          <h1>Test Results</h1>
          <p>Total: ${result.stats.total}</p>
          <p>Passed: ${result.stats.passed}</p>
          <p>Failed: ${result.stats.failed}</p>
        </body>
      </html>
    `;
    fs.writeFileSync('custom-report.html', html);
  }
}

module.exports = CustomReporter;
```

---

## Best Practices

### 1. Fast Feedback
- Run unit tests on every commit (<5 min)
- Run integration tests on PR (<15 min)
- Run full E2E suite nightly or on merge to main

### 2. Parallel Execution
- Use matrix strategies for cross-browser testing
- Implement sharding for large test suites
- Leverage cloud execution platforms

### 3. Test Data Management
- Use fixtures for consistent test data
- Reset database state between test runs
- Use API calls for test setup (faster than UI)

### 4. Flaky Test Handling
- Implement automatic retries (max 2-3)
- Track flaky tests separately
- Fix or quarantine consistently flaky tests

### 5. Security
- Store credentials in CI/CD secrets
- Never commit API keys or passwords
- Use environment-specific configurations

### 6. Artifact Management
- Store test reports for 30 days
- Archive screenshots/videos only on failure
- Keep build artifacts for rollback capability