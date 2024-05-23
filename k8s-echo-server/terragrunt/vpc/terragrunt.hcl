terraform {
  source = "../../modules/vpc"
}

inputs = {
  vpc_cidr           = "10.0.0.0/16"
  public_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24"]
  azs                 = ["us-west-2a", "us-west-2b"]
}

