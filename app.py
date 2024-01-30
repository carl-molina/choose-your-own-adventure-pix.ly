import os
from dotenv import load_dotenv
import requests

import boto3
# s3 = boto3.resource('s3')

AWS_ACCESS_KEY = os.environ['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = os.environ['aws_secret_access_key']

from flask import Flask, request, render_template, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES

# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage

from flask_debugtoolbar import DebugToolbarExtension
# from sqlalchemy.exc import IntegrityError <-- db, not needed right now

# import exifread <-- how to read exif data from photo file

app = Flask(__name__)

# app.config['S3_BUCKET'] = 'S3_BUCKET_NAME'
# app.config['S3_KEY'] = 'AWS_ACCESS_KEY'
# app.config['S3_SECRET'] = 'AWS_ACCESS_SECRET'
# app.config['S3_LOCATION'] = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

photos = UploadSet("photos", IMAGES)


app.config["UPLOADED_PHOTOS_DEST"] = "static/img"
configure_uploads(app, photos)


# attempt at configuring S3 connection, "manage via python" from lecture
s3 = boto3.client(
    's3',
    'us-west-1',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


@app.route('/', methods=['GET'])
def homepage():
    """Show homepage"""

    return render_template('base.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # checks for file type
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        # if passes all checks, uploads file to S3 bucket
        s3.upload_fileobj(file, 'name-of-bucket', file.filename)

        flash("File uploaded successfully")

    flash("Method not allowed. Failed to upload file.")