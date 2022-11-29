from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return "Video(name = {name}, views = {views}, likes = {likes})"

# avoid rewrite the database
# db.create_all()

# setting the arguments that the request body must have to make a Video post
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("likes", type=int, help="Likes of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video is required")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

# creating class to handle CRUD operations
class Video(Resource):
	# handle get request
	@marshal_with(resource_fields) #serialize the request following resource_fields
	def get(self, video_id):
		# sqlalchemy returns an instance of the query so we need to serialize it
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Could not find video...")

		return result


	# handle put request
	@marshal_with(resource_fields)
	def put(self, video_id):
		print('\n'*10)
		print(VideoModel.__table__.columns)
		args = video_put_args.parse_args()
		# check if the video already exists
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message="Video ID already exists...")
		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		# adding video object to the db (temporary)
		db.session.add(video)
		# commit any temporary changes to the db
		db.session.commit()

		return video, 201

	@marshal_with(resource_fields)
	# handle update request
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video doesnt exists, cannot update")
		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']
		db.session.add(result)
		db.session.commit()
		
		return result


	# PENDING
	# handle delete request
	# def delete(self, video_id):
	# 	return {"message": "Video deleted"}

# adding the endpoints
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
	app.run(debug=True)