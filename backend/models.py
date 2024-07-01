from datetime import datetime
from app import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    text_content = db.Column(db.Text)
    sentiment = db.Column(db.String(50))
    confidence_scores = db.Column(db.JSON)