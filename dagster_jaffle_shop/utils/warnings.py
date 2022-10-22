"Filter warnings about Dagster experimental configs."
import warnings

from dagster import ExperimentalWarning


warnings.filterwarnings("ignore", category=ExperimentalWarning)
