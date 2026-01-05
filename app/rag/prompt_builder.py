def build_prompt(
    system_prompt: str,
    conversation_summary: str | None,
    context: str,
    question: str
) -> str:
    prompt = system_prompt + "\n\n"

    if conversation_summary:
        prompt += f"Conversation so far:\n{conversation_summary}\n\n"

    if context:
        prompt += f"Context:\n{context}\n\n"

    prompt += f"User question:\n{question}"

    return prompt
