cd ~/amphyx-dev-backend/
git checkout main
git pull
~/.local/share/pypoetry/venv/bin/poetry install
~/.local/share/pypoetry/venv/bin/poetry shell
python manage.py migrate
echo ✅ Done.
