provider "helm" {
  kubernetes {
    host                   = var.k8s_host
    cluster_ca_certificate = base64decode(var.k8s_cluster_ca)
    token                  = var.k8s_token
  }
}

resource "helm_release" "echo_server" {
  name       = "echo-server"
  repository = "https://charts.helm.sh/stable"
  chart      = "echo-server"
  values = [<<EOF
replicaCount: 1
image:
  repository: "echo-server-image"
  tag: "latest"
env:
  - name: ECHO_MESSAGE
    value: ${var.echo_message}
EOF
  ]
}

