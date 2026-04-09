-- logs 기반으로 pages 생성, 원래는 반대로 해야하지만, 작업 순번상 이렇게 작업
INSERT INTO pages (page_name, url, category)
SELECT DISTINCT page, 
       'https://example.com' || page,
       (ARRAY['Search', 'Community', 'Information', 'Shopping', 'Support'])[floor(random() * 5 + 1)]
FROM logs;

-- 대륙별 카테고리 top 3, 메모리 크기 조절 + 실행계획 조회 포함

-- SET work_mem = '64MB';
-- EXPLAIN ANALYZE

WITH regional_stats AS (
    SELECT COALESCE(c.region, 'nonexx') AS region_name
         , p.category AS category
         , COUNT(*) AS visit_count
      FROM logs l
      INNER JOIN pages p on p.page_name = l.page
      LEFT JOIN users u ON l.user_id = u.id
      LEFT JOIN countries c ON u.country = c.name
     GROUP BY COALESCE(c.region, 'nonexx'), p.category
),
ranked_stats AS (
    SELECT region_name
         , category
         , visit_count
         , DENSE_RANK() OVER (PARTITION BY region_name ORDER BY visit_count DESC) as rnk
      FROM regional_stats
)

SELECT region_name, rnk, category, visit_count
  FROM ranked_stats
 WHERE rnk <= 3
 ORDER BY region_name, rnk;