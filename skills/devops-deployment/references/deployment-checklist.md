# Deployment Checklist

- Build is reproducible and artifact is immutable.
- Required tests and security checks are green.
- Config and secrets are environment-scoped.
- Database migrations are backward compatible.
- Rollout strategy (canary/blue-green) is selected.
- Rollback conditions and commands are documented.
- Post-deploy smoke checks are automated.
- Alert thresholds are verified before release.
