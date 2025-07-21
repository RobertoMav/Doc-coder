# Doc coder

The goal of this repo is to use LLMs not to code, but to help you speed up reaching solutions to Coding problems. That should be done using LLMs to:

1. understand the issue you are having - this is mainly prompting, so that's on the user I guess
2. narrowing it down to a problem - this can be seen as either an architectural (high-level) as well as very specific (coding hands-on), it also extends to easy problems such as one-liners as well as long coding sequences (though I do not encourage such adventure)
3. given the issue and problem the model should look (~zero-shot style) for possible solutions - for instance "I have a Python issue with my FastAPI code, it currently cannot run x function, here is my @file and here is the {{error}}". In this case the model will read the file, see the error and we would use the models broad capability to suggest solutions given the problem. This should only showcase the possible alternatives we could use to solve the issue, either high-level approaches and some more specific - in this case we are mostly using LLMs instrinsic knowledge to suggest solutions (be mindful of hallucinations).
4. given the solutions (so far we have a main issue (item 1), an specific problem (item 2) and a list with possible solutions and a text description why (item 3) - short and simple) the model will search the web for the given solutions documentation, for instance the issue with the code mentioned in item 3 was a Pydantic issue, the model will grab the documentation of pydantic, more specificly the page you are having issues, as well as other issues that happened before (github issues, stack overflow) and then it will return the link to such docs, an explanation and finally it will copy the code in the documentation page.

Therefore the goal of this task is to reduce the possibility of hallucinations - where one would check the docs directly to see if the model is actually following the correct info.


Todos:
1. Ty + Dataclass vs pydantic vs typedDict vs pydantic settings vs Annotated
2. make
3. github pages
4. dependabot
5. MetaFlow

Services:
1. Kafka
2. Kubernetes
3. Casual Inf


Main:
1. Graduate
2. AWS Cert




ML Eng:
1. Maintain/Update/Improve. What is the ideal - this should also be set with the developing services team:
    - Automatic testing services
    - Automatic Linter and checking
    - Observability - use of mlflow! DataDog?
    - Support to async AWS Lambda functions - use of step functions?
    - Ease to create new models and deploy them - DS works on model arch and we deploy
2. Adopt new services - incorporation phase
    - This is to incorporate new products in our umbrella.
    - Here we have issues to adapt new products  - refactor projects
3. Developing services
We need to be able to deploy solutions to our DS so we could have a dedicated team to test new features (me hehehe).
The team would be responsible to exposing new functionalities/capabilities to DS team, such as:
        - Observability - DataDog
        - MCP clients/servers on AWS Lambdas
        - A2A protocol
        - Agentic Memory
        - Training workflows
        - Post Training workflows
        - DSPy servers
        - ACP ?
        - MetaFlow usage
4. Some Ideas:
    - Automatic ticket creation
    - PR eval via LLM