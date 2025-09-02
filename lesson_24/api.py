# ===============================
# 📦 Імпорти
# ===============================
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace


#http://localhost:5000/swagger


# ===============================
# 🚀 Ініціалізація Flask + Swagger з авторизацією
# ===============================
app = Flask(__name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    version='1.0',
    title='Hillel API',
    description='📘 CRUD + Авторизація через Swagger',
    doc='/swagger',
    authorizations=authorizations,
    security='apikey'  # автоматично додає токен до захищених маршрутів
)

# ===============================
# 🧠 Імітація БД
# ===============================
users = {}
items = {}
auth_token = "secret-token"  # Тестовий токен

# ===============================
# 🧱 Моделі Swagger
# ===============================
user_model = api.model('User', {
    'username': fields.String(required=True),
    'password': fields.String(required=True),
})

item_model = api.model('Item', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'description': fields.String(required=False),
})

# ===============================
# 🔐 Авторизація
# ===============================
auth_ns = Namespace('auth', description='Авторизація')

@auth_ns.route('/signup')
class Signup(Resource):
    @auth_ns.expect(user_model)
    def post(self):
        """✅ Реєстрація нового користувача"""
        data = request.json
        if data['username'] in users:
            return {'message': 'Користувач вже існує'}, 400
        users[data['username']] = data['password']
        return {'message': 'Реєстрація успішна'}

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(user_model)
    def post(self):
        """🔐 Вхід користувача"""
        data = request.json
        if users.get(data['username']) != data['password']:
            return {'message': 'Невірний логін або пароль'}, 401
        return {'token': auth_token}

# ===============================
# 📁 CRUD операції
# ===============================
crud_ns = Namespace('items', description='📦 CRUD Операції з елементами')

@crud_ns.route('/')
class ItemList(Resource):
    @crud_ns.doc(security='apikey')
    def get(self):
        """📥 Отримати всі елементи (авторизовано)"""
        if request.headers.get("Authorization") != f"Bearer {auth_token}":
            return {'message': 'Unauthorized'}, 401
        return list(items.values())

    @crud_ns.expect(item_model)
    def post(self):
        """➕ Створити елемент"""
        data = request.json
        if data['id'] in items:
            return {'message': 'Елемент з таким ID вже існує'}, 400
        items[data['id']] = data
        return data, 201

@crud_ns.route('/<int:item_id>')
class Item(Resource):
    def get(self, item_id):
        """📄 Отримати елемент за ID"""
        item = items.get(item_id)
        return item if item else {'message': 'Не знайдено'}, 404

    @crud_ns.expect(item_model)
    def put(self, item_id):
        """✏️ Оновити елемент"""
        if item_id not in items:
            return {'message': 'Не знайдено'}, 404
        items[item_id] = request.json
        return items[item_id]

    def delete(self, item_id):
        """❌ Видалити елемент"""
        if item_id not in items:
            return {'message': 'Не знайдено'}, 404
        del items[item_id]
        return {'message': 'Видалено'}

# ===============================
# ✅ Реєстрація namespace'ів
# ===============================
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(crud_ns, path='/items')

# ===============================
# ▶️ Точка входу
# ===============================
if __name__ == '__main__':
    app.run(debug=True)
