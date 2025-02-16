# Тестовое задание по созданию карточки организации

## Запуск и работа

### Запуск

- Клонировать repository
- Ввести в терминал ```sudo docker compose up --build```(если вы на Linux) иначе запустить через Docker Desktop

После этих действий приложение готово к работе


> [!NOTE]
> Приложение работает на порту 8080, для работы используйте путь http://localhost:8080.
> Информацию об эндпоинтах можно посмотреть в документации Swagger (OpenAPI) `/docs` или `/redoc`

> [!NOTE]
> Если возникнут проблемы с миграциями, в папке build в файле app_entrypoint
> увеличить sleep и пересобрать приложение, ```sudo docker compose down```, ```sudo docker compose up --build```
> или же прогнать зависимости руками(обратите внимание на файл .env,
> там необходимо поменять значение host на localhost а port на 4545 )```alembic upgrage head```,
> после чего прогнать тестовые данные
> ```make seed``` или же ```python -m seeds.seed```

## Тестовые данные

### Организации

- {
  "id": "87dc34ad-295f-4e8d-9433-9dad5ce23f78",
  "name": "Вкусно и точка",
  "address": "ул. Балчуг, 5, Москва",
  "phones": [
  "+7-999-888-77-66"
  ],
  "activities": [
  "food"
  ]
  }

- {
  "id": "35f083cc-d237-4c1f-9725-7ac5e20efb45",
  "name": "ООО Компьютеры",
  "address": "ул. Солянка, 1/2 стр. 1, Москва",
  "phones": [
  "+7-912-345-67-89",
  "+7-987-654-32-10"
  ],
  "activities": [
  "computer",
  "accessory"
  ]
  }
- {
  "id": "3356f1bc-f133-4d5d-a23a-f8176eb78105",
  "name": "Nvidia",
  "address": "ул. Солянка, 1/2 стр. 1, Москва",
  "phones": [
  "+7-926-123-45-67"
  ],
  "activities": [
  "electronic",
  "computer"
  ]
  }
- {
  "id": "6946a71a-fd60-4d40-afc4-994961bef646",
  "name": "М-Видео",
  "address": "ул. Балчуг, 7, Москва",
  "phones": [
  "+7-495-123-45-67"
  ],
  "activities": [
  "electronic",
  "accessory"
  ]
  }

## Использовавшиеся инструменты

1. Python —— язык программирования
1. FastAPI —— веб-фреймворк
1. PostgreSQL —— база данных
1. SQLAlchemy —— ORM
1. Alembic —— мигратор
1. PostGis —— гео-данные

> [!NOTE]
> Подробнее узнать о всех зависимостях проекта можно в [файле pyproject.toml](pyproject.toml)