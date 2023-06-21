import openai

openai.api_key = "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"

def call_openai_api(*args, **kwargs):
    return openai.ChatCompletion.create(*args, **kwargs)
def ai_test(problem_desc):
    response1 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "Evaluate the following capstone project proposal based on the following"
                                      "Rubric: novelty, relevance, feasibility, impact, sustainability, use of technology"
                                      "Also give overall comments"
                                      "In summary grade the proposal on each of the points in the rubric out of 10"},
        {"role": "user", "content": "Problem Description: " + problem_desc},
    ])
    """response2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "Evaluate the following capstone project proposal based on the following"
                                      "Rubric: novelty, relevance, feasibility, impact, sustainability, use of technology"
                                      "Also give overall comments"
                                      "In summary grade the proposal on each of the points in the rubric out of 10"
                                      "Phrase response only to solution description"+problem_desc},
        {"role": "user", "content": "Solution Description: " +solution_desc},
    ])"""
    return (response1)

print(ai_test(input("Problem Description")))
print(ai_test(input("Solution Description")))
