# Program vs Process

**PROGRAM:**
- An executable file that is stored on a hard disk or a secondary memory.
- Passive entity
- Memory: texts

**PROCESS:**
- The file or program under execution.
- Active entity
- Memory: stack + data + heap + text 



# PROCESS STATE DIAGRAM
![State Diagram](process_state_diagram.drawio.svg)


## Each state means?

### ***NEW***
    - BATCH OS - Job arived in the job queue
    - Time sharing OS - process is being created
### ***READY***
    - Process waiting is ready queue for being assigned to a CPU/Processor
### ***RUNNING***
    - pgm is being executed on the cPU
### ***WAITING***
    - Process is waiting for some event to occur(I/O)
### ***TERMINATED***
    - Process has finished its execution