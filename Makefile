VENV_PATH=~/PycharmProjects/wtecc-CICD_PracticeCode/labs/01_base_pipeline/venv
SOURCE_PATH=~/project/Python/mdd-invest

install:
	source $(VENV_PATH)/bin/activate && pip3 install -r $(SOURCE_PATH)/requirements.txt

run:
	source $(VENV_PATH)/bin/activate && python3 $(SOURCE_PATH)/main.py && python3 $(SOURCE_PATH)/draw_mdd_data.py

.PHONY: run install
