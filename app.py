# Main API file 
import os
from werkzeug.utils import secure_filename
from flask import Flask,jsonify,request
from recommender import run_recommender
from functions_only_save import make_face_df_save
# Main Upload folder
UPLOAD_FOLDER = r'D:\PROJECTS\UPLOADS'

# Flask app
app = Flask(__name__)

#app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Allowed file extensions
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# Allowed file extensions checked
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Health Check end point 
# http://127.0.0.1/ - ENDPOINT URI 
@app.route("/",methods=['GET'])
def home():
    if(request.method=='GET'):
        data = "API is working fine"
        version = "V.1.0"
        return jsonify(
            {
                'version':version,
                'data': data,
                'app': "Hair Style Reccomendation System APP"
            }
        )

# File upload method
@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # decoded_image= base64.b64decode(file)        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify(
            {
                'message' : 'File successfully uploaded',
            }
        )
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp

# Predict the face value
@app.route("/predict",methods=["POST"])
def predict():
    if request.method == "POST":
        # file_path = request.get_json()['user_photo']  
        filename = request.get_json()['filename']
        uname = request.get_json()['uname']
        gender = request.get_json()['gender']

        folder = r'D:\PROJECTS\UPLOADS'

        file_path = os.path.join(folder, filename)
        try:    
            res = run_recommender(uname,gender,file_path)
        except Exception as e:
            resp = jsonify({
                      'message': str(e),
                      'status_code': 501
                }) 
            return resp

        # resp = jsonify(
        #         {
        #             'message': "Prediction success !!",
        #             'resp' : res,
        #             'uname': uname,
        #             'gender': gender,
        #             'status_code': 200
        #         }
        #     )   
        resp = jsonify({
            'resp': res
        })
        return resp
    else:
        resp = jsonify(
            {
                'message' : 'Failed to predict',
                'uname': uname,
                'gender': gender,
                'status_code': 400
            }
        )   
        return resp          

if __name__ == 'main':
    app.run(debug=True)
    