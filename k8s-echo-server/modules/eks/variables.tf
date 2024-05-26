variable "ssh_key_name" {
  description = "ssh_key_name"
  type        = string
}
variable "cluster_name" {
  description = "The name of the EKS cluster"
  type        = string
}
variable "vpc_id" {
  description = "vpc_id"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs"
  type        = list(string)
}

variable "desired_capacity" {
  description = "Desired number of worker nodes"
  type        = number
}

variable "max_capacity" {
  description = "Maximum number of worker nodes"
  type        = number
}

variable "min_capacity" {
  description = "Minimum number of worker nodes"
  type        = number
}

variable "instance_type" {
  description = "EC2 instance type for the nodes"
  type        = string
}
variable "vpc_cidr_block" {
  description = "vpc_cidr_block"
  type        = string
}

