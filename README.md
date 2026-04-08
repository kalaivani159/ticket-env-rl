# 🎟️ Ticket Booking RL Environment (OpenEnv)

## 🚀 Overview

This project implements a **Reinforcement Learning (RL) environment** for a ticket booking system using the **OpenEnv framework**.

The environment simulates real-world challenges such as:

* Limited seat allocation
* Payment failures
* Waitlist handling
* Cancellation & reallocation
* Priority-based booking

---

## 🎯 Objectives

* Design a **realistic RL environment**
* Ensure **correct runtime behavior**
* Follow **OpenEnv interface standards**
* Provide **clear grading logic**
* Enable **interpretable agent decisions**

---

## 🧠 Features

### ✅ Core Booking Logic

* Seat allocation under constraints
* Waitlist system
* Partial seat allocation
* Cancellation & reallocation

### 💳 Payment Handling

* Payment success / failure
* Retry payment
* Refund handling
* Edge case: payment deducted but failed

### 🔥 Intelligence Layer

* Priority-based allocation
* Smart agent decision making
* Handles conflicting requests

### ⭐ Explainability (Important)

Each step includes a **reason field**:

```
reason=Seats allocated successfully
reason=Payment retried successfully
reason=Already in waitlist
```

---

## 🏗️ Project Structure

```
ticket_env/
│
├── env.py
├── grader.py
├── inference.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── README.md
│
└── tasks/
    ├── easy.py
    ├── medium.py
    ├── hard.py
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---


## ▶️ Run the Environment

```bash

export HF_TOKEN= YOUR_HF_TOKEN

python inference.py
```

---

## 📊 Sample Output

```
[START] task=easy env=ticket_env model=baseline

[STEP] step=1 action={"action_type": "allocate", "user_id": "U1", "seats": 1} reward=0.45 done=false error=null reason=Seats allocated successfully

[STEP] step=2 action={"action_type": "allocate", "user_id": "U2", "seats": 1} reward=0.50 done=false error=null reason=Seats allocated successfully

[STEP] step=3 action={"action_type": "waitlist", "user_id": "U1", "seats": 0} reward=0.20 done=false error=null reason=Already in waitlist

[END] success=true steps=5 score=0.40 rewards=0.45,0.50,0.20,0.20,0.00
```

---

## 🧪 Tasks

### Easy

* All users have successful payments
* Goal: efficient allocation

### Medium

* Includes failed payments
* Requires retry + allocation strategy

### Hard

* Multiple users + limited seats
* Requires prioritization + smart allocation

---

## 📈 Grading Logic

The environment evaluates performance using:

* Allocation correctness (40%)
* Payment handling (30%)
* Efficiency (30%)

Score is normalized between **0 and 1**.

---

## 🌐 Demo

👉 Hugging Face Space (UI Demo):
     " link coming soon "

---

## 💻 GitHub Repository

👉 * GitHub link coming soon *

---

## 🧠 Tech Stack

* Python
* OpenEnv
* Gradio (for demo UI)

---

## 🏁 Conclusion

This project demonstrates:

* A **fully functional RL environment**
* **Real-world scenario modeling**
* **Clear evaluation metrics**
* **Explainable agent behavior**

---

## 🙌 Author

Kalaivani G
Kamalee S
Abirami M
