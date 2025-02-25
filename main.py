import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Lead, Base

DATABASE_URL = "sqlite:///leads.db"
engine = create_engine(DATABASE_URL, echo=True)


# Создаём сессию
Session = sessionmaker(bind=engine)
session = Session()


def process_json_files(files):
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for lead in data["_embedded"]["leads"]:
            lead_obj = session.query(Lead).filter_by(id=lead["id"]).first()

            fields_to_update = [
                "name", "price", "responsible_user_id", "group_id", "status_id", "pipeline_id",
                "loss_reason_id", "created_by", "updated_by", "created_at", "updated_at",
                "closed_at", "closest_task_at", "is_deleted", "account_id", "labor_cost"
            ]

            lead_data = {field: lead[field] for field in fields_to_update}
            lead_data["custom_fields"] = json.dumps(lead.get("custom_fields_values", []))

            if lead_obj:
                for field, value in lead_data.items():
                    setattr(lead_obj, field, value)
            else:
                new_lead = Lead(id=lead["id"], **lead_data)
                session.add(new_lead)

        session.commit()


# Пути к JSON-файлам
json_files = ["leads_response_1.json", "leads_response_2.json"]


def main():
    process_json_files(json_files)
    session.close()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()

