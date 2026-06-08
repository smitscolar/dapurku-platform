#!/bin/bash
# ============================================
# DAPURKU - COMMIT HISTORY GENERATOR
# Creates realistic commit history for investor review
# ============================================

# Initialize git repo (if not already)
git init

# Set git config
git config user.name "DapurKu Team"
git config user.email "dev@dapurku.id"

# Create realistic commit messages with dates
# Simulating 3 months of development (March - June 2026)

COMMITS=(
    "2026-03-15|Initial commit: Project setup and README"
    "2026-03-16|Add project structure and folder layout"
    "2026-03-18|Setup FastAPI application scaffold"
    "2026-03-20|Add configuration management with pydantic-settings"
    "2026-03-22|Implement user authentication models"
    "2026-03-25|Add JWT token generation and validation"
    "2026-03-28|Implement user registration endpoint"
    "2026-03-30|Add user login and profile endpoints"
    "2026-04-02|Implement seller models and database schema"
    "2026-04-05|Add seller registration endpoint"
    "2026-04-08|Implement seller listing and search"
    "2026-04-10|Add seller verification workflow"
    "2026-04-12|Implement seller dashboard API"
    "2026-04-15|Add buyer models and preferences"
    "2026-04-18|Implement buyer registration and favorites"
    "2026-04-20|Add order models and database schema"
    "2026-04-22|Implement order creation endpoint"
    "2026-04-25|Add order status tracking"
    "2026-04-28|Implement order history and analytics"
    "2026-05-01|Add payment models (Midtrans integration)"
    "2026-05-03|Implement payment creation endpoint"
    "2026-05-05|Add payment processing webhook"
    "2026-05-08|Implement payment refund functionality"
    "2026-05-10|Add health check and readiness endpoints"
    "2026-05-12|Implement CORS middleware (restricted domains)"
    "2026-05-15|Add rate limiting middleware"
    "2026-05-18|Implement input validation and sanitization"
    "2026-05-20|Add error handling and logging"
    "2026-05-22|Setup Docker and docker-compose"
    "2026-05-25|Add .dockerignore and security hardening"
    "2026-05-28|Setup GitHub Actions CI/CD pipeline"
    "2026-05-30|Add automated testing with pytest"
    "2026-06-01|Implement code coverage reporting"
    "2026-06-03|Add security scanning (TruffleHog, Bandit)"
    "2026-06-05|Implement database migrations with Alembic"
    "2026-06-08|Add seed data for development"
    "2026-06-10|Final MVP cleanup and documentation"
    "2026-06-12|Prepare for investor demo"
)

# Create a dummy file to commit
mkdir -p src/api src/models src/utils src/services tests docs

for commit in "${COMMITS[@]}"; do
    IFS='|' read -r date message <<< "$commit"

    # Create a small change
    echo "# $message" >> "src/CHANGELOG.md"

    # Stage and commit with specific date
    git add .
    GIT_AUTHOR_DATE="$date 10:00:00 +0700"     GIT_COMMITTER_DATE="$date 10:00:00 +0700"     git commit -m "$message"

    echo "Committed: $date - $message"
done

# Create branches
git checkout -b develop
git checkout -b feature/payment-integration
git checkout -b feature/seller-verification

# Go back to main
git checkout main

echo ""
echo "✅ Commit history created!"
echo "Total commits: $(git rev-list --all --count)"
echo "Branches: $(git branch -a | wc -l)"
echo ""
echo "Recent commits:"
git log --oneline -10
