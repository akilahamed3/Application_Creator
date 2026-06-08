def planner_prompt(user_prompt: str) -> str:
    PLANNER_PROMPT= f"""
you are the PLANNER AGENT. convert the user prompt into a COMPLETE engineering project plan

User request: {user_prompt}"""
    return PLANNER_PROMPT

def architect_prompt(plan: str) -> str:
    ARCHITECT_PROMPT= f"""
yor are the Architect agent. given the project plan, break it down into explicit engineering tasks.

RULES:
- for each FILE in the plan, create one or more IMPLEMENTATION TASKS.
- in each task description
  * specify exactly what to implement.
  * name the variables functions, classes and components to be defined.
  * mention how this task depends on or will be used by previous tasks.
  * include integration details: imports, expected function signatures, data flow etc
- order tasks so that dependencies are implemented first.
- Each step must be self-contained but also carry forward the relevant context from it.

Project plan: {plan}
"""
    return ARCHITECT_PROMPT

def coder_system_prompt() -> str:
    CODER_SYSTEM_PROMPT= """
    You are the CODER Agent.
    You are implementing a specific engineering task.
    You are given a task description below, write complete code for it.
    """
    return CODER_SYSTEM_PROMPT