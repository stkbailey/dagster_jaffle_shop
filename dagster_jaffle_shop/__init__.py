from dagster import repository, load_assets_from_package_module

from dagster_jaffle_shop import assets
from dagster_jaffle_shop.jobs import materialize_all_job


asset_list = load_assets_from_package_module(assets)


@repository
def dbt_jaffle_shop():
    return asset_list + [materialize_all_job]
