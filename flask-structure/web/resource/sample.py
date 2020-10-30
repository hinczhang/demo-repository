from flask_restful import Resource
from flask import Response,request
import json

#return useful information
class Sample(Resource):
	def get(self):#block get method
		pass
	def post(self):#open post method
		print(json.loads(request.data)['mode'])#the data delivered from frontend to backend are stored in the request.data, which should be jsonfied.
		data = json.dumps({'sample':'success!'})
		res = Response(response=data, status=200, mimetype="application/json")#send message to frontend
		return res
