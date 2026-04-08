def get_task():
    return {
        "available_seats": 1,
        "users": [
            {
                "id": "U1",
                "requested_seats": 1,
                "payment_status": "deducted_failed",  # ⭐ NEW CASE
                "priority": "high"
            },
            {
                "id": "U2",
                "requested_seats": 1,
                "payment_status": "success",
                "priority": "medium"
            }
        ],
        "waitlist": [],
        "history": []
    }