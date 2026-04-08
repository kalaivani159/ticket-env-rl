import asyncio
import os
import json
from datetime import datetime
from typing import List

from env import TicketEnv
from tasks.easy import get_task as easy_task
from tasks.medium import get_task as medium_task
from tasks.hard import get_task as hard_task
from grader import grade


# =========================
# ENV VARIABLES
# =========================
API_KEY = os.getenv("HF_TOKEN")
if not API_KEY:
    raise ValueError("HF_TOKEN is required")

MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
MAX_STEPS = 5


# =========================
# TIME FUNCTION
# =========================
def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# =========================
# LOGGING
# =========================
def log_start(task, env, model, episode):
    print(f"[{now()}] [START] episode={episode} task={task} env={env} model={model}", flush=True)


def log_step(step, action, reward, done, error, reason):
    action_json = json.dumps(action)
    error_val = error if error else "null"

    print(
        f"[{now()}] [STEP] step={step} action={action_json} reward={reward:.2f} done={str(done).lower()} error={error_val} reason={reason}",
        flush=True,
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[{now()}] [END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


# =========================
# SMART AGENT (ROTATION FIX)
# =========================
class SmartAgent:
    def __init__(self):
        self.index = 0
        self.priority_map = {"high": 0, "medium": 1, "low": 2}

    def act(self, state):
        users = state["users"]

        # 1. Fix payment first
        for u in users:
            if u["payment_status"] in ["failed", "deducted_failed"]:
                return {
                    "action_type": "retry_payment",
                    "user_id": u["id"],
                    "seats": 0
                }

        # 2. Sort by priority
        users_sorted = sorted(users, key=lambda x: self.priority_map[x["priority"]])

        # 3. Rotate users (KEY FIX ⭐)
        user = users_sorted[self.index % len(users_sorted)]
        self.index += 1

        if user["payment_status"] == "success":
            available = state["available_seats"]

            if available <= 0:
                return {
                    "action_type": "waitlist",
                    "user_id": user["id"],
                    "seats": 0
                }

            if user["requested_seats"] <= available:
                return {
                    "action_type": "allocate",
                    "user_id": user["id"],
                    "seats": user["requested_seats"]
                }

            return {
                "action_type": "partial_allocate",
                "user_id": user["id"],
                "seats": available
            }

        return {
            "action_type": "waitlist",
            "user_id": user["id"],
            "seats": 0
        }


agent = SmartAgent()


# =========================
# RUN TASK
# =========================
async def run_task(task_name, task_data):
    env = TicketEnv()
    state = env.reset(task_data)

    rewards: List[float] = []
    steps = 0

    episode_id = f"{task_name}_001"

    log_start(task_name, "ticket_env", MODEL_NAME, episode_id)

    try:
        for step in range(1, MAX_STEPS + 1):

            action = agent.act(state)

            state, reward, done, _ = env.step(action)

            reason = state["history"][-1]["reason"]

            rewards.append(reward)
            steps = step

            log_step(step, action, reward, done, None, reason)

            if done:
                break

        score = grade(state["history"])
        score = max(0.0, min(1.0, score))
        success = score >= 0.1

    except Exception as e:
        log_step(steps + 1, {"error": "exception"}, 0.0, True, str(e), "exception occurred")
        score = 0.0
        success = False

    finally:
        log_end(success, steps, score, rewards)


# =========================
# MAIN
# =========================
async def main():
    await run_task("easy", easy_task())
    await run_task("medium", medium_task())
    await run_task("hard", hard_task())


if __name__ == "__main__":
    asyncio.run(main())