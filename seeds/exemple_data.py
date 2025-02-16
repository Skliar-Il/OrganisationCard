from uuid import UUID

from geoalchemy2 import WKTElement

from src.database.models import Building, Activity, Phone, Organisation

buildings = [
    Building(
        id=UUID("76f92275-21ac-41c5-a676-940c44dd08ee"),
        address="ул. Балчуг, 7, Москва",
        geom=WKTElement("POINT(55.746979688044085 37.626132247593915)", srid=4326)
    ),
    Building(
        id=UUID("08218030-fa48-4870-a0b6-2fb9add9c131"),
        address="ул. Балчуг, 5, Москва",
        geom=WKTElement("POINT(55.74727140939181 37.62615155501417)", srid=4326)
    ),
    Building(
        id=UUID("27557b87-5db5-4dcb-b8b2-2da1e748a331"),
        address="ул. Солянка, 1/2 стр. 1, Москва",
        geom=WKTElement("POINT(55.753815171388986 37.63788126542102)", srid=4326)
    ),
]

activities = [
    Activity(id=1, name="food", parent_id=None, depth=0),
    Activity(id=2, name="electronic", parent_id=None, depth=0),
    Activity(id=3, name="computer", parent_id=2, depth=1),
    Activity(id=4, name="accessory", parent_id=3, depth=2)
]

organisations = [
    Organisation(
        id=UUID("35f083cc-d237-4c1f-9725-7ac5e20efb45"),
        name="ООО Компьютеры",
        building_id=UUID("27557b87-5db5-4dcb-b8b2-2da1e748a331")
    ),
    Organisation(
        id=UUID("3356f1bc-f133-4d5d-a23a-f8176eb78105"),
        name="Nvidia",
        building_id=UUID("27557b87-5db5-4dcb-b8b2-2da1e748a331")
    ),
    Organisation(
        id=UUID("87dc34ad-295f-4e8d-9433-9dad5ce23f78"),
        name="Вкусно и точка",
        building_id=UUID("08218030-fa48-4870-a0b6-2fb9add9c131")
    ),
    Organisation(
        id=UUID("6946a71a-fd60-4d40-afc4-994961bef646"),
        name="М-Видео",
        building_id=UUID("76f92275-21ac-41c5-a676-940c44dd08ee")
    )
]

phones = [
    Phone(phone="+7-912-345-67-89", organisation_id=UUID("35f083cc-d237-4c1f-9725-7ac5e20efb45")),
    Phone(phone="+7-987-654-32-10", organisation_id=UUID("35f083cc-d237-4c1f-9725-7ac5e20efb45")),
    Phone(phone="+7-926-123-45-67", organisation_id=UUID("3356f1bc-f133-4d5d-a23a-f8176eb78105")),
    Phone(phone="+7-999-888-77-66", organisation_id=UUID("87dc34ad-295f-4e8d-9433-9dad5ce23f78")),
    Phone(phone="+7-495-123-45-67", organisation_id=UUID("6946a71a-fd60-4d40-afc4-994961bef646"))
]

organisations_activities = [
    # ООО Компьютеры
    {"activity_id": 3, "organisation_id": UUID("35f083cc-d237-4c1f-9725-7ac5e20efb45")},  # computer
    {"activity_id": 4, "organisation_id": UUID("35f083cc-d237-4c1f-9725-7ac5e20efb45")},  # accessory

    # Nvidia
    {"activity_id": 3, "organisation_id": UUID("3356f1bc-f133-4d5d-a23a-f8176eb78105")},  # computer
    {"activity_id": 2, "organisation_id": UUID("3356f1bc-f133-4d5d-a23a-f8176eb78105")},  # electronic

    # Вкусно и точка
    {"activity_id": 1, "organisation_id": UUID("87dc34ad-295f-4e8d-9433-9dad5ce23f78")},  # food

    # М-Видео
    {"activity_id": 2, "organisation_id": UUID("6946a71a-fd60-4d40-afc4-994961bef646")},  # electronic
    {"activity_id": 4, "organisation_id": UUID("6946a71a-fd60-4d40-afc4-994961bef646")},  # accessory
]
