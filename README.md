# Student ML API — Advanced MLOps Exercise

A containerized and versioned Flask prediction API demonstrating a complete MLOps workflow using Git, GitHub, GitHub Actions, Docker, automated testing, semantic versioning, and GitHub Container Registry (GHCR).

This project was developed as an Advanced MLOps exercise to demonstrate a professional software delivery lifecycle from feature development to automated validation, release, deployment, traceability, and rollback.

---

## 1. Project Overview

`student-ml-api` is a small Flask-based prediction service used to demonstrate practical MLOps concepts.

The application provides:

- A health endpoint for application and model metadata
- A prediction endpoint for simple inference
- Automated API tests using `pytest`
- Continuous Integration using GitHub Actions
- Docker containerization
- Automated Docker image publishing to GHCR
- Semantic versioning using Git tags
- Versioned and immutable container artifacts
- OCI image metadata
- Commit-SHA Docker image tags
- Reproducible deployment
- Rollback to previous releases
- Docker layer caching optimization
- Failure analysis and troubleshooting

The development workflow used throughout the project is:

```text
Feature Branch
      ↓
Pull Request
      ↓
Automated CI
      ↓
Code Review
      ↓
Merge into main
      ↓
Semantic Version Tag
      ↓
Automated Release Pipeline
      ↓
Docker Image
      ↓
GitHub Container Registry
```

Development changes are introduced through feature branches and Pull Requests rather than being developed directly on the protected `main` branch.

---

## 2. Technology Stack

The project uses:

- Python 3.13
- Flask
- Pytest
- Git
- GitHub
- GitHub Actions
- Docker
- GitHub Container Registry (GHCR)
- Semantic Versioning
- OCI image metadata

---

## 3. Repository Structure

```text
student-ml-api/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
│
├── docs/
│   └── Documentation.pdf
│
├── tests/
│   └── test_app.py
│
├── .dockerignore
├── .gitignore
├── app.py
├── Dockerfile
├── pytest.ini
├── README.md
├── requirements.txt
└── VERSION
```

### Important Files

| File | Purpose |
|---|---|
| `app.py` | Flask API implementation |
| `tests/test_app.py` | Automated API tests |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container image definition |
| `.dockerignore` | Excludes unnecessary files from Docker build context |
| `VERSION` | Stores the application version |
| `.github/workflows/ci.yml` | Continuous Integration workflow |
| `.github/workflows/release.yml` | Automated release and container publishing workflow |
| `docs/Documentation.pdf` | Assignment report and implementation evidence |

---

## 4. Application API

The application exposes a health endpoint and a prediction endpoint.

### Health Endpoint

```http
GET /health
```

For application version `1.1.0`, the endpoint returns application and model metadata.

Example:

```json
{
  "status": "healthy",
  "application": "student-ml-api",
  "application_version": "1.1.0",
  "model_version": "model-1"
}
```

The health endpoint can be used to verify that the service is running and to identify the deployed application/model version.

---

### Prediction Endpoint

```http
POST /predict
```

Example request:

```json
{
  "value": 10
}
```

Example response:

```json
{
  "input": 10.0,
  "prediction": 20.0
}
```

The demonstration prediction logic multiplies the supplied numeric input by `2`.

The endpoint also validates missing and invalid inputs.

---

## 5. Running the Application Locally

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The API is available at:

```text
http://localhost:5000
```

Test the health endpoint:

```bash
curl http://localhost:5000/health
```

Test the prediction endpoint:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"value":10}'
```

---

## 6. Automated Testing

Automated tests are implemented using `pytest`.

Run the complete test suite with:

```bash
pytest -v
```

The test suite validates:

1. Successful health endpoint response
2. Successful prediction
3. Missing prediction input
4. Invalid prediction input

A successful local test execution produces:

```text
4 passed
```

These tests are also executed automatically by the CI pipeline.

---

## 7. Git Branching Strategy

A feature-branch workflow was followed throughout the project.

The general development process was:

```text
main
  ↓
feature branch
  ↓
development commits
  ↓
push branch
  ↓
Pull Request
  ↓
CI validation
  ↓
review
  ↓
