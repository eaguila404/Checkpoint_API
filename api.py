from flask import Flask,request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# initialize Flask API
app = Flask(__name__)

# Debug mode (auto-updates code)
app.config["DEBUG"] = True

# basedir
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize Database
db = SQLAlchemy(app)

# Init marshmallow
ma = Marshmallow(app)

#                        #
# CHECKPOINT Class/Model #
#                        #
class Checkpoint(db.Model):
    guid_ = db.Column(db.String, primary_key=True)
    longitude_ = db.Column(db.Float, nullable = False)
    latitude_ = db.Column(db.Float, nullable = False)

    def __init__(self,guid,longitude,latitude):
        self.guid_ = guid
        self.longitude_ = longitude
        self.latitude_ = latitude

# CHECKPOINT Schema
class CheckpointSchema(ma.Schema):
    class Meta:
        fields = ('guid_', 'longitude_', 'latitude_')


#                                  #
#  ExposedCheckpoints class/model  #
#                                  #
class ExposedCheckpoints(db.Model):
    id_ = db.Column(db.Integer,primary_key = True, autoincrement=True)
    guid_ = db.Column(db.String,db.ForeignKey(Checkpoint.guid_))
    epoch_ = db.Column(db.Integer,nullable = False)
    '''
    def __init__(self,id,guid,epoch):
        self.id_ = id
        self.guid_ = guid
        self.epoch_ = epoch
    '''

    def __init__(self,guid,epoch):
        #self.id_ = id
        self.guid_ = guid
        self.epoch_ = epoch


# ExposedCheckpoints schema
class ExposedCheckpointSchema(ma.Schema):
    class Meta:
        fields = ('id_','guid_','epoch_')


# initialize CHECKPOINT schema
Checkpoint_schema = CheckpointSchema()
Checkpoints_schema = CheckpointSchema(many=True)

# initialize Exposed CHECKPOINT schema
ExposedCheckpoint_schema = ExposedCheckpointSchema()
ExposedCheckpoints_schema = ExposedCheckpointSchema(many=True)

#                        #
#  CHECKPOINT ENDPOINTS  #
#                        #

# Create/Register a CHECKPOINT
# input json format
@app.route('/register', methods=['POST'])
def add_checkpoint():


    guid = request.json['guid']
    longitude = request.json['longitude']
    latitude = request.json['latitude']

    new_checkpoint = Checkpoint(guid,longitude,latitude)
    print(new_checkpoint)
    db.session.add(new_checkpoint)
    db.session.commit()


    return Checkpoint_schema.jsonify(new_checkpoint)

# Get All CHECKPOINTs
# return in json fromat
@app.route('/checkpoints', methods=['GET'])
def get_checkpoints():
    all_checkpoints = Checkpoint.query.all()
    result = Checkpoints_schema.dump(all_checkpoints)
    return jsonify(result)

# Get Single CHECKPOINT
# return in json fromat
@app.route('/checkpoint/<guid>', methods=['GET'])
def get_checkpoint(guid):
    checkpoint = Checkpoint.query.get(guid)
    print("printing:",checkpoint,Checkpoint_schema.jsonify(checkpoint))
    return Checkpoint_schema.jsonify(checkpoint)

# Update a CHECKPOINT
# input json format
@app.route('/checkpoint/update/<guid>', methods=['PUT'])
def update_checkpoint(guid):
    checkpoint = Checkpoint.query.get(guid)

    quid = request.json['guid']
    longitude = request.json['longitude']
    latitude = request.json['latitude']

    checkpoint.quid_ = quid
    checkpoint.longitude_ = longitude
    checkpoint.latitude_ = latitude

    db.session.commit()

    return Checkpoint_schema.jsonify(checkpoint)

# Delete CHECKPOINT
@app.route('/checkpoint/delete/<guid>', methods=['DELETE'])
def delete_checkpoint(guid):
    checkpoint = Checkpoint.query.get(guid)
    db.session.delete(checkpoint)
    db.session.commit()

    return Checkpoint_schema.jsonify(checkpoint)



#                                #
#  EXPOSED CHECKPOINT ENDPOINTS  #
#                                #
# initialize schema
ExposedCheckpoint_schema = ExposedCheckpointSchema()
ExposedCheckpoints_schema = ExposedCheckpointSchema(many=True)

# Create/add/report an Exposed CHECKPOINT
# input json format
@app.route('/report', methods=['POST'])
def add_exposed_checkpoint():
    guid = request.json['guid']
    epoch = request.json['epoch']

    new_exposed_checkpoint = ExposedCheckpoints(guid,epoch)

    db.session.add(new_exposed_checkpoint)
    db.session.commit()

    return ExposedCheckpoint_schema.jsonify(new_exposed_checkpoint)

# Get All exposed CHECKPOINTs
# return in json fromat
@app.route('/exposedcheckpoints', methods=['GET'])
def get_exposed_checkpoints():
    all_exposed_checkpoints = ExposedCheckpoints.query.all()
    result = ExposedCheckpoints_schema.dump(all_exposed_checkpoints)
    return jsonify(result)

# Get a Single exposed CHECKPOINT (all instances)
# return in json fromat
@app.route('/exposedcheckpoint/<guid>', methods=['GET'])
def get_exposed_checkpoint(guid):
    #guid_exposed_checkpoint = ExposedCheckpoints.query.filter(ExposedCheckpoints.guid_ == "CAd63B87-DA1E-488B-BD8B-C5E04FE06EC2").all()
    #guid_exposed_checkpoint = ExposedCheckpoints.query.filter_by(guid_ = guid)
    #result = ExposedCheckpoint_schema.dump(guid_exposed_checkpoint)
    all_exposed_checkpoints = ExposedCheckpoints.query.all()
    guid_exposed_checkpoint = [{'id':checkpoint.id_, 'guid':guid,'epoch':checkpoint.epoch_} for checkpoint in all_exposed_checkpoints]
    #print(result)
    return jsonify(guid_exposed_checkpoint)


# Delete Exposed CHECKPOINT record/instance
@app.route('/exposedcheckpoint/delete/<id>', methods=['DELETE'])
def delete_exposed_checkpoint(id):
    exposed_checkpoint = ExposedCheckpoints.query.get(id)
    db.session.delete(exposed_checkpoint)
    db.session.commit()

    return Checkpoint_schema.jsonify(exposed_checkpoint)

# Creates new db. Must delete previous first.
#db.create_all()
app.run()
