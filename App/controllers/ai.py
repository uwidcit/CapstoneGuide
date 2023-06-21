import os
import openai

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

#openai.Completion.create(model="ada", prompt=query)
def ai_test(proposal_nm, problem_desc, solution_desc, num_members, functionalities, technologies, goals, sustain, notes):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "Evaluate the following capstone project proposal based on the following"
                                      "Rubric: novelty, relevance, feasibility, impact, sustainability, use of technology"
                                      "Also give overall comments"
                                      "In summary grade the proposal on each of the points in the rubric 0-9"},
        {"role": "user", "content": "Proposal Name: " + proposal_nm + "\nProblem Description: " + problem_desc +
                                    "\nSolution Description: " + solution_desc + "\nNumber of Members: " + num_members
                                    + "\nRequirements: "+ functionalities + "\nTechnical Skills: "+ technologies +
                                    "\nGoals: "+ goals + "\nSustainability: "+ sustain + "\nAdditional Information: "+ notes}])
    print(response)

    f = open("C:/Users/admin/PycharmProjects/CapstoneGuide2/App/tests/ai_ds.jsonl", "a")
    f.write('{"prompt": "' + proposal_nm + '", "completion": "' + str(response.choices[0].message.content).replace("\n", "") + '"}\n')
    f.close()

    print(set_struct(str(response.choices[0].message.content).replace("\n", "")))
