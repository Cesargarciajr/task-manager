from taskmanager import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    # Relationship with categories
    categories = db.relationship('Category', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.user_id}', '{self.user_name}')"

# Define the Category model with unique color
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    category_color = db.Column(db.String(7), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('category_name', 'user_id', name='unique_category_per_user'),
        db.UniqueConstraint('category_color', 'user_id', name='unique_color_per_user')
    )

    def __repr__(self):
        return f"Category('{self.category_id}', '{self.category_name}', '{self.category_color}')"

# Define allowed timeframes for goals
ALLOWED_TIMEFRAMES = ['year', 'semester', 'trimester', 'month']

# Define the Goal model
class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    goal_name = db.Column(db.String(100), nullable=False)
    goal_description = db.Column(db.String(255), nullable=False)
    goal_important = db.Column(db.Boolean, default=False)
    goal_done = db.Column(db.Boolean, default=False)
    goal_timeframe_selection = db.Column(db.String(50), nullable=False)  # Use a regular string column
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)

    def __repr__(self):
        return f"Goal('{self.goal_id}', '{self.goal_name}', '{self.goal_description}', '{self.goal_important}', '{self.goal_done}', '{self.goal_timeframe_selection}')"
