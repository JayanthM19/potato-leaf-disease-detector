# 🍃 Potato Leaf Disease Detection  

## 📌 Project Overview  
This project utilizes **deep learning** to classify potato leaf diseases, specifically **Early Blight, Late Blight, and Healthy leaves**. The model is trained using **TensorFlow/Keras** and deployed with a simple **Flask/Tkinter-based UI**.

---

## 📂 Directory Structure  
<pre>
  📦 Potato-Leaf-Disease-Detection
  │-- dataset/ # Contains training, validation, and test datasets
  │ ├── Train/ # Training dataset
  │ ├── Valid/ # Validation dataset
  │ ├── Test/ # Testing dataset
  │-- myenv/ # Virtual environment (ignored in Git)
  │-- app.py # Flask/Tkinter-based GUI for prediction
  │-- train_model.py # Model training script
  │-- model.h5 # Trained deep learning model
  │-- .gitignore # Git ignore file
  │-- README.md # Project documentation
</pre>

---

## 🚀 Features  

✅ **Deep Learning Model** – Uses CNN-based classification for potato leaf diseases  
✅ **Real-Time Prediction** – Load and analyze images using a user-friendly interface  
✅ **Color-Coded Feedback** – Displays results with a simple color-based UI  
✅ **Dataset Management** – Uses structured directories for training and validation  
✅ **Lightweight Deployment** – Flask/Tkinter ensures easy execution on standard hardware  

---

## 📦 Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/Potato-Leaf-Disease-Detection.git
cd Potato-Leaf-Disease-Detection
```

2️⃣ Set Up Virtual Environment
python -m venv myenv
source myenv/bin/activate   # For Mac/Linux
myenv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

🏋️‍♂️ Training the Model
To train the deep learning model, run:
```bash
python train_model.py
```
The trained model will be saved as model.h5.


🎯 Running the Prediction App
To start the application:
```bash
python app.py
```
Upload a leaf image, and the model will classify it as Healthy, Early Blight, or Late Blight.

🤝 Contributing
Fork the Repository
Create a Feature Branch (git checkout -b feature-name)
Commit Changes (git commit -m "Added feature XYZ")
Push to Branch (git push origin feature-name)
Open a Pull Request
📜 License
This project is open-source and available under the MIT License.

✉️ Contact
For any issues or suggestions, feel free to reach out:

📧 Email: jayanthmulakalaplli@gmail.com
🐙 GitHub: JayanthM19
