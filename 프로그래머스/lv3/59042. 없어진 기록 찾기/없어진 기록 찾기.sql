-- 코드를 입력하세요
SELECT
    o.ANIMAL_ID,
    o.NAME
FROM ANIMAL_INS i
RIGHT OUTER JOIN ANIMAL_OUTS o ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE i.ANIMAL_ID is NULL
ORDER BY o.ANIMAL_ID