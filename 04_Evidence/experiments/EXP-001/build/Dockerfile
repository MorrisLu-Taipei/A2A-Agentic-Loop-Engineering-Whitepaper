# EXP-001 runner image — 全程容器內執行(對齊 ALE §9.4 不依賴本機)
FROM python:3.11-slim

RUN pip install --no-cache-dir \
    pytest==8.* pytest-cov==5.* hypothesis==6.* mutmut==2.* \
    openai==1.*

WORKDIR /exp
# runner 與任務在 compose 以 volume 掛入 /exp
ENTRYPOINT ["python"]
