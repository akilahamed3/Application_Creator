def planner_prompt(user_prompt: str) -> str:
    PLANNER_PROMPT= f"""
you are the PLANNER AGENT. convert the user prompt into a COMPLETE engineering project plan

User request: {user_prompt}"""
    return PLANNER_PROMPT