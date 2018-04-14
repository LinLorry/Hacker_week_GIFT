from project import db

class Class_first(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name = db.Column(db.String(16),index=True,nullable=False)
    s_id = db.relationship('Class_second',backref = 'class_first', lazy=True)

class Class_second(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16),nullable=False)
    f_id = db.Column(db.Integer,db.ForeignKey('class_first.id'),nullable=False)
    p_id = db.relationship('Gift',backref = 'class_second', lazy=True)


    standard = db.Column(db.Text)

    top_preface = db.Column(db.String(256))
    top_title = db.Column(db.String(64))

    medium_preface = db.Column(db.String(256))
    medium_title = db.Column(db.String(64))

    low_preface = db.Column(db.String(256))
    low_title = db.Column(db.String(64))