merge
```

Examples of work completed through Pull Requests include:

- Prediction API implementation
- Automated release workflow
- GHCR publishing correction
- Model metadata/version 1.1.0
- OCI image metadata
- Commit-SHA Docker image tagging
- Assignment documentation

This provides a traceable development history and prevents uncontrolled development directly on `main`.

---

## 8. Branch Protection

The `main` branch was configured with branch protection rules.

The workflow requires changes to go through a Pull Request before being merged.

Automated status checks are used as quality gates so that code changes can be validated before integration into the main branch.

This enforces the intended workflow:

```text
Feature Branch → Pull Request → CI → Review → Merge
```

---

## 9. Professional Pull Requests

Multiple Pull Requests were created during the project.

Pull Requests include structured information such as:

- Summary
- Changes
- Testing performed
- Docker/release impact
- Validation information
- Completion checklist

The PR workflow provides traceability between development changes, automated validation, reviews, and merge commits.

---

## 10. Continuous Integration

Continuous Integration is implemented using GitHub Actions.

Workflow file:

```text
.github/workflows/ci.yml
```

The CI workflow validates proposed changes before they are accepted.

Typical CI stages include:

```text
Checkout Repository
        ↓
Setup Python
        ↓
Install Dependencies
        ↓
Run Pytest
        ↓
Validate Docker Build
```

The CI workflow verifies both application behavior and container buildability.

---

## 11. CI Failure Demonstration

A deliberate test failure was introduced to demonstrate that the CI pipeline correctly detects invalid changes.

The expected health result was intentionally changed so that it did not match the application's actual response.

GitHub Actions detected the failed assertion and marked the CI execution as failed.

The error was then corrected and the workflow was executed again successfully.

This demonstrates that CI acts as an automated quality gate rather than simply running commands without enforcing their result.

---

## 12. Docker Containerization

The application is packaged as a Docker image.

The Dockerfile uses an explicitly versioned Python base image rather than `python:latest`.

It demonstrates Docker practices including:

- Explicit base image version
- `WORKDIR`
- Dependency installation
- Dependency-first `COPY` ordering
- `pip --no-cache-dir`
- Application source copying
- `EXPOSE`
- Explicit container command
- OCI image metadata

---

## 13. Docker Ignore File

The `.dockerignore` file prevents unnecessary development files from being copied into the Docker build context.

Examples include:

```text
.git
.github
__pycache__
*.pyc
.venv
.env
```

This keeps the build context smaller and avoids including unnecessary or sensitive development files in the image.

---

## 14. Building the Docker Image Locally

A versioned Docker image can be built using:

```bash
docker build -t student-ml-api:1.0.0 .
```

Run it with:

```bash
docker run -d \
  --name student-ml-api \
  -p 5000:5000 \
  student-ml-api:1.0.0
```

Verify the running container:

```bash
docker ps
```

Test the application:

```bash
curl http://localhost:5000/health
```

---

## 15. Semantic Versioning

Application releases use semantic version tags.

Important project releases include:

```text
v1.0.0
v1.1.0
```

Additional patch tags were created while improving the release workflow:

```text
v1.0.1
v1.1.1
```

The `v1.1.1` tag was used to exercise the improved release workflow and image metadata/SHA-tag publishing. The application metadata itself remained at application version `1.1.0`.

Git tags provide a permanent link between a source-code state and a release.

---

## 16. Automated Release Pipeline

Release automation is implemented using:

```text
.github/workflows/release.yml
```

The release workflow is triggered by semantic-version Git tags matching:

```text
v*.*.*
```

The release pipeline performs the following process:

```text
Git Version Tag
      ↓
Checkout Repository
      ↓
Setup Python
      ↓
Install Dependencies
      ↓
Run Automated Tests
      ↓
Extract Release Version
      ↓
Authenticate with GHCR
      ↓
Build Docker Image
      ↓
Apply OCI Metadata
      ↓
Publish Version Tag
      ↓
Publish latest Tag
      ↓
Publish Commit-SHA Tag
```

Docker images are published through GitHub Actions rather than manually uploaded.

---

## 17. GitHub Container Registry

Published images are stored in GitHub Container Registry.

Registry:

```text
ghcr.io/samiyasaleem/student-ml-api
```

Example pull:

```bash
docker pull ghcr.io/samiyasaleem/student-ml-api:1.1.0
```

Versioned images produced during the assignment include:

```text
1.0.0
1.0.1
1.1.0
1.1.1
latest
3d275cd
```

Explicit version tags are retained instead of relying only on `latest`.

This makes deployments reproducible and enables rollback to previous releases.

---

## 18. CI and Release Separation

CI and release responsibilities are intentionally separated.

### CI Workflow

The CI workflow:

- Runs tests
- Validates the application
- Validates the Docker build
- Does not publish production Docker images

### Release Workflow

The release workflow:

- Is triggered by release tags
- Runs validation
- Builds the release image
- Authenticates with GHCR
- Publishes versioned container artifacts

This separation prevents every feature branch or Pull Request from publishing a production/release image.

---

## 19. Application Version 1.1.0 and Model Metadata

A later feature introduced additional version metadata.

The health endpoint for version `1.1.0` returns:

```json
{
  "status": "healthy",
  "application": "student-ml-api",
  "application_version": "1.1.0",
  "model_version": "model-1"
}
```

This makes the deployed application and model versions visible through the API.

The change was implemented through a feature branch, Pull Request, automated CI, review, and merge.

---

## 20. Release Traceability

One of the main goals of the project was to establish traceability from a code change to the exact deployed container artifact.

For the `v1.1.0` release:

```text
Pull Request
    #4
     ↓
