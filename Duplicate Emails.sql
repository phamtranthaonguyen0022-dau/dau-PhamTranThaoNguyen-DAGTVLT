SELECT Email
FROM (
    SELECT email AS Email, COUNT(*) AS cnt
    FROM Person
    GROUP BY email
) t
WHERE cnt > 1;