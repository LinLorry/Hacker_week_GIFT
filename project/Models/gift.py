from project import db

class Gift(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False)

    name = db.Column(db.String(64),index=True,nullable=False)
    #level in 1,2,3,4,5,6,7,8,9
    level = db.Column(db.Integer,nullable=False)

    H_price = db.Column(db.FLOAT,nullable=False)
    L_price = db.Column(db.FLOAT,nullable=False)

    title = db.Column(db.String(64))
    commentaries = db.Column(db.Text)

    s_id = db.Column(db.Integer,db.ForeignKey('class_second.id'),nullable=False)