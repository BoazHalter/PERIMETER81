{{- define "echo-server.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "echo-server.labels" -}}
app.kubernetes.io/name: {{ include "echo-server.name" . }}
helm.sh/chart: {{ include "echo-server.chart" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "echo-server.selectorLabels" -}}
app.kubernetes.io/name: {{ include "echo-server.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "echo-server.name" -}}
{{- .Chart.Name -}}
{{- end }}

{{- define "echo-server.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version -}}
{{- end }}
