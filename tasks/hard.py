def get_task():
    return {
        "available_seats": 2,
        "users": [
            {
                "id": "U1",
                "requested_seats": 2,
                "payment_status": "failed",
                "priority": "high"
            },
            {
                "id": "U2",
                "requested_seats": 1,
                "payment_status": "success",
                "priority": "medium"
            },
            {
                "id": "U3",
                "requested_seats": 1,
                "payment_status": "success",
                "priority": "low"
            }
        ],
        "waitlist": [],
        "history": []
    }