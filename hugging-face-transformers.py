from transformers import pipeline

# Initialize the QA pipeline
qa_pipeline = pipeline("question-answering")

# Provide the context
context = """
Marie Curie was a physicist and chemist who conducted pioneering research on radioactivity. 
She was the first woman to win a Nobel Prize and is the only person to win Nobel Prizes in two different scientific fields. 
Her notable achievements include the development of the theory of radioactivity, techniques for isolating radioactive isotopes, and the discovery of two elements, polonium and radium. 
She also founded the Curie Institutes in Paris and Warsaw, which remain major centers of medical research today. 
Curie faced many obstacles, including widespread sexism in science and the dangers of handling radioactive materials, which ultimately contributed to her death in 1934.
"""

# Define the questions
questions = [
    "Who was Marie Curie?",
    "What notable achievements did Marie Curie have?",
    "What were the names of the elements Marie Curie discovered?",
    "What obstacles did Marie Curie face?",
    "When did Marie Curie die?"
]

# Extract the answers
for question in questions:
    result = qa_pipeline(question=question, context=context)
    print(f"Question: {question}")
    print(f"Answer: {result['answer']}\n")
