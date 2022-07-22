local-build:
	docker-compose -f docker-compose-local.yml build

local-up:
	docker-compose -f docker-compose-local.yml up -d

local-stop:
	docker-compose -f docker-compose-local.yml stop

local-api-bash:
	docker exec -ti fondeadora-url-shortener-api /bin/bash

local-api-logs:
	docker logs -f fondeadora-url-shortener-api

local-rebuild:
	docker-compose -f docker-compose-local.yml up -d --build