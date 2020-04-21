import requests

while True:
    question = input("Quesion:")
    
    if question == "exit":
        break
    else:
        post_data = {"question":question}
        res = requests.post(url="http://127.0.0.1:5000/question",data=post_data)
        print(res.text)