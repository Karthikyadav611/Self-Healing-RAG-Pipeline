import pandas as pd
import datetime
import os

def log_query(query, answer, score, actions):
    # Create logs directory
    os.makedirs("logs", exist_ok=True)

    log_path = os.path.join("logs", "query_logs.csv")

    log_data = {
        "timestamp": [datetime.datetime.now()],
        "query": [query],
        "answer": [answer],
        "score": [score],
        "actions": [", ".join(actions)]
    }

    df = pd.DataFrame(log_data)

    df.to_csv(
        log_path,
        mode="a",
        index=False,
        header=not os.path.exists(log_path)
    )