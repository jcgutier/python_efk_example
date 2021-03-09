FROM fluentd:latest
USER root
RUN fluent-gem install fluent-plugin-elasticsearch
RUN apk add curl
USER fluent
