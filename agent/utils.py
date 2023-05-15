from langchain.callbacks import get_openai_callback

def ask_agent(agent, question):
    with get_openai_callback() as cb:
        response = agent.run(question)
        print(f"Answer: {response}\n")
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Successful Requests: {cb.successful_requests}")
        print(f"Total Cost (USD): ${cb.total_cost}")
    return response