ifndef OPENAPI_SPEC
OPENAPI_SPEC=https://api.furiosa.ai/api/v1/openapi.yaml
endif

OPENAPI_GENERATOR_VERSION=3.0.2

generate-openapi:
	OPENAPI_GENERATOR_VERSION=3.0.2 java -jar share/openapi-generator-cli-5.0.1.jar generate -i ${OPENAPI_SPEC} -g python -c share/default.json -o ./
