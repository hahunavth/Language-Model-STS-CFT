from model.minicpm import MiniCPM
from mteb import MTEB
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

model_path = '../../pretrained/gemma-2-2b-jpn-it'
# adapter_path = None 
adapter_path = '/kaggle/input/llm-gemma-2-2b-jpn-it-finetune/out/20241102143347/checkpoint-1000'

model = MiniCPM(model_path=model_path,
                adapter_path=adapter_path)

TASK_LIST_STS = [
    "JSTS", # INSTALL datasets==2......
]

for task in TASK_LIST_STS:
    logger.info(f"Running task: {task}")
    evaluation = MTEB(tasks=[task], task_langs=["jpn"])
    evaluation.run(model, output_folder=f"results/gemma-2-2b-jpn-it/sts")
