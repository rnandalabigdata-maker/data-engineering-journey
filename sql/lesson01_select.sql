-- Lesson 1: SELECT, WHERE, ORDER BY, LIMIT, DISTINCT
-- Database: practice (PostgreSQL)   Schema: insurance
-- Run a query: put your cursor inside it, then press Ctrl + E, Ctrl + E

-- Q1. Show the first 10 customers (all columns).

     select * from insurance.customers limit 10;

-- Q2. Show policy_id, product_type and face_amount for all ACTIVE policies.
   SELECT policy_id,product_type,face_amount FROM insurance.policies WHERE status = 'Active';
 
-- Q3. Show all 'Term Life' policies, biggest face_amount first.
    SELECT * FROM insurance.policies WHERE product_type = 'Term Life' ORDER BY face_amount DESC;


-- Q4. Show the 5 policies with the biggest face_amount
--     (rename face_amount to cover_amount in the result).
   SELECT policy_id,product_type,face_amount as cover_amount FROM insurance.policies ORDER BY face_amount DESC, policy_id LIMIT 5;

-- Q5. List the different product types we sell (each only once).
    SELECT DISTINCT product_type FROM insurance.policies;
   

-- Q6. Show policies issued on or after 1 January 2024.

    SELECT * FROM insurance.policies WHERE issue_date >= '2024-01-01';


-- Q7. Find customers who have NO email address.
   SELECT * FROM insurance.customers WHERE email is NULL;


-- Q8. Find payments with a NEGATIVE amount (a data-quality problem!).
  SELECT * FROM insurance.premium_payments WHERE amount < 0;
  SELECT count(*) FROM insurance.premium_payments WHERE amount < 0;

-- Q9. Show agents who work in the 'West' or 'Northeast' region.

    SELECT * FROM insurance.agents WHERE region IN('West','Northeast');

-- Q10. Show customers whose last name starts with 'S', sorted by last name.

 SELECT * FROM insurance.customers WHERE last_name LIKE 'S%' ORDER BY last_name,first_name,customer_id;

