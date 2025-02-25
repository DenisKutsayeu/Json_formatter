from emulator import emulate_api_request
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = "leads.db"
CSV_PATH = "leads_export.csv"
PAGE_COUNT = 30


engine = create_engine(f"sqlite:///{DB_PATH}")
Session = sessionmaker(bind=engine)
session = Session()


# def load_data_to_db():
#     for page in range(1, PAGE_COUNT + 1):
#         print(f"Загружаем страницу {page}...")
#         data = emulate_api_request()
#
#         for lead in data["_embedded"]["leads"]:
#             if not session.query(Lead).filter_by(id=lead["id"]).first():  # Проверка на дубликаты
#                 new_lead = Lead(**lead)
#                 session.add(new_lead)
#
#         session.commit()


def fetch_api_data():
    all_leads = []

    for page in range(1, PAGE_COUNT + 1):
        print(f"Загружаем страницу {page}...")
        data = emulate_api_request()
        all_leads.extend(data["_embedded"]["leads"])

    return all_leads


def save_to_csv(leads):
    df = pd.DataFrame(leads)
    df.to_csv(CSV_PATH, index=False)
    print(f"Данные сохранены в {CSV_PATH}")


def main():
    # load_data_to_db()
    leads = fetch_api_data()
    save_to_csv(leads)
    session.close()


if __name__ == "__main__":
    main()