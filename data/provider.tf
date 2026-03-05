provider "aws" {
  region = "ap-south-1"
}

provider "databricks" {
  host  = var.databricks_host
  token = var.databricks_token
}
