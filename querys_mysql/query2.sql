-- SEGUNDA QUERY

WITH ultimo_ano AS (
    SELECT 
        MAX(data) as data_final,
        DATE_SUB(MAX(data), INTERVAL 1 YEAR) as data_inicial
    FROM contabil
)
SELECT 
    co.razao_social AS "Nome da Operadora",
    co.registro_ans AS "Registro ANS",
    SUM(CAST(c.vl_saldo_final AS DECIMAL(15,2))) as "Total de Despesas (R$)"
FROM contabil c
INNER JOIN cadastro_operadora co ON c.registro_ans = co.registro_ans
INNER JOIN ultimo_ano ua ON c.data BETWEEN ua.data_inicial AND ua.data_final
WHERE c.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
GROUP BY 
    co.razao_social,
    co.registro_ans
HAVING SUM(CAST(c.vl_saldo_final AS DECIMAL(15,2))) > 0
ORDER BY 
    "Total de Despesas (R$)" DESC
LIMIT 10;