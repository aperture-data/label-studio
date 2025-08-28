# console.sh - debug dockerfile with an environment like we see in cloud
run_args=()
run_args+=(--add-host host.docker.internal:host-gateway )

run_args+=(-e LABEL_STUDIO_APERTUREDB_KEY="moo")
run_args+=(-e LABEL_STUDIO_USERNAME=aperturedb@localhost )
run_args+=(-e LABEL_STUDIO_PASSWORD=41apertureDB3 )
run_args+=(-e LABEL_STUDIO_USER_TOKEN=PXq08K1kCwg9eTmhFPdwOgE5DEVvy5MejfW26p13EQvkse6w)
run_args+=(-e LABEL_STUDIO_CONFIGURED_STORAGE_BACKENDS="aperturedb gcs s3" )
run_args+=(-e LABEL_STUDIO_APERTUREDB_KEY="WzEsMSwiaG9zdC5kb2NrZXIuaW50ZXJuYWwiLCJpY21DTktpeHJsclRzaGpaR0xXUWg1SkY5bXoxSGpZVXUyYiJd")
run_args+=(-e LABEL_STUDIO_HOST="http://localhost:9001/labelstudio/")
run_args+=(-e LABEL_STUDIO_STATIC_PATH="/labelstudio/static/")
run_args+=(-e LABEL_STUDIO_URL_BASE="/labelstudio")
run_args+=(-e LABEL_STUDIO_DEBUG="FALSE")
run_args+=(-e LABEL_STUDIO_LOG_CONFIG_YAML="/app_config/ls_logging.yaml")
run_args+=(-e LABEL_STUDIO_CREATE_PROJ_TITLE="ApertureDB Labeling Data")
run_args+=(-e LABEL_STUDIO_DEFAULT_CLOUD_STORAGE="aperturedb")
run_args+=(-e LABEL_STUDIO_CLOUD_STORAGE_JSON_PATH="/app_config/cloud_storage_config.json")
# test config with spaces
#run_args+=(-e LABEL_STUDIO_CLOUD_STORAGE_JSON_PATH="/app_config/cloud config.json")
run_args+=(-p 9001:8000 )
run_args+=( --entrypoint=/bin/bash )
run_args+=( --user=0 )
run_args+=( -v ./app_config:/app_config )
run_args+=( --rm -it aperturedata/label-studio )
# docker run --rm -it --entrypoint=/bin/bash --user=0 aperturedata/label-studio

echo docker run ${run_args[@]}
docker run "${run_args[@]}"
