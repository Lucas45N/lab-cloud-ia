#!/bin/bash
set -e

echo "=== [1/4] Recompilando imagem Docker ==="
sudo docker compose build

echo "=== [2/4] Atualizando e recriando o contêiner em segundo plano ==="
sudo docker compose up -d --force-recreate

echo "=== [3/4] Limpando imagens antigas órfãs (FinOps/Disco) ==="
sudo docker image prune -f

echo "=== [4/4] Validando status do serviço (Health Check) ==="
sleep 2
curl -s http://localhost:8000/ | grep -q "status" && echo ">>> Deploy concluído com sucesso! API Online. <<<" || echo ">>> Falha no deploy. <<<"