Merge Commit
    da51780
     ↓
Git Tag
    v1.1.0
     ↓
Docker Image
    ghcr.io/samiyasaleem/student-ml-api:1.1.0
     ↓
Image Digest
    sha256:c62b24c72834db64053720b111d339a6b52c1cebfaa6151e47ab0c416a65dff3
```

This allows a deployed container to be traced back to the corresponding release and source-code history.

---

## 21. OCI Image Metadata

The Docker image was enhanced with OCI metadata labels.

Build arguments include:

```text
APP_VERSION
GIT_COMMIT
BUILD_DATE
```

OCI metadata records information including:

- Image title
- Application version
- Git revision
- Source repository
- Build date

For the later release workflow execution, metadata included:

```text
Version: 1.1.1
Commit: 3d275cda112d81bd4521396988aa4b1901fc85aa
Repository: https://github.com/SamiyaSaleem/student-ml-api
Build Date: 2026-09-10T07:49:06Z
```

This metadata improves artifact auditing and traceability.

---

## 22. Commit-SHA Docker Tag

The release workflow was extended to publish an additional Docker image tag based on the short Git commit SHA.

For the relevant release:

```text
3d275cd
```

The release generated:

```text
ghcr.io/samiyasaleem/student-ml-api:1.1.1
ghcr.io/samiyasaleem/student-ml-api:latest
ghcr.io/samiyasaleem/student-ml-api:3d275cd
```

These tags referenced the same published artifact with digest:

```text
sha256:c26c9d2acd198d8c782d8a56f770b716f4360d46852a89d3f7d02269b3c593af
```

A commit-SHA tag provides a direct relationship between a container artifact and the Git commit used to produce it.

---

## 23. Docker Layer Caching

Docker layer caching behavior was investigated by performing controlled builds.

The Dockerfile follows dependency-first ordering:

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY VERSION .
```

### Changing Only `app.py`

When only application source code was changed:

- Earlier Docker layers remained cached
- `requirements.txt` remained unchanged
- The dependency installation layer remained cached
- Application-related layers were rebuilt

### Changing `requirements.txt`

When `requirements.txt` was changed:

- The requirements layer was invalidated
- `pip install` executed again
- Following layers were rebuilt

This demonstrates why dependency files should be copied and installed before frequently changing source code.

Using:

```dockerfile
COPY . .
RUN pip install -r requirements.txt
```

too early would cause unrelated project changes to invalidate the dependency installation layer and result in slower builds.

---

## 24. Reproducible Deployment

The project demonstrates deployment directly from an existing registry artifact.

Example:

```bash
docker pull ghcr.io/samiyasaleem/student-ml-api:1.1.0
```

Run the downloaded image:

```bash
docker run -d \
  --name demo-student-ml-api \
  -p 5000:5000 \
  ghcr.io/samiyasaleem/student-ml-api:1.1.0
```

Verify:

```bash
curl http://localhost:5000/health
```

This deployment does not require rebuilding the application from source.

---

## 25. Rollback

Because previous versioned images remain available in GHCR, the application can be rolled back without rebuilding source code.

For example, pull the previous stable release:

```bash
docker pull ghcr.io/samiyasaleem/student-ml-api:1.0.0
```

Run the previous version:

```bash
docker run -d \
  --name rollback-student-ml-api \
  -p 5000:5000 \
  ghcr.io/samiyasaleem/student-ml-api:1.0.0
```

Verify:

```bash
curl http://localhost:5000/health
```

The rollback deployment returns version `1.0.0`.

This demonstrates that an older, already-published artifact can be restored without:

- Modifying source code
- Reinstalling dependencies
- Rebuilding the Docker image

---

## 26. Failure Analysis

Two deliberate failures were reproduced and diagnosed during the exercise.

### Failure 1 — Failed Pytest

#### Symptom

The prediction test failed.

Pytest reported:

```text
1 failed, 3 passed
```

and the assertion showed:

```text
assert 20.0 == 200
```

#### Root Cause

The expected prediction value in the test was deliberately changed from the correct value `20.0` to the incorrect value `200`.

The application itself continued to return the correct prediction.

#### Correction

