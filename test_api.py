from PIL import Image
from utils.api import predict

img = Image.open(r"E:\ept ragh\streamlit_app\001.bmp")
result = predict(img)
print("predicted_class:", result["predicted_class"])
print("confidence:", result["confidence"])
print("num ROIs:", len(result["regions_of_interest"]))