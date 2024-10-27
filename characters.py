from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Define the path to the `asl_images` folder relative to this script's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASL_IMAGES_PATH = os.path.join(BASE_DIR, "asl_images")

@app.route("/get-asl-image", methods=["POST"])
def get_asl_image():
    data = request.json
    character = data.get("character", "").upper()

    if not character:
        return jsonify({"error": "No character provided"}), 400

    # Adjust filename to match the `_test` suffix convention
    filename = f"{character}_test.jpg" if character != " " else "space_test.jpg"
    image_path = os.path.join(ASL_IMAGES_PATH, filename)

    # Check if the file exists and serve it
    if os.path.isfile(image_path):
        return send_file(image_path, mimetype="image/jpeg")
    else:
        return jsonify({"error": f"Image for '{character}' not found"}), 404

if name == "main":
    app.run(host="0.0.0.0", port=5000, debug=True)
