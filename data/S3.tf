resource "aws_s3_bucket" "raw_bucket" {
  bucket = "enterprise-raw-sales-bucket"
}

resource "aws_s3_bucket" "processed_bucket" {
  bucket = "enterprise-processed-sales-bucket"
}
