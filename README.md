# Student Information
* **Name:** Emine Ezgi Akcaöz
* **Student Number:** 2504109902
* **Department:** Management Information Systems
* **Course Name:** MIS 203 - Basic Programming

---

## AI Reflection
* **AI Tool Used:** Gemini
* **Prompt Used:** "Write a python code that asks the student for name, department, age, career goal and prints them in one line as a student profile."
* **What did you change?:** I adjusted the print format to display the profile as a single continuous line as required in the assignment instructions.

## Week 02
* **AI Tool Used:** Gemini
* **Prompt Used:** How can I do this assignment? I created a folder named week02, what should I do next? Explain step by step.
* **What did you change?:** I reviewed the code and made sure the variables are named properly.
* **What does break do in your program?:** It stops the while loop immediately when the user enters 'quit' or 'q'.

## Week 03
**AI Tool Used:** Gemini
**Prompt Used:** "How can I write a cinema ticket Python program using while loops and if/elif conditions?"
**What did you change?** I updated the variable names and fixed the discount order to match the assignment rules.
**Tests:** 
1. Input: Age 5, Day weekday, Student no -> Result: 0.00 TRY (Free)
2. Input: Age 20, Day weekend, Student yes -> Result: 175.00 TRY (Student)
3. Input: Age 150 -> Result: Invalid age.
**Why does the order of the rules matter?** The order ensures the biggest discount is applied first. If "Student" comes before "Child", a 10-year-old would get a smaller discount (30% instead of 40%).


## Week 04
* **AI Tool Used:** Gemini
* **Prompt Used:** "How can I write a hotel reservation Python program using dictionaries and loops?"
* **What did you change?:** I organized the capacity checks and variable names.
* **Tests:**
  1. Input: Economy, 1 adult -> Result: 1500.00 TRY
  2. Input: Superior, 1 adult, 1 child (age 5), 2 nights -> Result: 5000.00 TRY
  3. Input: Economy, 4 guests -> Result: Capacity error.
* **Why does the order of the rules matter?:** The order ensures child age checks are evaluated first to apply correct discounts before regular pricing.
