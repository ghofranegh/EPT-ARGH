from PIL import Image
from utils.api import predict

img = Image.open("path/to/any/test/image.png")
result = predict(img)
print("predicted_class:", result["predicted_class"])
print("confidence:", result["confidence"])
print("num ROIs:", len(result["regions_of_interest"]))