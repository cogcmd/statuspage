BUNDLE_NAME          = statuspage
BUNDLE_VERSION      ?= 0.1
IMAGE_TAG            = cogcmd/$(BUNDLE_NAME):$(BUNDLE_VERSION)

.PHONY: docker docker-clean docker-shell docker-fresh

docker: Dockerfile .dockerignore
	docker build --rm -t $(IMAGE_TAG) .

docker-clean:
	docker rmi -f `docker images -q $(IMAGE_TAG)` || true

docker-shell:
	docker run --rm -it $(IMAGE_TAG) sh

docker-fresh: docker-clean docker
