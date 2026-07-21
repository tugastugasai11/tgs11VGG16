from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Pastikan folder upload ada
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load model yang sudah dilatih
model = load_model('model_sepatu_vgg16.h5')
classes = ['Adidas', 'Converse', 'Nike']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Cek apakah ada file yang dikirim
        if 'file' not in request.files:
            return render_template('index.html', error='Tidak ada file yang diunggah.')
        
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='Pilih gambar terlebih dahulu.')

        if file:
            # Simpan gambar
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Proses gambar untuk prediksi (harus 224x224 pixel untuk VGG16)
            img = image.load_img(filepath, target_size=(224, 224))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Lakukan Prediksi
            prediction = model.predict(img_array)
            predicted_class = classes[np.argmax(prediction)]
            confidence = np.max(prediction) * 100

            return render_template('index.html', 
                                   prediction=predicted_class, 
                                   confidence=confidence, 
                                   image_path=filepath)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)