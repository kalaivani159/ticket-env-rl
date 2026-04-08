def get_task():
    return {
        "available_seats": 2,
        "users": [
            {
                "id": "U1",
                "requested_seats": 1,
                "payment_status": "success",
                "priority": "low"
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