cd ~/amphyx-dev-backend/
git checkout main
git pull
~/.local/share/pypoetry/venv/bin/poetry install
~/.local/share/pypoetry/venv/bin/poetry run python --version
~/.local/share/pypoetry/venv/bin/poetry run python ~/amphyx-dev-backend/manage.py migrate
echo ✅ Done.
