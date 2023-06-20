# import os
# import openai

# query = input("Please enter query")

# openai.api_key = "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"

# openai.Completion.create(model="cap-mod", prompt=query)

# response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}])
# print(response)

# f = open("App/tests/ai_ds.jsonl", "a")
# f.write('{"prompt": "' + query + '", "completion": "' + str(response.choices[0].message.content) + '"}')
# f.close()
