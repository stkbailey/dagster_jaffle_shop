import warnings

from dagster import repository, load_assets_from_package_module, ExperimentalWarning

from dagster_jaffle_shop import assets
from dagster_jaffle_shop.jobs import materialize_all_job


# Filter extraneous warnings that Dagster emits
warnings.filterwarnings("ignore", category=ExperimentalWarning)

asset_list = load_assets_from_package_module(assets)


@repository
def jaffle_shop_repo():
    return asset_list + [materialize_all_job]
