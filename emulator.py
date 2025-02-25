import random
import time


def emulate_api_request():
    response = {
        "_embedded": {
            "leads": []
        }
    }

    id = random.randint(3, 7)

    for i in range(random.randint(1,20)):
        lead = {
            "id": id,
            "name": f"Lead {id}",
            "price": round(random.uniform(1000, 50000), 2),
            "responsible_user_id": random.randint(10000, 99999),
            "group_id": random.randint(100, 500),
            "status_id": random.randint(1, 10),
            "pipeline_id": random.randint(1, 5),
            "loss_reason_id": random.choice([None, random.randint(1, 100)]),
            "created_by": random.randint(10000, 99999),
            "updated_by": random.randint(10000, 99999),
            "created_at": int(time.time()) - random.randint(10000, 50000),
            "updated_at": int(time.time()),
            "closed_at": random.choice([None, int(time.time()) - random.randint(1000, 10000)]),
            "closest_task_at": random.choice([None, int(time.time()) + random.randint(1000, 10000)]),
            "is_deleted": random.choice([True, False]),
            "custom_fields_values": [
                {
                    "field_id": random.randint(1, 100),
                    "field_name": "Custom Field",
                    "values": [{"value": f"Value {random.randint(1, 100)}"}]
                }
            ],
            "account_id": random.randint(1000000, 9999999),
            "labor_cost": random.choice([None, round(random.uniform(100, 1000), 2)])
        }
        response["_embedded"]["leads"].append(lead)

    return response


if __name__ == "__main__":
    print(emulate_api_request())
