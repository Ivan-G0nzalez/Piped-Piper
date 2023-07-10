from app.models.exts import db


"""
class Components:
    id = primary key
    title: str
"""

class Components(db.Model):
    __tablename__="components"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    device = db.relationship('Device', backref='components', uselist=False)

    def __repr__(self):
        return f'<components {self.name}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()       

    def update(self, name):
        self.name = name

        db.session.commit()



"""
class Device:  
    id:Integer primary key
    client_count: Integer
    cpu_utilization: Integer
    firmaware_version: Varchar(15)
    labels: Text
    macaddr: Text
    mem_free: Integer
    mem_total: Integer
    model: Text
    name: Varchar(25) Not Null unique
    serial: Text
    stack_id: Integer
    status: Text default Up
    temperature: Text
    uptime: Integer
    uplink_ports: Text
    components_id: Integer FOREING key
"""

class Device(db.Model):
    __tablename__='device'
    id= db.Column(db.Integer, primary_key=True)
    client_count = db.Column(db.Integer)
    cpu_utiization = db.Column(db.Float)
    firmware_version = db.Column(db.String(15))
    labels = db.Column(db.Text)
    macaddr = db.Column(db.String(15))
    mem_free = db.Column(db.Integer)
    mem_total = db.Column(db.Integer)
    model = db.Column(db.String(15))
    name = db.Column(db.String(25), unique=True, nullable=False)
    serial = db.Column(db.String, unique=True)
    stack_id = db.Column(db.Integer)
    status = db.Column(db.String(15), default="Up")
    temperature = db.Column(db.Integer)
    uptime = db.Column(db.Integer)
    uplink_ports = db.Column(db.String(15))
    threshold = db.Column(db.Integer)
    components_id = db.Column(db.Integer, db.ForeignKey('components.id'))

    def __repr__(self):
        return f'<devices {self.name}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()       

    def update(self, client_count, cpu_utiization, firmware_version, labels,macaddr,mem_free,model,stack_id, status,temperature,uptime,uplink_ports):
        self.client_count = client_count
        self.cpu_utiization = cpu_utiization
        self.firmware_version = firmware_version
        self.labels = labels
        self.macaddr = macaddr
        self.mem_free = mem_free
        self.model = model
        self.stack_id = stack_id
        self.status = status
        self.temperature = temperature
        self.uptime = uptime
        self.uplink_ports = uplink_ports
        

        db.session.commit()