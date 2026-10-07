<h2>Первый запуск</h2>

Установка виртуального окружения
```
python3 -m venv .venv_my_project        # Linux
```
```
python -m venv .venv_my_project         # Windows
```

Активация виртуального окружения
```
source .venv_my_project/bin/activate    # Linux
```
```
.venv_my_project\Scripts\activate       # Windows
```
Установка библиотек

```
python -m pip install --upgrade pip
pip install -r requirements.txt -i https://pypi.doubanio.com/simple
```

Запуск скрипта
```
./mlflow/start_mlflow.sh
```
```
sh ./mlflow/start_mlflow.sh
```
<hr>

Лучший run_id
```
6f56fb9b9cf645e992c04e8a1b1100d9
```
Репозиторий <a href="https://www.kaggle.com/datasets/laveshjadon/ai-impact-on-students" target="_blank" rel="noopener noreferrer">ai-impact-on-students</a> 
