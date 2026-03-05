resource "databricks_cluster" "dataops_cluster" {
  cluster_name            = "dataops-cluster"
  spark_version           = "13.3.x-scala2.12"
  node_type_id            = "i3.xlarge"
  autotermination_minutes = 60
  num_workers             = 1
}

resource "databricks_job" "sales_job" {
  name = "sales-etl-job"

  existing_cluster_id = databricks_cluster.dataops_cluster.id

  notebook_task {
    notebook_path = "/Shared/sales_etl"
  }
}
