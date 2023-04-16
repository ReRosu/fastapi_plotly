# fastapi_plotly
Learning to join fastapi and plotly

УСТАНОВКА
------------
### Настройка системы
~~~
sudo apt update
sudo apt upgrade
apt autoremove
sudo apt install python3.11
~~~

### Установка и конфигурация poetry
~~~
curl -sSL https://install.python-poetry.org
~~~
или
~~~
python -m pip install poetry
~~~
~~~
poetry config virtualenvs.in-project true
poetry --version
~~~

### Установка репозитория
~~~
git clone git@github.com:ReRosu/fastapi_plotly.git
cd fastapi_plotly
poetry env use python3.11
poetry install
~~~

### Запуск приложения
~~~
poetry shell
python main.py
~~~

