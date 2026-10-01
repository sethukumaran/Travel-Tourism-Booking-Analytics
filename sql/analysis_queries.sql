-- Travel & Tourism Analytics SQL 
-- Assumed table: travel_bookings

-- 1. Data quality profile
SELECT COUNT(*) AS rows, COUNT(DISTINCT booking_id) AS unique_bookings,
       COUNT(*) - COUNT(DISTINCT booking_id) AS duplicate_booking_ids
FROM travel_bookings;

-- 2. Booking funnel and cancellation rate
SELECT booking_status, COUNT(*) AS bookings,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS share_pct,
       SUM(total_trip_cost) AS gross_value
FROM travel_bookings
GROUP BY booking_status ORDER BY bookings DESC;

-- 3. Revenue KPIs by booking year
SELECT EXTRACT(YEAR FROM booking_date) AS booking_year,
       COUNT(*) AS bookings,
       SUM(CASE WHEN booking_status='Completed' THEN total_trip_cost ELSE 0 END) AS completed_revenue,
       AVG(CASE WHEN booking_status='Completed' THEN total_trip_cost END) AS avg_completed_value
FROM travel_bookings GROUP BY 1 ORDER BY 1;

-- 4. Destination performance
SELECT destination_city, destination_country, COUNT(*) AS bookings,
       SUM(total_trip_cost) AS gross_value,
       AVG(NULLIF(customer_rating,0)) AS avg_customer_rating,
       AVG(CASE WHEN booking_status='Cancelled' THEN 1.0 ELSE 0 END) AS cancellation_rate
FROM travel_bookings GROUP BY 1,2 ORDER BY gross_value DESC;

-- 5. Cancellation reasons
SELECT cancellation_reason, COUNT(*) AS cancellations,
       SUM(total_trip_cost) AS at_risk_value
FROM travel_bookings WHERE booking_status='Cancelled'
GROUP BY 1 ORDER BY cancellations DESC;

-- 6. Payment method risk
SELECT payment_method, COUNT(*) AS bookings,
       AVG(total_trip_cost) AS avg_booking_value,
       AVG(CASE WHEN booking_status='Cancelled' THEN 1.0 ELSE 0 END) AS cancellation_rate
FROM travel_bookings GROUP BY 1 ORDER BY cancellation_rate DESC;

-- 7. Customer experience: rating vs hotel quality
SELECT CASE WHEN hotel_rating < 2 THEN '1-1.9'
            WHEN hotel_rating < 3 THEN '2-2.9'
            WHEN hotel_rating < 4 THEN '3-3.9' ELSE '4-5' END AS hotel_rating_band,
       COUNT(*) AS bookings, AVG(NULLIF(customer_rating,0)) AS avg_customer_rating,
       AVG(total_trip_cost) AS avg_trip_cost
FROM travel_bookings GROUP BY 1 ORDER BY 1;

-- 8. Lead time and trip duration analysis
SELECT AVG(DATE_PART('day', travel_date-booking_date)) AS avg_lead_days,
       AVG(DATE_PART('day', return_date-travel_date)) AS avg_trip_days,
       AVG(total_trip_cost) AS avg_trip_cost
FROM travel_bookings;

-- 9. High-value completed trips for account management
SELECT booking_id, customer_id, destination_city, total_trip_cost,
       number_of_travellers, customer_rating
FROM travel_bookings WHERE booking_status='Completed'
ORDER BY total_trip_cost DESC LIMIT 20;

-- 10. Operational review queue: poor experience among completed trips
SELECT hotel_name, destination_city, COUNT(*) AS poor_experience_bookings,
       AVG(customer_rating) AS avg_rating, SUM(total_trip_cost) AS value
FROM travel_bookings
WHERE booking_status='Completed' AND customer_rating < 2
GROUP BY 1,2 HAVING COUNT(*) >= 3 ORDER BY poor_experience_bookings DESC;
