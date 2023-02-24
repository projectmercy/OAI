import openai
openai.api_key = "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"

models = openai.Model.list()
for model in models['data']:
    print(model.id)