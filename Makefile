dagit:
	dagit --package-name dagster_jaffle_shop

materialize:
	dagster job execute --package-name dagster_jaffle_shop -j materialize_all_job

format:
	black dagster_jaffle_shop tests

setup:
	touch /tmp/dagster.yaml