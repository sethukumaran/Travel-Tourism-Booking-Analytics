# Travel & Tourism Booking Analytics

## Project overview
This project analyzes a travel-booking dataset to evaluate booking-funnel performance, revenue concentration, cancellation risk, customer experience, destinations, hotels, payment methods, and operational opportunities. The analysis is designed as a portfolio project for a data analyst role.

## Dataset
- File: `Travel-And-Tourism.csv`
- Grain: one row per booking
- Size: 1,000 bookings and 29 source columns
- Booking dates: January 2024 to August 2026
- Core entities: booking, customer, destination, hotel, transportation, payment, status, cost, and rating.

## Tools
- Python: pandas, numpy, matplotlib, seaborn
- SQL: PostgreSQL-compatible analytical queries
- GitHub: project documentation and reproducibility

## Analytical approach
1. Loaded and typed dates and numeric fields.
2. Validated missing values, duplicates, ranges, and status logic.
3. Created lead time, trip duration, post-discount revenue, cost per traveller, cost per night, and booking year.
4. Profiled the booking funnel and revenue by status.
5. Compared destinations, hotels, payment methods, transportation, and customer experience.
6. Built visualizations for management-oriented storytelling.
7. Translated business questions into reusable SQL queries.

## Key findings
- The dataset contains 1,000 bookings with no duplicate rows and no missing cells after ingestion.
- 772 bookings are completed, 141 are cancelled, 79 are confirmed, and 8 are pending.
- The observed cancellation rate is 14.1%; this is a realized cancellation rate, not a forecast.
- Completed bookings contribute approximately ₹169.99 million in gross trip value.
- Average completed trip value is approximately ₹220,196.
- Average completed customer rating is approximately 3.00/5, indicating a material service-quality improvement opportunity.
- Average booking lead time is approximately 95.8 days and average trip duration is approximately 5.4 days.
- Gross value is highly concentrated in international or premium destinations; decisions should therefore consider both value and cancellation/rating risk rather than bookings alone.

## Python analysis included
The Python script includes:
- Data loading.
- Date conversion.
- Numeric type conversion.
- Missing-value checks.
- Duplicate checks.
- Descriptive statistics.
- Booking-status analysis.
- Destination analysis.
- Payment-method analysis.
- Transportation analysis.
- Meal-plan analysis.
- Revenue analysis.
- Cancellation analysis.
- Customer-rating analysis.

# Feature engineering:
- Lead_Time_Days
- Trip_Duration_Days
- Revenue_After_Discount
- Cost_Per_Traveller
- Cost_Per_Night
- Booking_Year
# Visualizations for:
Booking status.
- Trip-cost distribution.
- Customer-rating distribution.
- Top destinations.
- Gross value by status.
- Completed revenue trend.

# SQL analysis included
The SQL file contains queries for:
- Data-quality profiling.
- Booking funnel and cancellation rate.
- Revenue by booking year.
- Destination performance.
- Cancellation reasons.
- Payment-method risk.
- Hotel rating versus customer rating.
- Booking lead time and trip duration.
- High-value completed bookings.
- Poor-experience operational review queue.

## Business insights
### 1. Protect high-value demand
Prioritize retention and payment assurance for high-value international bookings. A cancellation on a large group or premium itinerary creates more financial exposure than a cancellation on a short domestic trip. Use the SQL high-value query to create an account-management queue.

### 2. Treat cancellation as an operational problem
Cancellation reasons should be monitored by destination, payment method, lead-time band, and transportation type. Build an early-warning workflow for transportation disruption, visa issues, budget constraints, and work commitments.

### 3. Improve experience before increasing acquisition
An average completed rating near 3/5 suggests that additional bookings may not translate into repeat demand unless service delivery improves. Link hotel, destination, transportation, and review text to identify supplier-level root causes.

### 4. Use value-weighted destination decisions
Rank destinations on gross value, completed revenue, cancellation rate, average rating, and average booking value together. A destination with fewer bookings can still be strategically important if it generates high value and strong satisfaction.

### 5. Separate realized and pipeline metrics
Completed revenue is realized performance. Confirmed, pending, and cancelled trip values represent pipeline, uncertainty, and lost opportunity respectively; they should not be combined in a single revenue KPI.

## Limitations and assumptions
- `Total_Trip_Cost` is treated as gross booking value; profit, supplier cost, refunds, and net revenue are not available.
- The dataset appears synthetic or portfolio-oriented; findings should be validated against production data before commercial decisions.
- Ratings equal to zero are treated as not yet rated for future or cancelled bookings.
- Customer review comments are categorical text and require NLP or manual coding for deeper root-cause analysis.
- The file contains future travel dates relative to part of the booking history, so confirmed and pending bookings require pipeline treatment.

## Conclusion
The dataset shows a strong completed-booking base and substantial gross booking value. However, the business has two important priorities: reducing cancellations and improving customer experience.

From a senior analyst perspective, the recommended strategy is to manage the business through a value-weighted booking funnel:

1.Protect high-value confirmed and completed bookings.

2.Identify cancellation risk before travel.

3.Improve hotel and supplier performance.

4.Monitor customer ratings as a leading indicator of repeat demand.

5.Separate realized revenue from future pipeline.

6.Extend the analysis into a dashboard and cancellation-propensity model.

