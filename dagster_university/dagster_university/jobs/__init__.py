from dagster import AssetSelection, define_asset_job


trips_by_week = AssetSelection.keys("trips_by_week")

trip_update_job = define_asset_job(
    name="trip_update_job",
    selection=AssetSelection.all() - trips_by_week
)

trips_by_week_update_job = define_asset_job(
    name="trips_by_week_update_job",
    selection=trips_by_week
)