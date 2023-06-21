import os
import openai

problem = input("Please enter Problem Statement")
solution = input("Please enter Solution Description")

openai.api_key = "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"


def set_struct(sentence):
    j = 0
    rubric = [0, 0, 0, 0, 0, 0]
    for i in range(len(sentence)):
        if sentence[i] == ":":
            rubric[j] = int(sentence[i + 2])
            j += 1


            if j >= 6:
                print(rubric)
                return sentence

    print(rubric)
    return sentence


# openai.Completion.create(model="ada", prompt=query)
def ai_test(problem, solution):
    response1 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system",
         "content": "Evaluate the following capstone project proposal based on the following rubric"
                    "Grade the proposal on each of the points in the rubric from 0-10."
                                      "Rubric: novelty, relevance, feasibility, impact, sustainability, use of technology"
                                      "Also give overall comments"},
        {"role": "user", "content": problem}])
    print(response1)

    f = open("C:/Users/admin/PycharmProjects/CapstoneGuide2/App/tests/ai_ds.jsonl", "a")
    f.write('{"prompt": "' + problem + '", "completion": "' + str(response1.choices[0].message.content).replace("\n",
                                                                                                                "") + '"}\n')
    f.close()

    print(set_struct(str(response1.choices[0].message.content).replace("\n", "")))

    response2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "Evaluate the following capstone project proposal based on the following"
                                      "Rubric: novelty, relevance, feasibility, impact, sustainability, use of technology"
                                      "Also give overall comments"
                                      "In summary grade the proposal on each of the points in the rubric from 0-10."
                                      "Evaluate both the following problem: " + problem + " and the solution proposed."
                                                                                          "Phrase response only based on solution."},
        {"role": "user", "content": "Solution: " + solution}])
    print(response2)

    f = open("C:/Users/admin/PycharmProjects/CapstoneGuide2/App/tests/ai_ds.jsonl", "a")
    f.write('{"prompt": "' + problem + '", "completion": "' + str(response2.choices[0].message.content).replace("\n",
                                                                                                                "") + '"}\n')
    f.close()
    print(set_struct(str(response2.choices[0].message.content).replace("\n", "")))


ai_test(problem, solution)