The expected value was restored to `20.0`.

After the correction:

```text
4 passed
```

This demonstrates how automated testing detects application/test inconsistencies before integration.

---

### Failure 2 — Incorrect Docker Port Mapping

The container was deliberately started using:

```bash
docker run -d \
  --name failure-port-demo \
  -p 5002:5000 \
  ghcr.io/samiyasaleem/student-ml-api:1.1.1
```

#### Symptom

The following request failed:

```bash
curl http://localhost:5000/health
```

because nothing was mapped to host port `5000`.

#### Root Cause

Docker was configured with:

```text
5002:5000
```

This means:

```text
Host Port 5002 → Container Port 5000
```

Therefore, the application was accessible through:

```bash
curl http://localhost:5002/health
```

#### Correction

Use the intended host mapping:

```text
5000:5000
```

This failure demonstrates the importance of understanding the difference between host and container ports.

---

## 27. End-to-End Demonstration

The final project was demonstrated using the complete deployment workflow.

### Clone Repository

```bash
git clone https://github.com/SamiyaSaleem/student-ml-api.git
cd student-ml-api
```

### Inspect Git History

```bash
git log --oneline --decorate --graph -10
```

### Inspect Release Tags

```bash
git tag --list
```

Important tags include:

```text
v1.0.0
v1.0.1
v1.1.0
v1.1.1
```

### Pull Published Image

```bash
docker pull ghcr.io/samiyasaleem/student-ml-api:1.1.0
```

### Run Published Image

```bash
docker run -d \
  --name demo-student-ml-api \
  -p 5000:5000 \
  ghcr.io/samiyasaleem/student-ml-api:1.1.0
```

### Test Health Endpoint

```bash
curl http://localhost:5000/health
```

### Test Prediction Endpoint

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"value":10}'
```

Expected prediction:

```json
{
  "input": 10.0,
  "prediction": 20.0
}
```

### Roll Back

Stop/remove the newer deployment and run the previously published `1.0.0` artifact:

```bash
docker pull ghcr.io/samiyasaleem/student-ml-api:1.0.0

docker run -d \
  --name rollback-student-ml-api \
  -p 5000:5000 \
  ghcr.io/samiyasaleem/student-ml-api:1.0.0
```

The health endpoint confirms that version `1.0.0` is running.

---

## 28. Assignment Evidence

The complete assignment report containing implementation and demonstration screenshots is included in:

```text
docs/Documentation.pdf
```

The report contains evidence of:

- GitHub repository structure
- Professional Pull Requests
- Failed CI execution
- Successful CI execution
- Successful release execution
- GHCR versioned images
- Git release tags
- Repository cloning
- Git history
- Pull Request history
- GitHub Actions history
- Registry image pull
- Container execution
- API verification
- Rollback

---

## 29. Key MLOps Concepts Demonstrated

This project demonstrates the following MLOps principles:

**Version Control**  
Application and infrastructure configuration are maintained in Git.

**Feature Branch Development**  
Changes are developed outside the protected `main` branch.

**Pull Request Workflow**  
Changes are reviewed and validated before integration.

**Continuous Integration**  
Tests and Docker builds run automatically.

**Automated Release**  
Release tags trigger container build and publishing.

**Immutable Versioned Artifacts**  
Previous Docker versions remain available in the registry.

**Semantic Versioning**  
Git tags and Docker tags identify releases.

**Traceability**  
PRs, commits, Git tags, Docker tags, OCI metadata, and image digests can be connected.

**Reproducibility**  
A published image can be pulled and executed without rebuilding source code.

**Rollback**  
A previous stable image can be redeployed directly from the registry.

**Failure Detection**  
Automated tests and controlled failure scenarios demonstrate troubleshooting and quality gates.

**Build Optimization**  
Docker layer ordering improves caching and avoids unnecessary dependency installation.

---

## 30. Final MLOps Workflow

```text
Developer Change
      ↓
Feature Branch
      ↓
Commit
      ↓
Push to GitHub
      ↓
Pull Request
      ↓
GitHub Actions CI
      ↓
Tests + Docker Build Validation
      ↓
Code Review
      ↓
Merge into Protected Main
      ↓
Semantic Version Git Tag
      ↓
Release GitHub Action
      ↓
Tests
      ↓
Docker Build
      ↓
OCI Metadata
      ↓
Version + latest + Commit-SHA Tags
      ↓
GitHub Container Registry
      ↓
Pull Published Artifact
      ↓
Deploy Container
      ↓
Verify API
      ↓
Rollback to Previous Version if Required
```

---

## Author

**SamiyaSaleem**

Advanced MLOps Exercise — Student ML API
