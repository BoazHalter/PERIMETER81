terraform {
  source = "../../modules/eks"
}

dependency "vpc" {
  config_path = "../vpc"
}

inputs = {
  cluster_name     = "my-eks-cluster"
  node_group_name  = "my-node-group"
  subnet_ids       = dependency.vpc.outputs.public_subnets
  desired_capacity = 1
  max_capacity     = 1
  min_capacity     = 1
  instance_type    = "t3.medium"
}

