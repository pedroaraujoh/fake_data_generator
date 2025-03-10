#!/bin/bash

# Executa o notebook usando papermill
/home/ec2-user/.local/bin/papermill /home/ec2-user/script_fake_generator/fake_data_generator.ipynb /home/ec2-user/papermill_output/fake_data_generator.ipynb

# Opcional: salvar logs
echo "Notebook executado em $(date)" >> /home/ec2-user/exec_logs/exec_log.txt
