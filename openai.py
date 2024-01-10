import os
import openai

open_api_key = "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"  #from https://beta.openai.com/account/api-keys

openai.organization = "Self"
openai.api_key = os.getenv(open_api_key)
openai.Model.list()


curl https://api.openai.com/v1/completions -H "Content-Type: application/json" \ -H "Authorization: Bearer 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" \ -d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'