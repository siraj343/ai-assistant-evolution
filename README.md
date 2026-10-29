# AI Assistant 🤖

Building my own AI assistant while learning AI Engineering.

## Tech Stack
- Python
- Ollama
- Qwen3:4b

## Progress
- Day 01: Built my first basic AI assistant using Python and Ollama.

- Day 02: Added environment variables using .env to avoid hardcoding configuration values and implemented a while loop for
continuous conversation with an exit condition.

- Day 03: Added conversation memory by storing user and assistant messages in a list, allowing the AI to use
previous messages as context.

- Day 04: Added a system prompt to define my AI assistant's personality, behavior, and response constraints. Learned the five ingredients of effective prompting: role, audience, task, constraints, and output format. 

- Day 05: Implemented tool calling (function calling), connecting LLM responses to Python functions using tool schemas, function mappings, and tool results.

- Day 06: Added a weather tool that accepts city arguments, learned argument extraction through tool calling, and enabled the assistant to choose between multiple tools.

- Day 07: Improved tool calling with a multi-step execution loop, added a user-city tool, and handled chained tool calls with step limits and error handling.

- Day 08: Refactored the AI agent with improved error handling, tool execution, debug logging, and reusable utilities. Added safer API response handling and organized the project structure.

- Day 09: Learned LLM streaming, collected response chunks into complete conversation history, and explored reconstructing streamed tool calls.

- Day 10: Integrated streaming into the AI agent for live responses and tool calls, and added Ctrl+C interruption handling.

- Day 11: Started learning RAG, generated text embeddings using Ollama, and implemented cosine similarity to compare semantic meaning between text samples.

- Day 12: Built a document search system using embeddings and cosine similarity. Added a knowledge base, ranked relevant documents using top-k retrieval, and explored embedding updates and semantic search limitations.

## Goal
To gradually make my AI assistant more advanced as I learn new concepts.