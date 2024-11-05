from model.minicpm import MiniCPM
from mteb import MTEB
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

model_path = '../../pretrained/gemma-2-2b-jpn-it'
# adapter_path = None
adapter_path = '/kaggle/input/llm-gemma-2-2b-jpn-it-finetune/out/20241103120758/checkpoint-1000'



model = MiniCPM(model_path=model_path,
                adapter_path=adapter_path)

TASK_LIST_RETRIEVAL = [
    "JaGovFaqsRetrieval",
    # "JaQuADRetrieval",
    # "JaqketRetrieval",

    # "MIRACLRetrieval",
    # "MIRACLRetrievalHardNegatives",
    # "MintakaRetrieval",
    # "MrTidyRetrieval",
    # "MultiLongDocRetrieval",
    
    # "NLPJournalAbsIntroRetrieval",
    # "NLPJournalTitleAbsRetrieval",
    # "NLPJournalTitleIntroRetrieval",

    # "XPQARetrieval",
]

for task in TASK_LIST_RETRIEVAL:
    logger.info(f"Running task: {task}")
    evaluation = MTEB(tasks=[task], task_langs=["jpn"])
    evaluation.run(model, output_folder=f"results/gemma-2-2b-jpn-it/retrieval")

