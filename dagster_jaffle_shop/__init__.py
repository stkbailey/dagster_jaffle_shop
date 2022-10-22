from dagster import repository, load_assets_from_package_module

from dagster_jaffle_shop import assets

asset_list = load_assets_from_package_module(assets)

@repository
def dbt_jaffle_shop():
    return asset_list