# face_detect
INSTALL
install python < 3.7
pip install -r requirements.txt

START
uvicorn app:app --reload --port 8089 --host 0.0.0.0

POST: {"content":"IMGTEXT"}
WHERE: ip_or_host:8089/prediction/ 

IMGTEXT = base64 image data
