from openai import OpenAI
import requests
import json


# BASE_URL = "your_base_url"
# API_KEY = "your_api_key"
# client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

# model_names = client.models.list()
# for model in model_names:
#     print(model.id)
# client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

model_names = [
    "gpt-3.5-turbo",
    "gpt-4",
    "gpt-4-0613",
    "gpt-4-1106-preview",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-1106",
    "gpt-4-vision-preview",
]


# call for ollama localhost
def ollama_call(prompt):
    # print("calling ollama")
    # print(prompt)
    body = {
        "model": "seeker-model",
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(
        "http://localhost:11434/api/generate", data=json.dumps(body)
    )
    return json.loads(response.text)["response"]


def gpt_call(model_name, prompt):
    return ollama_call(prompt)
    # response = client.chat.completions.create(
    #     model=model_name, messages=[{"role": "user", "content": prompt}]
    # )
    # return response.choices[0].message.content


if __name__ == "__main__":
    # print(gpt_call(model_names[0], "Please introduce yourself in twenty words."))
    print(gpt_call(model_names[0], """You are a software engineer specializing in exception handling. Your
task is to optimize the given code unit by applying appropriate exception
handling strategies.

public void marshal(org.w3c.dom.Node node, Object namespacePrefixMapper) throws JAXBException {
  Marshaller marshaller = jc.createMarshaller();
  NamespacePrefixMapperUtils.setProperty(marshaller, namespacePrefixMapper);
  getContents();
  setMceIgnorable((McIgnorableNamespaceDeclarator) namespacePrefixMapper);
  marshaller.marshal(jaxbElement, node);
  ((McIgnorableNamespaceDeclarator) namespacePrefixMapper).setMcIgnorable(null);
}

Ensure that the code is syntactically correct and adheres to best practices
in exception handling."""))
