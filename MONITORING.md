# Possibilities to use a Monitoring System with RAG

- Use proxy metrics to monitor the performance of the RAG model
  - use feedback (good / bad answers)
  - data drift
  - model prediction drift
  - LLM based grading
    - use other LLM for evaluation
    - use response validation
  - use text descriptors (structured representation of questions / answers)
- Direct Metrics
  - number of references sources
  - % of questions answered correctly (user feedback)
  - % context used in answers
  - topic modeling -> statistical analysis of the questions

## Monitoring Tools
- evidently
- langsmith -> paid service
- weave / traces (wandb)
- https://github.com/langfuse/langfuse
- https://github.com/Arize-ai/phoenix

## RAG UI 
- https://github.com/technologiestiftung/parla-frontend 
  - parla.berlin