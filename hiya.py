print("hello git")

_GCP_REGION	[YOUR GCP_REGION]
_CUSTOM_SERVICE_ACCOUNT	[YOUR CUSTOM_SERVICE_ACCOUNT]
_ENDPOINT	[Your inverting proxy host pipeline ENDPOINT]
_TFX_IMAGE_NAME	lab-03-tfx-image
_PIPELINE_NAME	tfx_covertype_continuous_training
_MODEL_NAME	tfx_covertype_classifier
_DATA_ROOT_URI	gs://cloud-training/OCBL203/workshop-datasets
_PIPELINE_FOLDER	workshops/tfx-caip-tf23/lab-03-tfx-cicd/labs/pipeline
_PIPELINE_DSL	runner.py
_PYTHON_VERSION	3.7
_RUNTIME_VERSION	2.3
_USE_KFP_SA	False
_ENABLE_TUNING	True


starting build "e7fd1867-22ff-435f-8bc0-10c2840ee0f6"

FETCHSOURCE
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Initialized empty Git repository in /workspace/.git/
From https://github.com/krishnayogik/Data-Science-Python
 * branch            078a0d03b6e7e26320ae2385143e0c3dfa79768a -> FETCH_HEAD
HEAD is now at 078a0d0 Create test.txt
BUILD
Starting Step #0
Step #0: Already have image (with digest): gcr.io/cloud-builders/docker
Step #0: invalid argument "gcr.io/qwiklabs-gcp-04-8ab3c72d4a82/lab-03-tfx-image:" for "-t, --tag" flag: invalid reference format
Step #0: See 'docker build --help'.
Finished Step #0
ERROR
ERROR: build step 0 "gcr.io/cloud-builders/docker" failed: step exited with non-zero status: 125
