from pathlib import Path
import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
# store in a simple app dir in the user's home for cross-platform compatibility
SCORE_DIR = Path.home() / ".number_guess"
SCORE_DIR.mkdir(parents=True, exist_ok=True)
SCORE_PATH = SCORE_DIR / "highest_score.json"

from datetime import timezone

def load_best_score():
    """Return tuple (score:int, iso_ts:str) or None"""
    try:
        if SCORE_PATH.exists():
            data = json.loads(SCORE_PATH.read_text(encoding="utf-8"))
            score = data.get("score")
            ts = data.get("saved_at")
            if score is None:
                return None
            return (int(score), ts)
    except Exception as e:
        logger.exception("Failed to load best score: %s", e)
    return None


def save_best_score(score: int):
    try:
        payload = {"score": int(score), "saved_at": datetime.now(timezone.utc).isoformat()}
        SCORE_DIR.mkdir(parents=True, exist_ok=True)
        SCORE_PATH.write_text(json.dumps(payload), encoding="utf-8")
    except Exception as e:
        logger.exception("Failed to save best score: %s", e)


def reset_best_score():
    try:
        if SCORE_PATH.exists():
            SCORE_PATH.unlink()
    except Exception as e:
        logger.exception("Failed to reset best score: %s", e)
