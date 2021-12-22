# Threads
- Basic unit of CPU utilization
- Consists of
    - Thread ID
    - Program Counter (PC)
    - Register Sets
    - Stack Segment Memory

>If one thread crashes, all threads crashes.

- Consumes less resource

![Threads](threads.drawio.svg)

## A real world example

### MS word (process)
You are typing a paragraph on MS word. But in background one more thread running and checking your spelling mistakes. As soon as you do a typo the other thread notifies you about the typo.. And makes your life easy.