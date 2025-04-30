import openai

openai.api_key = "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"

models = openai.models.list()

for model in models:
    print(model.id)
