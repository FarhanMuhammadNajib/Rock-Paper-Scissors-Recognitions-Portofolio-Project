from flask import Flask, render_template, request
from predict import prediksi
from PIL import Image
import os
import base64
import io

app= Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}
def allowed_file_extensions(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        predictfile=request.files['predictFile']
        if predictfile == None or  predictfile.filename == "":
            with open("./static/PredictFile/ErrorImage/NoFile.png", "rb") as image_file:
            # Encode the image as Base64
                base64_image = base64.b64encode(image_file.read()).decode()      
            return  render_template("Predict.html", prediction = "No File Submited", img_path = base64_image)
        elif not allowed_file_extensions(predictfile.filename):
            with open("./static/PredictFile/ErrorImage/NotSupported.png", "rb") as image_file:
            # Encode the image as Base64
                base64_image = base64.b64encode(image_file.read()).decode() 
            return  render_template("Predict.html", prediction = "File Not Supported", img_path = base64_image  )
        
        filePath="./static/PredictFile/" + predictfile.filename
        predictfile.save(filePath)
        with Image.open(filePath) as img:
            # Convert the image to JPEG
            fill_color = (255,255,225)
            img = img.convert("RGBA")
            if img.mode in ('RGBA', 'LA'):
                background = Image.new(img.mode[:-1], img.size, fill_color)
                background.paste(img, img.split()[-1]) # omit transparency
                img = background
            img.convert("RGB").save(filePath, "JPEG", )

            
        prediction=prediksi(filePath)
        
        im = Image.open(filePath)
        data = io.BytesIO()
        im.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())
        
        if os.path.exists(filePath):  
            os.remove(filePath)
        
        return render_template("Predict.html", prediction = prediction, img_path = encoded_img_data.decode('utf-8'))
    
if __name__ == "__main__":
    app.run(port=1000)