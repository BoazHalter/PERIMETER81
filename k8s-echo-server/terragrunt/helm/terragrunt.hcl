terraform {
  source = "../../modules/helm"
}

dependency "eks" {
  config_path = "../eks"
}

inputs = {
  k8s_host                   = dependency.eks.outputs.cluster_endpoint
  k8s_cluster_ca             = dependency.eks.outputs.cluster_certificate_authority
  k8s_token                  = data.aws_eks_cluster_auth.token.token
  echo_message               = "Hello from Helm deployment"
}

