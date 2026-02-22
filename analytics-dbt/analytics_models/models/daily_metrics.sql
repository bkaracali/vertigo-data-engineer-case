{{ config(materialized='table') }}

WITH base_data AS (
    SELECT * FROM {{ source('raw_data', 'user_daily_metrics') }}
),

daily_agg AS (
    SELECT
        event_date,
        CASE 
			WHEN country IS NULL OR country = '' THEN 'Unknown' 
			ELSE country 
		END AS country,
        platform,
        COUNT(DISTINCT user_id) AS dau,
        SUM(iap_revenue) AS total_iap_revenue,
        SUM(ad_revenue) AS total_ad_revenue,
        SUM(match_start_count) AS matches_started,
        SUM(match_end_count) AS total_matches_ended,
        SUM(victory_count) AS total_victories,
        SUM(defeat_count) AS total_defeats,
        SUM(server_connection_error) AS total_server_errors
    FROM base_data
    GROUP BY 1, 2, 3
)

SELECT
    event_date,
    country,
    platform,
    dau,
    total_iap_revenue,
    total_ad_revenue,
    -- ARPDAU: (IAP + Ad Revenue) / DAU
    SAFE_DIVIDE((total_iap_revenue + total_ad_revenue), dau) AS arpdau,
    matches_started,
    -- Match per DAU: matches_started / dau
    SAFE_DIVIDE(matches_started, dau) AS match_per_dau,
    -- Win Ratio: victory / match_end
    SAFE_DIVIDE(total_victories, total_matches_ended) AS win_ratio,
    -- Defeat Ratio: defeat / match_end
    SAFE_DIVIDE(total_defeats, total_matches_ended) AS defeat_ratio,
    -- Server Error per DAU
    SAFE_DIVIDE(total_server_errors, dau) AS server_error_per_dau
FROM daily_agg