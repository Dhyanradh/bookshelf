# BookShelfHQ - DevOps Mock Project

This is a mock DevOps project designed to simulate a real-world workflow using both local and AWS resources.

## 🔧 Stack Overview

- **Language**: Python (Flask)
- **CI/CD**: GitHub Actions
- **Infra as Code**: Terraform
- **Provisioning**: Ansible (optional)
- **Containers**: Docker
- **Cloud**: AWS Free Tier (EC2, S3)
- **Monitoring**: Prometheus + Grafana (local)

## 📁 Project Structure

```
bookshelfhq/
│
├── backend/              # Flask app
├── docker-compose.yml    # For local dev
├── Dockerfile            # Containerize app
├── infra/                # Terraform scripts
├── .github/workflows/    # CI/CD pipeline
└── README.md             # Project overview
```

## 🗓️ Week 1 Plan

### ✅ Local Tasks
- [x] Create app repo (`bookshelfhq`)
- [x] Write Dockerfile for backend
- [x] Create `docker-compose.yml` for local testing
- [ ] Run & test app locally
- [ ] Push to GitHub

### ✅ AWS Tasks
- [ ] Create EC2 instance (t2.micro)
- [ ] SSH and install Docker + app
- [ ] Write Terraform code to automate EC2 creation
- [ ] Optional: Use Ansible to configure EC2
- [ ] Set up GitHub Actions to deploy on `main` push

## 🔐 IAM & Security
- Use IAM roles for Terraform
- Use key pairs for EC2 access
- Store secrets in GitHub Actions Secrets
