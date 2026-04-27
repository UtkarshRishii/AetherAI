import datetime

def get_time_information() -> str:
    now = datetime.datetime.now()
    return (
        f"Current Real-Time Information:\n"
        f"Day: {now.strftime('%A')}\n"
        f"Date: {now.strftime('%Y-%m-%d')}\n"
        f"Month: {now.strftime('%B')}\n"
        f"Year: {now.strftime('%Y')}\n"
        f"Time: {now.strftime('%H:%M:%S')}\n"
    )