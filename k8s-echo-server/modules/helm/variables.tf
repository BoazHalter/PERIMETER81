variable "k8s_host" {
  description = "Kubernetes API server host"
  type        = string
}

variable "k8s_cluster_ca" {
  description = "Kubernetes cluster CA certificate"
  type        = string
}

variable "k8s_token" {
  description = "Kubernetes token"
  type        = string
}

variable "echo_message" {
  description = "The message to echo"
  type        = string
}

