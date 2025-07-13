# Doc coder

The goal of this repo is to use LLMs not to code, but to help you speed up reaching solutions to Coding problems. That should be done using LLMs to:

1. understand the issue you are having - this is mainly prompting, so that's on the user I guess
2. narrowing it down to a problem - this can be seen as either an architectural (high-level) as well as very specific (coding hands-on), it also extends to easy problems such as one-liners as well as long coding sequences (though I do not encourage such adventure)
3. given the issue and problem the model should look (~zero-shot style) for possible solutions - for instance "I have a Python issue with my FastAPI code, it currently cannot run x function, here is my @file and here is the {{error}}". In this case the model will read the file, see the error and we would use the models broad capability to suggest solutions given the problem. This should only showcase the possible alternatives we could use to solve the issue, either high-level approaches and some more specific - in this case we are mostly using LLMs instrinsic knowledge to suggest solutions (be mindful of hallucinations).

If we consider step 2 and 3 are not absolute gems there is nothing new so far, this leads us to:

4. given the solutions (so far we have a main issue (item 1), an specific problem (item 2) and a list with possible solutions and a text description why (item 3) - short and simple) the model will search the web for the given solutions documentation, for instance the issue with the code mentioned in item 3 was a Pydantic issue, the model will grab the documentation of pydantic, more specificly the page you are having issues, as well as other issues that happened before (github issues, stack overflow) and then it will return the link to such docs, an explanation and finally it will copy the code in the documentation page.

Therefore the goal of this task is to reduce the possibility of hallucinations - where one would check the docs directly to see if the model is actually following the correct info.
