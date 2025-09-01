import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
AUTH_URL = f"{BASE_URL}/auth"
ITEMS_URL = f"{BASE_URL}/items"
AUTH_TOKEN = "secret-token"


# ======= Сесійна фікстура для HEADERS =======
@pytest.fixture(scope="session")
def auth_headers():
    return {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }


# ======= AUTH =======
@pytest.fixture
# Cтворюємо прекондішни для перевірки дубліката юзера
def prepare_duplicate_user():
    username = "admin"
    password = "pass123"
    requests.post(f"{AUTH_URL}/signup", json={"username": username, "password": password})
    yield username, password

# Реєстрація кількох нових користувачів
@pytest.mark.parametrize(
    "username,password",
    [
        ("user1", "Pass1"),
        ("User2", "Pass2"),
        ("Test User3", "Pass3")
    ]
)
# Реєстрація успішна
def test_signup_success(username, password):
    response = requests.post(f"{AUTH_URL}/signup", json={"username": username, "password": password})
    assert response.status_code == 200
    assert "Реєстрація успішна" in response.json()["message"]

# Реєстрація з існуючим юзером
def test_signup_duplicate(prepare_duplicate_user):
    username, password = prepare_duplicate_user
    response = requests.post(f"{AUTH_URL}/signup", json={"username": username, "password": password})
    assert response.status_code == 400
    assert "Користувач вже існує" in response.json()["message"]

# Без заповнення обов'язкових полів
@pytest.mark.parametrize(
    "payload",
    [
        {"username": "user_no_pass"},          # без пароля
        {"password": "pass_no_user"},          # без юзернейму
        {}                                     # взагалі пусто
    ]
)
def test_signup_missing_required_fields(payload):
    response = requests.post(f"{AUTH_URL}/signup", json=payload)
    assert response.status_code == 500

# Логін з очікувано неправильним паролем
@pytest.mark.xfail(reason="Очікувано неправильний пароль")
def test_login_fail():
    requests.post(f"{AUTH_URL}/signup", json={"username": "tester2", "password": "123"})
    response = requests.post(f"{AUTH_URL}/login", json={"username": "tester2", "password": "wrong"})
    assert response.status_code == 401


# ======= ITEMS =======
# Успішне створення items з тільки обов'язковими полями (без дескріпшна), та всіма полями
@pytest.mark.parametrize("item_data", [
    {"id": 1001, "name": "FullItem", "description": "test desc", "price": 10.5},
    {"id": 1002, "name": "MinimalItem"},  # тільки обов’язкові поля
])

def test_create_item(item_data, auth_headers):
    response = requests.post(f"{ITEMS_URL}/", json=item_data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["name"] == item_data["name"]

# Створюємо окремий айтем
@pytest.fixture
def prepared_item(auth_headers):
    item = {"id": 1003, "name": "FullItem", "description": "test desc", "price": 10.5}
    response = requests.post(f"{ITEMS_URL}/", json=item, headers=auth_headers)
    assert response.status_code == 201
    yield item  # передаємо айтем у тест
    requests.delete(f"{ITEMS_URL}/{item['id']}", headers=auth_headers) # Після тесту на всяк випадок видаляємо

# Використовуємо фікстуру для оновлення айтема
@pytest.mark.usefixtures("prepared_item")
def test_update_prepared_item(prepared_item, auth_headers):
    item_id = prepared_item["id"]
    updated_data = {"id": item_id, "name": "UpdatedItem"}
    response = requests.put(f"{ITEMS_URL}/{item_id}", json=updated_data, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["name"] == "UpdatedItem"

# Використовуємо фікстуру для видалення айтема
@pytest.mark.usefixtures("prepared_item")
def test_delete_prepared_item(prepared_item, auth_headers):
    item_id = prepared_item["id"]
    # Спочатку оновимо, щоб точно бути впевненими, що айтем існує
    requests.put(f"{ITEMS_URL}/{item_id}", json={"id": item_id, "name": "TempName"}, headers=auth_headers)

    response = requests.delete(f"{ITEMS_URL}/{item_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Видалено"

# Знаходження, оновлення та видалення айтема, ID якого не існує
@pytest.fixture
def fake_item_id():
    return 99999  # ID, якого точно не існує

def test_get_nonexistent_item(fake_item_id, auth_headers):
    response = requests.get(f"{ITEMS_URL}/{fake_item_id}", headers=auth_headers)
    assert response.status_code == 404


def test_update_nonexistent_item(fake_item_id, auth_headers):
    response = requests.put(f"{ITEMS_URL}/{fake_item_id}", json={"name": "Updated"}, headers=auth_headers)
    assert response.status_code == 404


def test_delete_nonexistent_item(fake_item_id, auth_headers):
    response = requests.delete(f"{ITEMS_URL}/{fake_item_id}", headers=auth_headers)
    assert response.status_code == 404