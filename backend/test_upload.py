import requests

file_path = r"C:\Users\disha\Downloads\RESUME_DISHA_BHANARKAR.pdf"

with open(file_path, "rb") as file:

    response = requests.post(
        "http://127.0.0.1:5000/upload-resume",
        files={"resume": file}
    )

print(response.status_code)
print(response.json())
