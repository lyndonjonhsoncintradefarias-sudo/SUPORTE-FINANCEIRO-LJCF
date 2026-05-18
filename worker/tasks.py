import os
from datetime import timedelta

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# App configuration
# ---------------------------------------------------------------------------

broker_url = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
result_backend = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

celery_app = Celery(
    "worker",
    broker=broker_url,
    backend=result_backend,
    include=["worker.tasks"],
)

celery_app.conf.update(
    # Serialisation
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    # Timezone
    timezone="UTC",
    enable_utc=True,
    # Beat schedule — add your periodic tasks here
    beat_schedule={
        "example-periodic-task": {
            "task": "worker.tasks.example_periodic_task",
            "schedule": timedelta(minutes=5),
        },
    },
)

# ---------------------------------------------------------------------------
# Tasks
# ---------------------------------------------------------------------------


@celery_app.task(name="worker.tasks.example_periodic_task", bind=True)
def example_periodic_task(self):
    """Periodic task executed every 5 minutes by Beat.

    Replace or extend this with your own business logic.
    """
    print("Running example periodic task")
    return {"status": "ok"}


@celery_app.task(name="worker.tasks.example_task", bind=True)
def example_task(self, message: str = "hello"):
    """One-off task that can be dispatched on demand.

    Usage:
        from worker.tasks import example_task
        example_task.delay("your message here")
    """
    print(f"Running example task: {message}")
    return {"status": "ok", "message": message}
