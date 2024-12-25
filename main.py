app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Існуючі класи моделей

admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
admin.add_view(ModelView(Customer, db.session))
# Додайте інші таблиці до панелі адміністратора
admin.add_view(ModelView(InsurancePolicies, db.session))
admin.add_view(ModelView(Agents, db.session))
admin.add_view(ModelView(Sales, db.session))

if __name__ == '__main__':
   app.run(debug=True)
