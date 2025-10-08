Email Validation System

When a user signs up for a website, the system needs to check if the email address is valid before saving it.

We can model this as a Finite Automaton (FA):

Each state represents a step in validating an email.

Transitions occur based on input characters (letters, digits, symbols like @ or .).

🎯 Goal:

Write a Python program that simulates a finite automaton to validate email addresses.

⚙️ Automata Design (Simplified DFA)

We define states:

q0 → Start  
q1 → After reading local part (before '@')
q2 → After '@' (reading domain part)
q3 → After '.' in domain
q_accept → Accept (valid email)


Transitions (simplified):

q0 → letter/digit → q1

q1 → letter/digit/._ → stay in q1

q1 → @ → q2

q2 → letter/digit → q2

q2 → . → q3

q3 → letter/digit → q_accept
