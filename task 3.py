# ========== System Components ==========

class PlannerAgent:
    def __init__(self):
        pass

    def decompose_task(self, task):
        # Decompose task into sub-tasks (stub example)
        return [
            f"Literature Review for {task}",
            f"Collect Latest Papers on {task}",
            f"Summarize Key Trends in {task}",
            f"Prepare Research Summary for {task}"
        ]


class RetrieverAgent:
    def __init__(self):
        pass

    def retrieve(self, query):
        # Simulate document retrieval (stub example)
        print(f"Retrieving documents for: {query}")
        return [f"Doc1 about {query}", f"Doc2 about {query}"]


class AnalyzerAgent:
    def __init__(self):
        pass

    def analyze(self, documents):
        # Simulate analysis (stub example)
        print(f"Analyzing {len(documents)} documents...")
        return [f"Key insights from {doc}" for doc in documents]

class WriterAgent:
    def __init__(self):
        pass

    def generate_summary(self, insights):
        # Simple concatenation (stub example)
        return " ".join(insights)

# ========== Coordinator ==========

class OpenDeepResearchSystem:
    def __init__(self):
        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.analyzer = AnalyzerAgent()
        self.writer = WriterAgent()
    
    def run(self, main_task):
        print(f"[System] Starting Deep Research Project on: {main_task}")
        sub_tasks = self.planner.decompose_task(main_task)
        all_insights = []
        for task in sub_tasks:
            docs = self.retriever.retrieve(task)
            insights = self.analyzer.analyze(docs)
            all_insights.extend(insights)
        summary = self.writer.generate_summary(all_insights)
        print(f"\n[System] Research Summary:\n{summary}")

# ========== Example Usage ==========

if __name__ == "__main__":
    system = OpenDeepResearchSystem()
    system.run("Advancements in Large Language Models")
