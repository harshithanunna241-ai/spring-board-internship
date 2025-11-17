import random

def generate_subquestions(main_question):
    """
    Decompose a research question into smaller sub-questions.
    In a real system, this would use an LLM; here it uses templates.
    """
    templates = [
        f"What are the key concepts in '{main_question}'?",
        f"Who are the main contributors or researchers related to '{main_question}'?",
        f"What are typical challenges in '{main_question}'?",
        f"What are the latest developments about '{main_question}'?",
        f"How can '{main_question}' be applied in practice?"
    ]
    return random.sample(templates, 3)

def search_answers(sub_questions):
    """
    Simulate answering sub-questions.
    In production, this would query search/LLM APIs.
    """
    static_answers = {
        "concepts": "The main concepts include decomposition, abstraction, and prompt engineering.",
        "contributors": "Key contributors are researchers from OpenAI and Google DeepMind.",
        "challenges": "Typical challenges include ambiguity in decomposition and maintaining answer accuracy.",
        "developments": "Recent advances involve agent-based architectures and improved contextual summarization.",
        "applications": "Such assistants are used in research, education, and enterprise search."
    }
    answers = []
    for q in sub_questions:
        if "key concepts" in q:
            answers.append(static_answers["concepts"])
        elif "contributors" in q:
            answers.append(static_answers["contributors"])
        elif "challenges" in q:
            answers.append(static_answers["challenges"])
        elif "latest developments" in q:
            answers.append(static_answers["developments"])
        elif "applied" in q:
            answers.append(static_answers["applications"])
        else:
            answers.append("Further research needed.")
    return answers

def summarize_findings(sub_questions, answers):
    """
    Simple summary generation: concatenate for demo purposes.
    In production, use LLM summarization.
    """
    summary = "Summary of findings:\n"
    for q, a in zip(sub_questions, answers):
        summary += f"- {q}\n  {a}\n"
    return summary

def mini_ai_research_assistant(main_question):
    sub_questions = generate_subquestions(main_question)
    print("Generated sub-questions:")
    for sq in sub_questions:
        print(" -", sq)
    answers = search_answers(sub_questions)
    print("\nAnswers:")
    for a in answers:
        print(" -", a)
    summary = summarize_findings(sub_questions, answers)
    print("\n" + summary)

if __name__ == "__main__":
    main_q = "How do LLM-based research assistants work?"
    mini_ai_research_assistant(main_q)
