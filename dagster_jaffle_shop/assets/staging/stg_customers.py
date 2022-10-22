from dagster import asset, OpExecutionContext

from dagster_jaffle_shop.utils.io_managers import duckdb_io_manager
from dagster_jaffle_shop.utils.queries import render_jinja_template


@asset(io_manager_def=duckdb_io_manager)
def stg_customers(context: OpExecutionContext, raw_customers: str) -> str:
    query = """
    with source as (

        {#-
        Normally we would select from the table here, but we are using seeds to load
        our data in this project
        #}
        select * from {{ ref('raw_customers') }}

    ),

    renamed as (

        select
            id as customer_id,
            first_name,
            last_name

        from source

    )

    select * from renamed

    """
    return render_jinja_template(query)
