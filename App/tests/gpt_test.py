import os
import openai

problem = input("Please enter Problem Statement")
solution = input("Please enter Solution Description")


openai.api_key = "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"

#openai.Completion.create(model="ada", prompt=query)
def ai_test(problem, solution):
    response1 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "Evaluate the following capstone project proposal based on the following"
                                      "Rubric: novelty, relevance, feasibility, impact, sustainability, use of technology"
                                      "Also give overall comments"
                                      "In summary grade the proposal on each of the points in the rubric out of 10"},
        {"role": "user", "content": problem}])
    print(response1)

    f = open("C:/Users/admin/PycharmProjects/CapstoneGuide2/App/tests/ai_ds.jsonl", "a")
    f.write('{"prompt": "' + problem + '", "completion": "' + str(response1.choices[0].message.content).replace("\n", "") + '"}\n')
    f.close()

    response2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "Evaluate the following capstone project proposal based on the following"
                                      "Rubric: novelty, relevance, feasibility, impact, sustainability, use of technology"
                                      "Also give overall comments"
                                      "In summary grade the proposal on each of the points in the rubric out of 10."
                                      "Evaluate both the following problem: " + problem + " and the solution proposed."
                                                                                         "Phrase response only based on solution."},
        {"role": "user", "content": "Solution: " + solution}])
    print(response2)

    f = open("C:/Users/admin/PycharmProjects/CapstoneGuide2/App/tests/ai_ds.jsonl", "a")
    f.write('{"prompt": "' + problem + '", "completion": "' + str(response2.choices[0].message.content).replace("\n", "") + '"}\n')
    f.close()

ai_test(problem, solution)
