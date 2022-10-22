import pandas

from dagster import asset, OpExecutionContext

from dagster_jaffle_shop.definitions import get_seed_filepath
from dagster_jaffle_shop.utils.io_managers import duckdb_io_manager


@asset(io_manager_def=duckdb_io_manager)
def raw_orders(context: OpExecutionContext) -> str:
    table_name = context.asset_key_for_output().to_string()
    f = get_seed_filepath(f"{table_name}.csv")
    query = f"SELECT * FROM read_csv_auto('{f}')"
    context.add_output_metadata({"query": query})
    return query
