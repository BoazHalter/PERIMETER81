cluster_name     = "boaz-eks-cluster"
node_group_name  = "boaz-eks-node-group"
subnet_ids       = ["subnet-038d0338a87e6ff6a","subnet-0a81128286a577add"]
desired_capacity = 1
max_capacity     = 1
min_capacity     = 1
instance_type    = "t3.medium"
