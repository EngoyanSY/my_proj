#!/bin/bash

# Автоматически переходим в корень проекта (на один уровень выше папки mlflow)
cd "$(dirname "$0")/.."

# Активируем виртуальное окружение, в котором установлен mlflow
source .venv_my_project/Scripts/activate

# Создаем папку mlflow, если её еще нет
mkdir -p mlflow

# Запускаем MLflow локально
# --backend-store-uri: указывает путь к SQLite БД (будет создан файл mlflow/mlflow.db)
# --default-artifact-root: папка, куда будут сохраняться модели, графики и т.д.
mlflow server \
    --backend-store-uri sqlite:///mlflow/mlflow.db \
    --default-artifact-root ./mlflow/mlartifacts \
    --host 127.0.0.1 \
    --port 5000