# Push LPPP-FitClem vers GitLab et GitHub

```bash
cd deploy/LPPP-FitClem

# Config identité locale (optionnel)
git config --local user.name "Lucas Tymen"
git config --local user.email "lucas.tymen@gmail.com"

# Init + commit initial
git init --initial-branch=main
git add .
git commit -m "Initial commit — landing FitClem candidature RMD"

# GitLab (HTTPS)
git remote add origin https://gitlab.com/LucasTymen/LPPP-FitClem.git
git push -u origin main

# GitHub
git remote add github https://github.com/LucasTymen/LPPP-FitClem.git
git push -u github main
```
