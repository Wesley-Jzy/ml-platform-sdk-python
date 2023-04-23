import os
import wget
import volcengine_ml_platform
from volcengine_ml_platform import constant
from volcengine_ml_platform.util import cache_dir

volcengine_ml_platform.init()

CACHE_DIR = cache_dir.create("bert_glue")
print("start download glue_data ...")
tmp_file_path = CACHE_DIR.subpath("glue_data.tar.gz")
DATA_URL = 'https://ml-platform-public-examples-cn-beijing.tos-cn-beijing.volces.com/bert/glue/glue_data.tar.gz'
if not os.path.exists(tmp_file_path):
    wget.download(DATA_URL, out=tmp_file_path)

os.system(f"tar -zxvf {tmp_file_path} -C {CACHE_DIR.get_root_path()}")
os.system(f"rm {tmp_file_path}")
print("finish download glue_data")


print("start download bert model ...")
BERT_BASE_MODEL = 'bert-base-uncased'
tmp_file_path = CACHE_DIR.subpath(f"{BERT_BASE_MODEL}.tar.gz")
MODEL_URL = f'https://ml-platform-public-examples-cn-beijing.tos-cn-beijing.volces.com/bert/model/{BERT_BASE_MODEL}.tar.gz'
if not os.path.exists(tmp_file_path):
    wget.download(MODEL_URL, out=tmp_file_path)

os.system(f"tar -zxvf {tmp_file_path} -C {CACHE_DIR.get_root_path()}")
os.system(
    f"mv {CACHE_DIR.get_root_path()}/{BERT_BASE_MODEL} {CACHE_DIR.get_root_path()}/{BERT_BASE_MODEL}-model"
)
os.system(f"rm {tmp_file_path}")
print("finish download bert model")
