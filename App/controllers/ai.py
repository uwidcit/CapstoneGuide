import openai

openai.api_key = "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"

def ai_test(query):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}])
   # print(response)

    f = open("App/tests/ai_ds.jsonl", "a")
    f.write("file opened") #'{"prompt": "' + query + '", "completion": "' + str(response.choices[0].message.content) + '"}')
    f.close()
    return (str(response.choices[0].message.content))