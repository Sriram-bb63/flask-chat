from python

workdir app

copy . ./

run pip install -r requirements.txt

expose 5000

cmd ["python", "chat.py"]